"""Definisi hierarki akun modular untuk:
Entry Point : general
Statement   : balance_statement
"""

from .current_and_non_current import CURRENT_AND_NON_CURRENT_HIERARCHY
from .liquidity import LIQUIDITY_HIERARCHY

BALANCE_STATEMENT_VARIANTS = {
    "current_and_non_current": CURRENT_AND_NON_CURRENT_HIERARCHY,
    "liquidity": LIQUIDITY_HIERARCHY,
}

__all__ = [
    "BALANCE_STATEMENT_VARIANTS",
    "CURRENT_AND_NON_CURRENT_HIERARCHY",
    "LIQUIDITY_HIERARCHY",
]

