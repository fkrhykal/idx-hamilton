"""Equations transformation module for financial statement integrity validation.

Provides strongly-typed AccountingEquationSpecification and EquationComponentTerm definitions,
the vectorized AccountingEquationEngine, and centralized catalog registries for all IDX sectors.
"""

from __future__ import annotations

from .collective_investment_contract import (
    COLLECTIVE_INVESTMENT_CONTRACT_EQUATIONS,
)
from .cross_statement import (
    CROSS_STATEMENT_EQUATIONS,
    ENTRY_POINT_CROSS_EQUATIONS,
    get_cross_equations,
)
from .domain import (
    AccountingEquationCategory,
    AccountingEquationOperator,
    AccountingEquationSpecification,
    EquationComponentTerm,
    build_vertical_aggregation_equations,
)
from .engine import AccountingEquationEngine
from .financial_and_sharia import FINANCIAL_AND_SHARIA_EQUATIONS
from .financing import FINANCING_EQUATIONS
from .general import GENERAL_EQUATIONS
from .infrastructure import INFRASTRUCTURE_EQUATIONS
from .insurance import INSURANCE_EQUATIONS
from .property import PROPERTY_EQUATIONS
from .registry import (
    ENTRY_POINT_EQUATIONS,
    equations_dataframe,
    get_equations,
)
from .securities import SECURITIES_EQUATIONS

__all__ = [
    "COLLECTIVE_INVESTMENT_CONTRACT_EQUATIONS",
    "CROSS_STATEMENT_EQUATIONS",
    "ENTRY_POINT_CROSS_EQUATIONS",
    "ENTRY_POINT_EQUATIONS",
    "FINANCIAL_AND_SHARIA_EQUATIONS",
    "FINANCING_EQUATIONS",
    "GENERAL_EQUATIONS",
    "INFRASTRUCTURE_EQUATIONS",
    "INSURANCE_EQUATIONS",
    "PROPERTY_EQUATIONS",
    "SECURITIES_EQUATIONS",
    "AccountingEquationCategory",
    "AccountingEquationEngine",
    "AccountingEquationOperator",
    "AccountingEquationSpecification",
    "EquationComponentTerm",
    "build_vertical_aggregation_equations",
    "equations_dataframe",
    "get_cross_equations",
    "get_equations",
]
