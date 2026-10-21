"""Definisi hierarki akun untuk:
Entry Point : securities
Statement   : cash_flow_statement
Variant     : indirect_method
"""

from ... import AccountSpec, SignRule

INDIRECT_METHOD_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CFF", "NetCashFlowsReceivedFromUsedInFinancingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFF.DEBT.19", "ProceedsFromNon-BankFinancialInstitutionLoan", parent_code="CFF", sign_rule=SignRule.ADD),
    AccountSpec("CFF.DIV.01", "DividendsPaidFromFinancingActivities", parent_code="CFF", sign_rule=SignRule.SUB),
    AccountSpec("CFI", "NetCashFlowsReceivedFromUsedInInvestingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFO", "NetCashFlowsReceivedFromUsedInOperatingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFS", "CashAndCashEquivalentsCashFlows", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFS.NET", "NetIncreaseDecreaseInCashAndCashEquivalents", parent_code="CFS", sign_rule=SignRule.RAW, is_total=True),
)

__all__ = ["INDIRECT_METHOD_HIERARCHY"]
