"""Definisi hierarki akun untuk:
Entry Point : collective_investment_contract
Statement   : cash_flow_statement
Variant     : indirect_method
"""

from ... import AccountSpec, SignRule

INDIRECT_METHOD_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CFF", "NetCashFlowsReceivedFromUsedInFinancingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFO", "NetCashFlowsReceivedFromUsedInOperatingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFS", "CashAndCashEquivalentsCashFlows", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFS.NET", "NetIncreaseDecreaseInCashAndCashEquivalents", parent_code="CFS", sign_rule=SignRule.RAW, is_total=True),
)

__all__ = ["INDIRECT_METHOD_HIERARCHY"]
