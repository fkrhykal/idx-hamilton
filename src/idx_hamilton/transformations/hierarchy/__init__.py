from dataclasses import dataclass
from enum import StrEnum
import polars as pl


class SignRule(StrEnum):
    ADD = "+abs"
    SUB = "-abs"
    RAW = "raw"
    SUB_RAW = "-raw"


class AccountRole(StrEnum):
    SUMMATIVE = "summative"     # Akun aditif kalkulasi pohon utama
    ALLOCATION = "allocation"   # Alokasi kepemilikan laba (target_code)
    RATIO = "ratio"             # Rasio per lembar saham (EPS)
    BRIDGE = "bridge"           # Jembatan rekonsiliasi kas (CFS)
    MEMO = "memo"               # Catatan kaki / teks informatif


class AccountOrigin(StrEnum):
    TAXONOMY = "taxonomy"       # Terdefinisi di Calculation Linkbase (*CAL*.xml)
    REPORTED = "reported"       # Hadir dari pelaporan riil emiten di Parquet (non-CAL)


class AccountNature(StrEnum):
    UNSPECIFIED = "unspecified"
    # Cash Flow & Operational Nature
    CORE_INFLOW = "core_inflow"             # Pos penerimaan inti operasional rutin (pelanggan, komisi, dsb)
    CORE_OUTFLOW = "core_outflow"           # Pos pengeluaran inti operasional esensial (gaji, beban umum & administrasi, pemasok, pajak badan)
    INCIDENTAL_INFLOW = "incidental_inflow" # Pos penerimaan kas non-rutin/insidental (bunga, dividen, pelepasan aset)
    INCIDENTAL_OUTFLOW = "incidental_outflow" # Pos pengeluaran kas non-rutin/diskresioner (bunga, denda)
    BILATERAL = "bilateral"                 # Pos dua arah / kliring / fluktuatif modal kerja


@dataclass(frozen=True)
class AccountSpec:
    code: str
    account: str
    parent_code: str | None
    sign_rule: SignRule
    is_total: bool = False
    role: AccountRole = AccountRole.SUMMATIVE
    origin: AccountOrigin = AccountOrigin.TAXONOMY
    target_code: str | None = None
    nature: AccountNature = AccountNature.UNSPECIFIED


# Import modular hierarchies per Entry Point
from .collective_investment_contract import COLLECTIVE_INVESTMENT_CONTRACT_HIERARCHIES  # noqa: E402
from .financial_and_sharia import FINANCIAL_AND_SHARIA_HIERARCHIES  # noqa: E402
from .financing import FINANCING_HIERARCHIES  # noqa: E402
from .general import GENERAL_HIERARCHIES  # noqa: E402
from .infrastructure import INFRASTRUCTURE_HIERARCHIES  # noqa: E402
from .insurance import INSURANCE_HIERARCHIES  # noqa: E402
from .property import PROPERTY_HIERARCHIES  # noqa: E402
from .securities import SECURITIES_HIERARCHIES  # noqa: E402

ENTRY_POINT_HIERARCHIES: dict[str, dict[str, dict[str, tuple[AccountSpec, ...]]]] = {
    "general": GENERAL_HIERARCHIES,
    "property": PROPERTY_HIERARCHIES,
    "infrastructure": INFRASTRUCTURE_HIERARCHIES,
    "financial_and_sharia": FINANCIAL_AND_SHARIA_HIERARCHIES,
    "financing": FINANCING_HIERARCHIES,
    "insurance": INSURANCE_HIERARCHIES,
    "securities": SECURITIES_HIERARCHIES,
    "collective_investment_contract": COLLECTIVE_INVESTMENT_CONTRACT_HIERARCHIES,
 }


def get_hierarchy(
    entry_point: str,
    statement_type: str,
    variant: str,
) -> tuple[AccountSpec, ...]:
    """Mengambil tuple definisi AccountSpec untuk kombinasi Entry Point, Statement, dan Variant tertentu."""
    return ENTRY_POINT_HIERARCHIES[entry_point][statement_type][variant]


def hierarchy_dataframe(
    entry_point: str | None = None,
    statement_type: str | None = None,
    variant: str | None = None,
) -> pl.DataFrame:
    """Mengembalikan DataFrame hierarki akun lengkap dengan kolom:
    ['entry_point', 'statement', 'variant', 'code', 'account', 'parent_code', 'sign_rule', 'is_total']
    """
    rows: list[dict[str, object]] = []

    eps_to_iter = (
        [(entry_point, ENTRY_POINT_HIERARCHIES[entry_point])]
        if entry_point
        else list(ENTRY_POINT_HIERARCHIES.items())
    )

    for ep_name, stmt_map in eps_to_iter:
        stmts_to_iter = (
            [(statement_type, stmt_map[statement_type])]
            if statement_type
            else list(stmt_map.items())
        )

        for stmt_name, var_map in stmts_to_iter:
            vars_to_iter = (
                [(variant, var_map[variant])]
                if variant
                else list(var_map.items())
            )

            for var_name, specs in vars_to_iter:
                for spec in specs:
                    rows.append(
                        {
                            "entry_point": ep_name,
                            "statement": stmt_name,
                            "variant": var_name,
                            "code": spec.code,
                            "account": spec.account,
                            "parent_code": spec.parent_code,
                            "sign_rule": str(spec.sign_rule),
                            "is_total": spec.is_total,
                            "role": spec.role.value,
                            "origin": spec.origin.value,
                            "target_code": spec.target_code,
                            "nature": spec.nature.value,
                        }
                    )
    schema = {
        "entry_point": pl.String,
        "statement": pl.String,
        "variant": pl.String,
        "code": pl.String,
        "account": pl.String,
        "parent_code": pl.String,
        "sign_rule": pl.String,
        "is_total": pl.Boolean,
        "role": pl.String,
        "origin": pl.String,
        "target_code": pl.String,
        "nature": pl.String,
    }
    return pl.DataFrame(rows, schema=schema)


__all__ = [
    "AccountSpec",
    "SignRule",
    "AccountRole",
    "AccountOrigin",
    "AccountNature",
    "ENTRY_POINT_HIERARCHIES",
    "get_hierarchy",
    "hierarchy_dataframe",
    "GENERAL_HIERARCHIES",
    "PROPERTY_HIERARCHIES",
    "INFRASTRUCTURE_HIERARCHIES",
    "FINANCIAL_AND_SHARIA_HIERARCHIES",
    "FINANCING_HIERARCHIES",
    "INSURANCE_HIERARCHIES",
    "SECURITIES_HIERARCHIES",
    "COLLECTIVE_INVESTMENT_CONTRACT_HIERARCHIES",
]
