"""Equation definitions for:
Entry Point : infrastructure
Statement   : cash_flow_statement
Variant     : indirect_method
"""

from idx_hamilton.transformations.hierarchy.infrastructure.cash_flow_statement.indirect_method import (
    INDIRECT_METHOD_HIERARCHY,
)

from ...domain import (
    AccountingEquationCategory,
    AccountingEquationOperator,
    AccountingEquationSpecification,
    EquationComponentTerm,
    build_vertical_aggregation_equations,
)

_SPECS = {spec.code: spec for spec in INDIRECT_METHOD_HIERARCHY}

# 1. Horizontal Macro Equations
HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    AccountingEquationSpecification(
        equation_name="Macro Net Cash Flow Identity: CFS.NET == CFO + CFI + CFF",
        statement_type="cash_flow_statement",
        target_account=_SPECS["CFS.NET"],
        component_terms=(
            EquationComponentTerm(account_specification=_SPECS["CFO"]),
            EquationComponentTerm(account_specification=_SPECS["CFI"]),
            EquationComponentTerm(account_specification=_SPECS["CFF"]),
        ),
        operator=AccountingEquationOperator.EQUALS,
        equation_category=AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY,
    ),
)

# 2. Vertical Rollup Equations down to atomic grain
ROLLUP_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    build_vertical_aggregation_equations(
        "cash_flow_statement",
        INDIRECT_METHOD_HIERARCHY,
        excluded_taxonomic_codes=("CFS.NET",),
    )
)

# Combined variant equations
INDIRECT_METHOD_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    HORIZONTAL_EQUATIONS + ROLLUP_EQUATIONS
)

__all__ = [
    "HORIZONTAL_EQUATIONS",
    "INDIRECT_METHOD_EQUATIONS",
    "ROLLUP_EQUATIONS",
]
