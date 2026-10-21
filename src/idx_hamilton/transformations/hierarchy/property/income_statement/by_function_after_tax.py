"""Definisi hierarki akun untuk:
Entry Point : property
Statement   : income_statement
Variant     : by_function_after_tax
Berdasarkan  : IDX-rt_role-2020-01-01_2311000 (34 Calculation Arcs)
"""

from ... import AccountSpec, SignRule, AccountRole, AccountOrigin

BY_FUNCTION_AFTER_TAX_HIERARCHY: tuple[AccountSpec, ...] = (
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
    AccountSpec("PL.C", "ProfitLossFromContinuingOperations", parent_code="PL", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.D", "ProfitLossFromDiscontinuedOperations", parent_code="PL", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.TAX", "TaxBenefitExpenses", parent_code="PL.C", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.GP", "GrossProfit", parent_code="PL.C.EBT", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.GP.01", "SalesAndRevenue", parent_code="PL.C.EBT.GP", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.GP.02", "CostOfSalesAndRevenue", parent_code="PL.C.EBT.GP", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.01", "SellingExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.02", "GeneralAndAdministrativeExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.03", "FinanceIncome", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.04", "InterestAndFinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.05", "GainsLossesOnChangesInForeignExchangeRates", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.06", "ShareOfProfitLossOfAssociatesAccountedForUsingEquityMethod", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.07", "ShareOfProfitLossOfJointVenturesAccountedForUsingEquityMethod", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.08", "OtherIncome", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.09", "OtherExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.10", "OtherGainsLosses", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.11", "FinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI", "OtherComprehensiveIncomeAfterTax", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.AT", "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.RC.AT", "OtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.AT.01", "OtherComprehensiveIncomeForGainsLossesOnRevaluationOfPropertyAndEquipmentAfterTax", parent_code="OCI.NR.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.AT.02", "OtherComprehensiveIncomeForRemeasurementOfDefinedBenefitObligationAfterTax", parent_code="OCI.NR.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.AT.03", "OtherAdjustmentsToOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI.NR.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.01", "GainsLossesOnExchangeDifferencesOnTranslationAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.02", "ReclassificationAdjustmentsOnExchangeDifferencesOnTranslationAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.AT.03", "GainsLossesOnCashFlowHedgesAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.04", "ReclassificationAdjustmentsOnCashFlowHedgesAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.AT.05", "CarryingAmountOfNonFinancialAssetLiabilityWhoseAcquisitionOrIncurrenceWasHedgedOnHighlyProbableForecastTransactionAdjustedFromEquityAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.06", "GainsLossesOnHedgesOfNetInvestmentsInForeignOperationsAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.07", "ReclassificationAdjustmentsOnHedgesOfNetInvestmentsInForeignOperationsAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.AT.08", "ShareOfOtherComprehensiveIncomeOfAssociatesAccountedForUsingEquityMethodAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.09", "ShareOfOtherComprehensiveIncomeOfJointVenturesAccountedForUsingEquityMethodAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.10", "OtherAdjustmentsToOtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.AFS", "UnrealisedGainsLossesOnChangesInFairValueOfAvailableForSaleFinancialAssetsAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.AFSR", "ReclassificationAdjustmentsOnAvailableForSaleFinancialAssetsAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.SUB_RAW),
)
