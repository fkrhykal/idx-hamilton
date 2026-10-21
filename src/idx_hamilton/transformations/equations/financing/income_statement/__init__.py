"""Equation definitions for:
Entry Point : financing
Statement   : income_statement
"""

from .by_nature_after_tax import BY_NATURE_AFTER_TAX_EQUATIONS
from .by_nature_before_tax import BY_NATURE_BEFORE_TAX_EQUATIONS

INCOME_STATEMENT_VARIANTS = {
    "by_nature_after_tax": BY_NATURE_AFTER_TAX_EQUATIONS,
    "by_nature_before_tax": BY_NATURE_BEFORE_TAX_EQUATIONS,
}

__all__ = [
    "BY_NATURE_AFTER_TAX_EQUATIONS",
    "BY_NATURE_BEFORE_TAX_EQUATIONS",
    "INCOME_STATEMENT_VARIANTS",
]
