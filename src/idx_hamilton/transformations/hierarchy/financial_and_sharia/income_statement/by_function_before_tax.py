"""Definisi hierarki akun untuk:
Entry Point : financial_and_sharia
Statement   : income_statement
Variant     : by_function_before_tax
"""

from ... import AccountSpec, SignRule

BY_FUNCTION_BEFORE_TAX_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CI", "ComprehensiveIncome", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CI.NCI", "ComprehensiveIncomeAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("CI.P", "ComprehensiveIncomeAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.B.C", "BasicEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.B.D", "BasicEarningsLossPerShareFromDiscontinuedOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.D.C", "DilutedEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.D.D", "DilutedEarningsLossPerShareFromDiscontinuedOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("OCI", "OtherComprehensiveIncomeAfterTax", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.BT", "OtherComprehensiveIncomeBeforeTax", parent_code="OCI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.BT", "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.BT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.BT.01", "OtherComprehensiveIncomeForRemeasurementOfDefinedBenefitObligationBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.BT.02", "OtherAdjustmentsToOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.BT.04", "OtherComprehensiveIncomeForGainsLossesOnRevaluationOfPropertyAndEquipmentBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT", "OtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.BT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.RC.BT.01", "UnrealisedGainsLossesOnChangesInFairValueThroughOtherComprehensiveIncomeFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.03", "ReclassificationAdjustmentsOnFairValueThroughOtherComprehensiveIncomeFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.04", "UnrealisedGainsLossesOnChangesInFairValueOfAvailableForSaleFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.07", "ShareOfOtherComprehensiveIncomeOfAssociatesAccountedForUsingEquityMethodBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.08", "OtherAdjustmentsToOtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.10", "ReclassificationAdjustmentsOnAvailableForSaleFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.11", "GainsLossesOnCashFlowHedgesBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.13", "GainsLossesOnExchangeDifferencesOnTranslationBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.TAX", "TaxOnOtherComprehensiveIncome", parent_code="OCI", sign_rule=SignRule.RAW),
    AccountSpec("PL", "ProfitLoss", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C", "ProfitLossFromContinuingOperations", parent_code="PL", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.EQ.02", "ShareOfProfitLossOfAssociatesAccountedForUsingEquityMethod", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.FIN.05", "InterestIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.FIN.06", "GainsLossesOnChangesInForeignExchangeRates", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.FIN.07", "DividendsIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.FIN.08", "RealisedGainsLossesOnTradingOfMarketableSecurities", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.FIN.11", "GainsLossesOnChangesInFairValueOfMarketableSecurities", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.OF.01", "SellingExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.OF.02", "GeneralAndAdministrativeExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.TAX", "TaxBenefitExpenses", parent_code="PL.C", sign_rule=SignRule.RAW),
    AccountSpec("PL.D", "ProfitLossFromDiscontinuedOperations", parent_code="PL", sign_rule=SignRule.RAW),
    AccountSpec("PL.NCI", "ProfitLossAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("PL.P", "ProfitLossAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW),
)

__all__ = ["BY_FUNCTION_BEFORE_TAX_HIERARCHY"]
