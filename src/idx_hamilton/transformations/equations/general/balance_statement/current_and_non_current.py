"""Equation definitions for:
Entry Point : general
Statement   : balance_statement
Variant     : current_and_non_current
"""

from idx_hamilton.transformations.hierarchy.general.balance_statement.current_and_non_current import (
    CURRENT_AND_NON_CURRENT_HIERARCHY,
)

from ...domain import (
    AccountingEquationCategory,
    AccountingEquationOperator,
    AccountingEquationSpecification,
    EquationComponentTerm,
    build_vertical_aggregation_equations,
)

_SPECS = {spec.code: spec for spec in CURRENT_AND_NON_CURRENT_HIERARCHY}

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
        CURRENT_AND_NON_CURRENT_HIERARCHY,
    )
)

# Combined variant equations
CURRENT_AND_NON_CURRENT_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    HORIZONTAL_EQUATIONS + ROLLUP_EQUATIONS
)

__all__ = [
    "CURRENT_AND_NON_CURRENT_EQUATIONS",
    "HORIZONTAL_EQUATIONS",
    "ROLLUP_EQUATIONS",
]
