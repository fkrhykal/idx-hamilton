"""Definisi hierarki akun untuk:
Entry Point : collective_investment_contract
Statement   : cash_flow_statement
Variant     : direct_method
"""

from ... import AccountSpec, SignRule

DIRECT_METHOD_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CFF", "NetCashFlowsReceivedFromUsedInFinancingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFF.EQ.14", "ProceedsFromSalesOfParticipationUnit", parent_code="CFF", sign_rule=SignRule.ADD),
    AccountSpec("CFF.EQ.15", "PaymentsForAcquisitionOfParticipationUnit", parent_code="CFF", sign_rule=SignRule.SUB),
    AccountSpec("CFO", "NetCashFlowsReceivedFromUsedInOperatingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFO.BCA.OPS.IN.35", "ProceedsFromSalesOfEquityinstrumentPortfolios", parent_code="CFO", sign_rule=SignRule.ADD),
    AccountSpec("CFO.BCA.OPS.OUT.30", "PurchaseOfEquityInstrumentPortfolios", parent_code="CFO", sign_rule=SignRule.SUB),
    AccountSpec("CFO.BCA.OPS.OUT.31", "PaymentsForInvestmentExpenses", parent_code="CFO", sign_rule=SignRule.SUB),
    AccountSpec("CFO.BCA.TAX.02", "IncomeTaxesRefundedPaidFromOperatingActivities", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.BCA.TAX.04", "InterestsReceivedFromOperatingActivities", parent_code="CFO", sign_rule=SignRule.ADD),
    AccountSpec("CFO.BCA.TAX.06", "DividendsReceivedFromOperatingActivities", parent_code="CFO", sign_rule=SignRule.ADD),
    AccountSpec("CFS", "CashAndCashEquivalentsCashFlows", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("CFS.NET", "NetIncreaseDecreaseInCashAndCashEquivalents", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
)

__all__ = ["DIRECT_METHOD_HIERARCHY"]
