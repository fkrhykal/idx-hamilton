"""Package hierarki untuk income_statement general.
Setiap variasi didefinisikan secara modular di filenya masing-masing.
"""

from ... import AccountSpec
from .by_function_after_tax import BY_FUNCTION_AFTER_TAX_HIERARCHY
from .by_function_before_tax import BY_FUNCTION_BEFORE_TAX_HIERARCHY
from .by_nature_after_tax import BY_NATURE_AFTER_TAX_HIERARCHY
from .by_nature_before_tax import BY_NATURE_BEFORE_TAX_HIERARCHY

INCOME_STATEMENT_VARIANTS: dict[str, tuple[AccountSpec, ...]] = {
    "by_function_after_tax": BY_FUNCTION_AFTER_TAX_HIERARCHY,
    "by_function_before_tax": BY_FUNCTION_BEFORE_TAX_HIERARCHY,
    "by_nature_after_tax": BY_NATURE_AFTER_TAX_HIERARCHY,
    "by_nature_before_tax": BY_NATURE_BEFORE_TAX_HIERARCHY,
}

__all__ = [
    "BY_FUNCTION_AFTER_TAX_HIERARCHY",
    "BY_FUNCTION_BEFORE_TAX_HIERARCHY",
    "BY_NATURE_AFTER_TAX_HIERARCHY",
    "BY_NATURE_BEFORE_TAX_HIERARCHY",
    "INCOME_STATEMENT_VARIANTS",
]
