"""Definisi hierarki akun untuk:
Entry Point : financing
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
    AccountSpec("OCI.BT", "OtherComprehensiveIncomeBeforeTax", parent_code="OCI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.BT", "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.BT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.BT.01", "OtherComprehensiveIncomeForRemeasurementOfDefinedBenefitObligationBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.BT.02", "OtherAdjustmentsToOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT", "OtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.BT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.RC.BT.01", "UnrealisedGainsLossesOnChangesInFairValueThroughOtherComprehensiveIncomeFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.04", "UnrealisedGainsLossesOnChangesInFairValueOfAvailableForSaleFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.08", "OtherAdjustmentsToOtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.09", "ReclassificationAdjustmentsOnExchangeDifferencesOnTranslationBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.11", "GainsLossesOnCashFlowHedgesBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.13", "GainsLossesOnExchangeDifferencesOnTranslationBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.TAX", "TaxOnOtherComprehensiveIncome", parent_code="OCI", sign_rule=SignRule.RAW),
    AccountSpec("PL", "ProfitLoss", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C", "ProfitLossFromContinuingOperations", parent_code="PL", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.EQ.02", "ShareOfProfitLossOfAssociatesAccountedForUsingEquityMethod", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.FIN.01", "InterestAndFinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.FIN.04", "FinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.FIN.06", "GainsLossesOnChangesInForeignExchangeRates", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.OF.01", "SellingExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.OF.02", "GeneralAndAdministrativeExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.OTH.02", "OtherIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.OTH.03", "OtherExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.TAX", "TaxBenefitExpenses", parent_code="PL.C", sign_rule=SignRule.RAW),
    AccountSpec("PL.NCI", "ProfitLossAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("PL.P", "ProfitLossAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW),
)

__all__ = ["BY_FUNCTION_BEFORE_TAX_HIERARCHY"]
