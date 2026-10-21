"""Equation definitions for:
Entry Point : securities
Statement   : income_statement
"""

from .by_function_after_tax import BY_FUNCTION_AFTER_TAX_EQUATIONS
from .by_function_before_tax import BY_FUNCTION_BEFORE_TAX_EQUATIONS

INCOME_STATEMENT_VARIANTS = {
    "by_function_after_tax": BY_FUNCTION_AFTER_TAX_EQUATIONS,
    "by_function_before_tax": BY_FUNCTION_BEFORE_TAX_EQUATIONS,
}

__all__ = [
    "BY_FUNCTION_AFTER_TAX_EQUATIONS",
    "BY_FUNCTION_BEFORE_TAX_EQUATIONS",
    "INCOME_STATEMENT_VARIANTS",
]
