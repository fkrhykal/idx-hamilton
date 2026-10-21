"""Definisi hierarki akun untuk:
Entry Point : insurance
Statement   : income_statement
Variant     : by_function_before_tax
"""

from ... import AccountSpec, SignRule

BY_FUNCTION_BEFORE_TAX_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CI", "ComprehensiveIncome", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CI.NCI", "ComprehensiveIncomeAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("CI.P", "ComprehensiveIncomeAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.B.C", "BasicEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.D.C", "DilutedEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("OCI", "OtherComprehensiveIncomeAfterTax", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL", "ProfitLoss", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C", "ProfitLossFromContinuingOperations", parent_code="PL", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.FIN.01", "InterestAndFinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.OF.02", "GeneralAndAdministrativeExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.TAX", "TaxBenefitExpenses", parent_code="PL.C", sign_rule=SignRule.RAW),
    AccountSpec("PL.D", "ProfitLossFromDiscontinuedOperations", parent_code="PL", sign_rule=SignRule.RAW),
    AccountSpec("PL.NCI", "ProfitLossAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("PL.P", "ProfitLossAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW),
)

__all__ = ["BY_FUNCTION_BEFORE_TAX_HIERARCHY"]
