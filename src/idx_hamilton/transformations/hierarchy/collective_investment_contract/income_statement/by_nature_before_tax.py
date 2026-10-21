"""Definisi hierarki akun untuk:
Entry Point : collective_investment_contract
Statement   : income_statement
Variant     : by_nature_before_tax
"""

from ... import AccountSpec, SignRule

BY_NATURE_BEFORE_TAX_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CI", "ComprehensiveIncome", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL", "ProfitLoss", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.FIN.05", "InterestIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.FIN.07", "DividendsIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.FIN.17", "GainsLossesFromSecuritiesPortfolio", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.ON.38", "InvestmentManagementExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.ON.39", "CustodianExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.OTH.03", "OtherExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
)

__all__ = ["BY_NATURE_BEFORE_TAX_HIERARCHY"]
