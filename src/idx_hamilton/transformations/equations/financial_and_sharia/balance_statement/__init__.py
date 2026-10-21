"""Equation definitions for:
Entry Point : financial_and_sharia
Statement   : balance_statement
"""

from .liquidity import LIQUIDITY_EQUATIONS

BALANCE_STATEMENT_VARIANTS = {
    "liquidity": LIQUIDITY_EQUATIONS,
}

__all__ = [
    "BALANCE_STATEMENT_VARIANTS",
    "LIQUIDITY_EQUATIONS",
]
