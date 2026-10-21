"""Registry and catalog for entry point accounting equation specifications."""

from __future__ import annotations

import polars as pl

from .collective_investment_contract import (
    COLLECTIVE_INVESTMENT_CONTRACT_EQUATIONS,
)
from .cross_statement import (
    ENTRY_POINT_CROSS_EQUATIONS,
    get_cross_equations,
)
from .domain import AccountingEquationSpecification
from .financial_and_sharia import FINANCIAL_AND_SHARIA_EQUATIONS
from .financing import FINANCING_EQUATIONS
from .general import GENERAL_EQUATIONS
from .infrastructure import INFRASTRUCTURE_EQUATIONS
from .insurance import INSURANCE_EQUATIONS
from .property import PROPERTY_EQUATIONS
from .securities import SECURITIES_EQUATIONS

ENTRY_POINT_EQUATIONS: dict[
    str, dict[str, dict[str, tuple[AccountingEquationSpecification, ...]]]
] = {
    "general": GENERAL_EQUATIONS,
    "property": PROPERTY_EQUATIONS,
    "infrastructure": INFRASTRUCTURE_EQUATIONS,
    "financial_and_sharia": FINANCIAL_AND_SHARIA_EQUATIONS,
    "financing": FINANCING_EQUATIONS,
    "insurance": INSURANCE_EQUATIONS,
    "securities": SECURITIES_EQUATIONS,
    "collective_investment_contract": COLLECTIVE_INVESTMENT_CONTRACT_EQUATIONS,
}


def get_equations(
    entry_point: str,
    statement_type: str,
    variant: str,
) -> tuple[AccountingEquationSpecification, ...]:
    """Retrieves tuple of AccountingEquationSpecification definitions for a given Entry Point, Statement, and Variant."""
    if statement_type == "cross_statement":
        return get_cross_equations(entry_point, variant)
    return ENTRY_POINT_EQUATIONS[entry_point][statement_type][variant]


def equations_dataframe() -> pl.DataFrame:
    """Flattens all registered AccountingEquationSpecifications into a master Polars DataFrame."""
    records = []
    for ep, st_dict in ENTRY_POINT_EQUATIONS.items():
        for st, vt_dict in st_dict.items():
            for vt, eqs in vt_dict.items():
                for eq in eqs:
                    records.append(
                        {
                            "entry_point": ep,
                            "statement": st,
                            "variant": vt,
                            "equation_name": eq.equation_name,
                            "equation_category": str(eq.equation_category),
                            "target_code": eq.target_account.code,
                            "target_account": eq.target_account.account,
                            "components_count": len(eq.component_terms),
                            "component_codes": ", ".join(
                                term.account_specification.code
                                for term in eq.component_terms
                            ),
                            "component_accounts": ", ".join(
                                term.account_specification.account
                                for term in eq.component_terms
                            ),
                        }
                    )
    for ep, vt_dict in ENTRY_POINT_CROSS_EQUATIONS.items():
        for vt, eqs in vt_dict.items():
            for eq in eqs:
                records.append(
                    {
                        "entry_point": ep,
                        "statement": "cross_statement",
                        "variant": vt,
                        "equation_name": eq.equation_name,
                        "equation_category": str(eq.equation_category),
                        "target_code": eq.target_account.code,
                        "target_account": eq.target_account.account,
                        "components_count": len(eq.component_terms),
                        "component_codes": ", ".join(
                            term.account_specification.code
                            for term in eq.component_terms
                        ),
                        "component_accounts": ", ".join(
                            term.account_specification.account
                            for term in eq.component_terms
                        ),
                    }
                )
    if not records:
        return pl.DataFrame(
            schema={
                "entry_point": pl.Utf8,
                "statement": pl.Utf8,
                "variant": pl.Utf8,
                "equation_name": pl.Utf8,
                "equation_category": pl.Utf8,
                "target_code": pl.Utf8,
                "target_account": pl.Utf8,
                "components_count": pl.UInt32,
                "component_codes": pl.Utf8,
                "component_accounts": pl.Utf8,
            }
        )
    return pl.DataFrame(records)
