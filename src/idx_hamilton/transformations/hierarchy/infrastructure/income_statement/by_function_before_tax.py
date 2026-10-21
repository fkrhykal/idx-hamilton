"""Definisi hierarki akun untuk:
Entry Point : infrastructure
Statement   : income_statement
Variant     : by_function_before_tax
Berdasarkan  : IDX-rt_role-2020-01-01_3321000 (38 Calculation Arcs)
"""

from ... import AccountSpec, SignRule, AccountRole, AccountOrigin

BY_FUNCTION_BEFORE_TAX_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CI.NCI", "ComprehensiveIncomeAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.ALLOCATION, origin=AccountOrigin.REPORTED, target_code="CI"),
    AccountSpec("CI.P", "ComprehensiveIncomeAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.ALLOCATION, origin=AccountOrigin.REPORTED, target_code="CI"),
    AccountSpec("EPS.B.C", "BasicEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.RATIO, origin=AccountOrigin.REPORTED),
    AccountSpec("EPS.B.D", "BasicEarningsLossPerShareFromDiscontinuedOperations", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.RATIO, origin=AccountOrigin.REPORTED),
    AccountSpec("EPS.D.C", "DilutedEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.RATIO, origin=AccountOrigin.REPORTED),
    AccountSpec("EPS.D.D", "DilutedEarningsLossPerShareFromDiscontinuedOperations", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.RATIO, origin=AccountOrigin.REPORTED),
    AccountSpec("PL.NCI", "ProfitLossAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.ALLOCATION, origin=AccountOrigin.REPORTED, target_code="PL"),
    AccountSpec("PL.P", "ProfitLossAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.ALLOCATION, origin=AccountOrigin.REPORTED, target_code="PL"),
    AccountSpec("CI", "ComprehensiveIncome", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL", "ProfitLoss", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.01", "ProfitLossFromDiscontinuedOperations", parent_code="PL", sign_rule=SignRule.RAW),
    AccountSpec("PL.C", "ProfitLossFromContinuingOperations", parent_code="PL", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.GP", "GrossProfit", parent_code="PL.C.EBT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.GP.01", "SalesAndRevenue", parent_code="PL.C.EBT.GP", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.GP.02", "CostOfSalesAndRevenue", parent_code="PL.C.EBT.GP", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.01", "SellingExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.02", "InterconnectionExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.03", "GeneralAndAdministrativeExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.04", "FinanceIncome", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.05", "InterestAndFinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.06", "GainsLossesOnChangesInForeignExchangeRates", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.07", "ShareOfProfitLossOfAssociatesAccountedForUsingEquityMethod", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.08", "ShareOfProfitLossOfJointVenturesAccountedForUsingEquityMethod", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.09", "GainsLossesOnDerivativeFinancialInstruments", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.10", "OtherIncome", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.11", "OtherExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.12", "OtherGainsLosses", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.01", "TaxBenefitExpenses", parent_code="PL.C", sign_rule=SignRule.RAW),
    AccountSpec("OCI", "OtherComprehensiveIncomeAfterTax", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.BT", "OtherComprehensiveIncomeBeforeTax", parent_code="OCI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.BT", "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.BT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.BT.01", "OtherComprehensiveIncomeForGainsLossesOnRevaluationOfPropertyAndEquipmentBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.BT.02", "OtherComprehensiveIncomeForRemeasurementOfDefinedBenefitObligationBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.BT.03", "OtherAdjustmentsToOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.NR.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT", "OtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.BT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.RC.BT.01", "GainsLossesOnExchangeDifferencesOnTranslationBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.02", "ReclassificationAdjustmentsOnExchangeDifferencesOnTranslationBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.BT.03", "GainsLossesOnCashFlowHedgesBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.04", "ReclassificationAdjustmentsOnCashFlowHedgesBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.BT.05", "CarryingAmountOfNonFinancialAssetLiabilityWhoseAcquisitionOrIncurrenceWasHedgedOnHighlyProbableForecastTransactionAdjustedFromEquityBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.06", "GainsLossesOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.07", "ReclassificationAdjustmentsOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.BT.08", "ShareOfOtherComprehensiveIncomeOfAssociatesAccountedForUsingEquityMethodBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.09", "ShareOfOtherComprehensiveIncomeOfJointVenturesAccountedForUsingEquityMethodBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.10", "OtherAdjustmentsToOtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.01", "TaxOnOtherComprehensiveIncome", parent_code="OCI", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.FC", "FinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.BT.AFS_UNR", "UnrealisedGainsLossesOnChangesInFairValueOfAvailableForSaleFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.AFS_REC", "ReclassificationAdjustmentsOnAvailableForSaleFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.SUB_RAW),
)

__all__ = ["BY_FUNCTION_BEFORE_TAX_HIERARCHY"]
