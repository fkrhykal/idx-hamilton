"""Definisi hierarki akun untuk:
Entry Point : collective_investment_contract
Statement   : balance_statement
Variant     : current_and_non_current
"""

from ... import AccountSpec, SignRule

CURRENT_AND_NON_CURRENT_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("A", "Assets", parent_code=None, sign_rule=SignRule.ADD, is_total=True),
    AccountSpec("A.C.01", "CashAndCashEquivalents", parent_code="A.C", sign_rule=SignRule.ADD),
    AccountSpec("L", "Liabilities", parent_code="LE", sign_rule=SignRule.ADD, is_total=True),
    AccountSpec("L.C.25", "TaxesPayable", parent_code="L.C", sign_rule=SignRule.ADD),
)

__all__ = ["CURRENT_AND_NON_CURRENT_HIERARCHY"]
