"""Equation definitions for:
Entry Point : insurance
Statement   : income_statement
Variant     : by_nature_after_tax
"""

from idx_hamilton.transformations.hierarchy.insurance.income_statement.by_nature_after_tax import (
    BY_NATURE_AFTER_TAX_HIERARCHY,
)

from ...domain import (
    AccountingEquationCategory,
    AccountingEquationOperator,
    AccountingEquationSpecification,
    EquationComponentTerm,
    build_vertical_aggregation_equations,
)

_SPECS = {spec.code: spec for spec in BY_NATURE_AFTER_TAX_HIERARCHY}

# 1. Horizontal Macro Equations
HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    AccountingEquationSpecification(
        equation_name="Macro Net Profit Allocation: ProfitLoss == OwnersOfParent + NonControllingInterests",
        statement_type="income_statement",
        target_account=_SPECS["PL"],
        component_terms=(
            EquationComponentTerm(account_specification=_SPECS["PL.P"]),
            EquationComponentTerm(account_specification=_SPECS["PL.NCI"]),
        ),
        operator=AccountingEquationOperator.EQUALS,
        equation_category=AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY,
    ),
    AccountingEquationSpecification(
        equation_name="Macro Comprehensive Income Allocation: ComprehensiveIncome == OwnersOfParent + NonControllingInterests",
        statement_type="income_statement",
        target_account=_SPECS["CI"],
        component_terms=(
            EquationComponentTerm(account_specification=_SPECS["CI.P"]),
            EquationComponentTerm(account_specification=_SPECS["CI.NCI"]),
        ),
        operator=AccountingEquationOperator.EQUALS,
        equation_category=AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY,
    ),
)

# 2. Vertical Rollup Equations down to atomic grain
ROLLUP_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    build_vertical_aggregation_equations(
        "income_statement",
        BY_NATURE_AFTER_TAX_HIERARCHY,
    )
)

# Combined variant equations
BY_NATURE_AFTER_TAX_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    HORIZONTAL_EQUATIONS + ROLLUP_EQUATIONS
)

__all__ = [
    "BY_NATURE_AFTER_TAX_EQUATIONS",
    "HORIZONTAL_EQUATIONS",
    "ROLLUP_EQUATIONS",
]
