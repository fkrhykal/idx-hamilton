"""Equation definitions for:
Entry Point : general
Statement   : cash_flow_statement
"""

from .direct_method import DIRECT_METHOD_EQUATIONS
from .indirect_method import INDIRECT_METHOD_EQUATIONS

CASH_FLOW_STATEMENT_VARIANTS = {
    "direct_method": DIRECT_METHOD_EQUATIONS,
    "indirect_method": INDIRECT_METHOD_EQUATIONS,
}

__all__ = [
    "CASH_FLOW_STATEMENT_VARIANTS",
    "DIRECT_METHOD_EQUATIONS",
    "INDIRECT_METHOD_EQUATIONS",
]
