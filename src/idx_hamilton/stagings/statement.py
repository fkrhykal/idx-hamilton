import collections
import io
import itertools
import logging
import os
import zipfile
from abc import ABC
from collections.abc import Sequence
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import IO, ClassVar, cast

import patito as pt
import polars as pl
from hamilton.function_modifiers import (
    extract_fields,
    parameterize,
    source,
    value,
)
from hamilton.function_modifiers.dependencies import ParametrizedDependency
from ixbrlparse import IXBRL, ixbrlNumeric

from idx_hamilton.models import Model
from idx_hamilton.sources import IxbrlFilling, Period

type FilePath = str

type StatementCode = str

type Variant = str

type Variants = dict[StatementCode, Variant]

log = logging.getLogger(__name__)


class EntryPoint(StrEnum):
    GENERAL = "1"
    PROPERTY = "2"
    INFRASTRUCTURE = "3"
    FINANCIAL_AND_SHARIA = "4"
    SECURITIES = "5"
    INSURANCE = "6"
    COLLECTIVE_INVESTMENT_CONTRACT = "7"
    FINANCING = "8"

    @classmethod
    def from_char(cls, char: str) -> EntryPoint | None:
        if char in cls._value2member_map_:
            return cls(char)
        return None

    def slug(self) -> str:
        return self._name_.lower()


@dataclass(frozen=True)
class Statement(ABC):
    statement_type: ClassVar[str]
    variants: ClassVar[Variants]

    filling: IxbrlFilling
    filepath: FilePath

    @property
    def basename(self) -> str:
        return self.filepath.split("/")[-1]

    @property
    def code(self) -> StatementCode:
        return self.basename[1:7]

    @property
    def variant(self) -> Variant:
        return self.variants[self.code]

    @property
    def entry_point(self) -> EntryPoint:
        entry_point = EntryPoint.from_char(self.filepath[0])
        if not entry_point:
            raise ValueError("Entry point should not be None")
        return entry_point

    def read_bytes(self) -> bytes:
        with zipfile.ZipFile(self.filling.zip_path) as z:
            return z.read(self.filepath)

    def to_ixbrl(self) -> IXBRL:
        return self._normalize_ixbrl(io.BytesIO(self.read_bytes()))

    def _normalize_ixbrl(self, content: IO[bytes]) -> IXBRL:
        normalized = (
            content.read()
            .replace(b"ix:nonnumeric", b"ix:nonNumeric")
            .replace(b"ix:nonfraction", b"ix:nonFraction")
            .replace(b"contextref=", b"contextRef=")
            .replace(b"unitref=", b"unitRef=")
        )
        return IXBRL(io.BytesIO(normalized))


@dataclass(frozen=True)
class BalanceStatement(Statement):
    statement_type: ClassVar[str] = "balance_statement"
    variants: ClassVar[dict[str, str]] = {
        "210000": "current_and_non_current",
        "220000": "liquidity",
    }


@dataclass(frozen=True)
class IncomeStatement(Statement):
    statement_type: ClassVar[str] = "income_statement"
    variants: ClassVar[dict[str, str]] = {
        "311000": "by_function_after_tax",
        "321000": "by_function_before_tax",
        "312000": "by_nature_after_tax",
        "322000": "by_nature_before_tax",
    }


@dataclass(frozen=True)
class CashFlowStatement(Statement):
    statement_type: ClassVar[str] = "cash_flow_statement"
    variants: ClassVar[dict[str, str]] = {
        "510000": "direct_method",
        "520000": "indirect_method",
    }


class Account(Model):
    statement: str
    variant: Variant
    emiten_code: str
    year: int
    period: Period
    context: str
    account: str
    value: float

    class c:
        statement: pl.Expr
        variant: pl.Expr
        emiten_code: pl.Expr
        year: pl.Expr
        period: pl.Expr
        context: pl.Expr
        account: pl.Expr
        value: pl.Expr


STATEMENTS = (
    BalanceStatement,
    IncomeStatement,
    CashFlowStatement,
)

STATEMENT_REGISTRY = {code: cls for cls in STATEMENTS for code in cls.variants}

DEI = "1000000.html"


