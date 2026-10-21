import logging
from enum import StrEnum
from pathlib import Path

import patito as pt
import polars as pl
from hamilton.function_modifiers import parameterize, source, value
from hamilton.function_modifiers.dependencies import ParametrizedDependency

from idx_hamilton.models import Model
from idx_hamilton.sources import Period
from idx_hamilton.stagings.statement import STATEMENTS, Account, EntryPoint, Variant

log = logging.getLogger(__name__)


class Provenace(StrEnum):
    ACTUAL = "ACTUAL"
    COMPARATIVE_BACKFILL = "COMPARATIVE_BACKFILL"
    MISSING = "MISSING"


class AccountFact(Model):
    emiten_code: str
    year: int
    period: Period
    statement: str
    variant: Variant
    account: str
    value: float
    provenance: Provenace

    class c:
        emiten_code: pl.Expr
        year: pl.Expr
        period: pl.Expr
        statement: pl.Expr
        variant: pl.Expr
        account: pl.Expr
        value: pl.Expr
        provenance: pl.Expr

    class n:
        emiten_code: str
        year: str
        period: str
        statement: str
        variant: str
        account: str
        value: str
        provenance: str


BACKFILLED_ACCOUNT_NODES: dict[str, dict[str, ParametrizedDependency]] = {
    f"{ep.slug()}_{stmt.statement_type}_facts": {
        "staged_accounts": source(f"{ep.slug()}_{stmt.statement_type}_accounts"),
        "statement_partition": value((ep.slug(), stmt.statement_type)),
    }
    for ep in EntryPoint
    for stmt in STATEMENTS
}


@parameterize(**BACKFILLED_ACCOUNT_NODES)
def backfilled_accounts(
    staged_accounts: pt.DataFrame[Account], statement_partition: tuple[str, str]
) -> pt.DataFrame[AccountFact]:
    if staged_accounts.is_empty():
        return AccountFact.DataFrame()

    cache_dir = Path(".data/transformations/backfillings").joinpath(
        *statement_partition
    )

    cache_dir.mkdir(parents=True, exist_ok=True)

    target_file = cache_dir / "facts.parquet"

    if target_file.exists():
        return AccountFact.validate(pl.read_parquet(target_file))

    mapped = staged_accounts.with_columns(
        effective_year=(
            pl.when(Account.c.context.str.starts_with("Current"))
            .then(Account.c.year)
            .otherwise(Account.c.year - 1)
        ),
        effective_period=(
            pl.when(Account.c.context.str.contains("Duration|Instant"))
            .then(Account.c.period)
            .otherwise(pl.lit("Audit"))
        ),
        provenance=(
            pl.when(Account.c.context.str.starts_with("Current"))
            .then(pl.lit(Provenace.ACTUAL))
            .otherwise(pl.lit(Provenace.COMPARATIVE_BACKFILL))
        ),
        priority=(
            pl.when(Account.c.context.str.starts_with("Current"))
            .then(pl.lit(1))
            .otherwise(pl.lit(2))
        ),
    ).filter(pl.col("effective_year").is_not_null())
    reconciled = (
        mapped.sort("priority", maintain_order=True)
        .unique(
            subset=[
                "emiten_code",
                "effective_year",
                "effective_period",
                "statement",
                "account",
            ],
            keep="first",
        )
        .select(
            emiten_code="emiten_code",
            year="effective_year",
            period="effective_period",
            statement="statement",
            variant="variant",
            account="account",
            value="value",
            provenance="provenance",
        )
    )

    account_facts = AccountFact.validate(reconciled)
    account_facts.write_parquet(target_file)
    return account_facts
