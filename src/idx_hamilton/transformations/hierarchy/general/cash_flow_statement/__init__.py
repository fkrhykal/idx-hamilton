"""Package hierarki untuk cash_flow_statement general.
Setiap variasi didefinisikan secara modular di filenya masing-masing.
"""

from ... import AccountSpec
from .direct_method import DIRECT_METHOD_HIERARCHY
from .indirect_method import INDIRECT_METHOD_HIERARCHY

CASH_FLOW_STATEMENT_VARIANTS: dict[str, tuple[AccountSpec, ...]] = {
    "direct_method": DIRECT_METHOD_HIERARCHY,
    "indirect_method": INDIRECT_METHOD_HIERARCHY,
}

__all__ = [
    "DIRECT_METHOD_HIERARCHY",
    "INDIRECT_METHOD_HIERARCHY",
    "CASH_FLOW_STATEMENT_VARIANTS",
]