@extract_fields({ep.slug(): list[Statement] for ep in EntryPoint})
def route_statements(
    ixbrl_fillings: list[IxbrlFilling],
) -> dict[str, list[Statement]]:
    routed: dict[str, list[Statement]] = {ep.slug(): [] for ep in EntryPoint}

    for filling in ixbrl_fillings:
        with zipfile.ZipFile(filling.zip_path) as z:
            for filepath in z.namelist():
                base_name = filepath.split("/")[-1]
                if base_name == DEI or len(base_name) < 7:
                    continue
                code: StatementCode = base_name[1:7]
                stmt_cls = STATEMENT_REGISTRY.get(code)
                if not stmt_cls:
                    continue
                ep = EntryPoint.from_char(filepath[0])
                if not ep:
                    continue
                stmt_instance = stmt_cls(filling=filling, filepath=filepath)
                routed[ep.slug()].append(stmt_instance)

    return routed


def _parse_statement(stmt: Statement) -> list[Account]:
    records: list[Account] = []
    try:
        ixbrl = stmt.to_ixbrl()
        for numeric in cast(list[ixbrlNumeric], ixbrl.numeric):
            if numeric.value is None:
                continue
            records.append(
                Account(
                    statement=stmt.statement_type,
                    variant=stmt.variant,
                    emiten_code=stmt.filling.emiten_code,
                    year=stmt.filling.year,
                    period=stmt.filling.period,
                    context=str(numeric.context),
                    account=str(numeric.name),
                    value=float(numeric.value),
                )
            )
    except Exception as err:  # noqa: BLE001
        log.warning("[PARSE_STATEMENT_ERROR] %s", err)
        return []
    return records


class ParquetTarget(tuple[int, Period]):
    @property
    def year(self):
        return self[0]

    @property
    def period(self):
        return self[1]

    def target_path(self, base_dir: Path) -> Path:
        return base_dir / f"{self[0]}_{self[1]}.parquet"


def parse_accounts_with_cache(
    statements: Sequence[Statement], statement_partition: tuple[str, str]
) -> pt.DataFrame[Account]:
    if not statements:
        return Account.DataFrame()

    cache_dir = Path(".data/stagings/statements").joinpath(*statement_partition)

    cache_dir.mkdir(parents=True, exist_ok=True)

    tasks: dict[ParquetTarget, list[Statement]] = collections.defaultdict(list)

    for stmt in statements:
        tasks[ParquetTarget((stmt.filling.year, stmt.filling.period))].append(stmt)

    pending_tasks: dict[ParquetTarget, list[Statement]] = {
        target: stmts
        for target, stmts in tasks.items()
        if not (
            (t_path := target.target_path(cache_dir)).is_file()
            and t_path.stat().st_size > 0
        )
    }
    if pending_tasks:
        cores = os.cpu_count() or 4
        with ProcessPoolExecutor(max_workers=cores) as executor:
            for target, stmts in tasks.items():
                target_file = target.target_path(cache_dir)
                log.info(
                    "[PARSING] %s %d %s (%d filings)",
                    statement_partition,
                    target.year,
                    target.period,
                    len(stmts),
                )
                stmts_each_core = 4
                chunksize = max(1, len(stmts) // (cores * stmts_each_core))
                batch_results = executor.map(
                    _parse_statement, stmts, chunksize=chunksize
                )
                accounts = list(itertools.chain.from_iterable(batch_results))
                if accounts:
                    account_df = Account.DataFrame(accounts)
                    account_df.write_parquet(target_file)

    accounts = pl.read_parquet(cache_dir.joinpath("*.parquet"))
    accounts = Account.validate(accounts)
    return accounts


STATEMENT_NODES: dict[str, dict[str, ParametrizedDependency]] = {
    f"{ep.slug()}_{stmt.statement_type}": {
        "statements": source(ep.slug()),
        "target_cls": value(stmt),
    }
    for ep in EntryPoint
    for stmt in STATEMENTS
}


@parameterize(**STATEMENT_NODES)
def filter_statement_type(
    statements: list[Statement], target_cls: type[Statement]
) -> list[Statement]:
    return [s for s in statements if isinstance(s, target_cls)]


ACCOUNT_NODES: dict[str, dict[str, ParametrizedDependency]] = {
    f"{ep.slug()}_{stmt.statement_type}_accounts": {
        "statements": source(f"{ep.slug()}_{stmt.statement_type}"),
        "statement_partition": value((ep.slug(), stmt.statement_type)),
    }
    for ep in EntryPoint
    for stmt in STATEMENTS
}


@parameterize(**ACCOUNT_NODES)
def staged_accounts(
    statements: list[Statement], statement_partition: tuple[str, str]
) -> pt.DataFrame[Account]:
    return parse_accounts_with_cache(statements, statement_partition)
