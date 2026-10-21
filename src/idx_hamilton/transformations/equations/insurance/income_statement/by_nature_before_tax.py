"""Equation definitions for:
Entry Point : insurance
Statement   : income_statement
Variant     : by_nature_before_tax
"""

from idx_hamilton.transformations.hierarchy.insurance.income_statement.by_nature_before_tax import (
    BY_NATURE_BEFORE_TAX_HIERARCHY,
)

from ...domain import (
    AccountingEquationSpecification,
    build_vertical_aggregation_equations,
)

_SPECS = {spec.code: spec for spec in BY_NATURE_BEFORE_TAX_HIERARCHY}

# 1. Horizontal Macro Equations
HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = ()

# 2. Vertical Rollup Equations down to atomic grain
ROLLUP_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    build_vertical_aggregation_equations(
        "income_statement",
        BY_NATURE_BEFORE_TAX_HIERARCHY,
    )
)

# Combined variant equations
BY_NATURE_BEFORE_TAX_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    HORIZONTAL_EQUATIONS + ROLLUP_EQUATIONS
)

__all__ = [
    "BY_NATURE_BEFORE_TAX_EQUATIONS",
    "HORIZONTAL_EQUATIONS",
    "ROLLUP_EQUATIONS",
]
