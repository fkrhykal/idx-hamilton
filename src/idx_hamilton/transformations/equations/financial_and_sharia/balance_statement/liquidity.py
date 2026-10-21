"""Equation definitions for:
Entry Point : financial_and_sharia
Statement   : balance_statement
Variant     : liquidity
"""

from idx_hamilton.transformations.hierarchy.financial_and_sharia.balance_statement.liquidity import (
    LIQUIDITY_HIERARCHY,
)

from ...domain import (
    AccountingEquationCategory,
    AccountingEquationOperator,
    AccountingEquationSpecification,
    EquationComponentTerm,
    build_vertical_aggregation_equations,
)

_SPECS = {spec.code: spec for spec in LIQUIDITY_HIERARCHY}

# 1. Horizontal Macro Equations
HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    AccountingEquationSpecification(
        equation_name="Macro Balance Sheet Identity: Assets == LiabilitiesAndEquity",
        statement_type="balance_statement",
        target_account=_SPECS["A"],
        component_terms=(EquationComponentTerm(account_specification=_SPECS["LE"]),),
        operator=AccountingEquationOperator.EQUALS,
        equation_category=AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY,
    ),
)

# 2. Vertical Rollup Equations down to atomic grain
ROLLUP_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    build_vertical_aggregation_equations(
        "balance_statement",
        LIQUIDITY_HIERARCHY,
    )
)

# Combined variant equations
LIQUIDITY_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    HORIZONTAL_EQUATIONS + ROLLUP_EQUATIONS
)

__all__ = [
    "HORIZONTAL_EQUATIONS",
    "LIQUIDITY_EQUATIONS",
    "ROLLUP_EQUATIONS",
]
