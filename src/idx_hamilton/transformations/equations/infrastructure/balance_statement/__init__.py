"""Equation definitions for:
Entry Point : infrastructure
Statement   : balance_statement
"""

from .current_and_non_current import CURRENT_AND_NON_CURRENT_EQUATIONS
from .liquidity import LIQUIDITY_EQUATIONS

BALANCE_STATEMENT_VARIANTS = {
    "current_and_non_current": CURRENT_AND_NON_CURRENT_EQUATIONS,
    "liquidity": LIQUIDITY_EQUATIONS,
}

__all__ = [
    "BALANCE_STATEMENT_VARIANTS",
    "CURRENT_AND_NON_CURRENT_EQUATIONS",
    "LIQUIDITY_EQUATIONS",
]
