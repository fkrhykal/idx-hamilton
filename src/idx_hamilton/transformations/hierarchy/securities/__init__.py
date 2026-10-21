"""Entry Point: securities"""

from .balance_statement import BALANCE_STATEMENT_VARIANTS
from .income_statement import INCOME_STATEMENT_VARIANTS
from .cash_flow_statement import CASH_FLOW_STATEMENT_VARIANTS

SECURITIES_HIERARCHIES = {
    "balance_statement": BALANCE_STATEMENT_VARIANTS,
    "income_statement": INCOME_STATEMENT_VARIANTS,
    "cash_flow_statement": CASH_FLOW_STATEMENT_VARIANTS,
}

__all__ = [
    "SECURITIES_HIERARCHIES",
    "BALANCE_STATEMENT_VARIANTS",
    "INCOME_STATEMENT_VARIANTS",
    "CASH_FLOW_STATEMENT_VARIANTS",
]
