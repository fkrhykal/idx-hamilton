"""Definisi hierarki akun untuk:
Entry Point : insurance
Statement   : income_statement
Variant     : by_nature_before_tax
Berdasarkan  : IDX-rt_role-2020-01-01_6322000 (51 Calculation Arcs)
"""

from ... import AccountSpec, SignRule

BY_NATURE_BEFORE_TAX_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CI", "ComprehensiveIncome", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL", "ProfitLoss", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.01", "ProfitLossFromDiscontinuedOperations", parent_code="PL", sign_rule=SignRule.RAW),
    AccountSpec("PL.C", "ProfitLossFromContinuingOperations", parent_code="PL", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.01", "RevenueFromInsurancePremiums", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.02", "ReinsurancePremiums", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.03", "RetrocessionPremiums", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.04", "DecreaseIncreaseInUnearnedPremiums", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.05", "DecreaseIncreaseInPremiumIncomeCededToReinsurancer", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.06", "CommissionIncome", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.07", "NetInvestmentIncome", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.08", "UjrahReceived", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.09", "GainsLossesOnSaleOfSecuritiesAndMutualFundsAtFairValueThroughProfitOrLoss", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.10", "GainsLossesOnSaleOfSharesOfStock", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.11", "UnrealisedFairValueGainsLossesOnSecuritiesAndMutualFundsAtFairValueThroughProfitOrLoss", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.12", "OtherUnderwritingIncome", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.13", "ClaimExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.14", "ReinsuranceClaims", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.15", "RetrocessionClaims", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.16", "IncreaseDecreaseInEstimatedClaimsLiability", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.17", "IncreaseDecreaseInLiabilityForFuturePolicyBenefit", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.18", "IncreaseDecreaseInProvisionForLossesArisingFromLiabilityAdequacyTest", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.19", "IncreaseDecreaseInInsuranceLiabilitiesCededToReinsurers", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.20", "IncreaseDecreaseInLiabilitiesToPolicyholderInUnitLinkedContracts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.21", "CommissionExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.22", "OtherUnderwritingExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.23", "UjrahPaid", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.24", "AcquisitionCostsOfInsuranceContracts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.25", "GeneralAndAdministrativeExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("PL.C.EBT.26", "InterestAndFinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB_RAW),
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
    AccountSpec("OCI.RC.BT.03", "UnrealisedGainsLossesOnChangesInFairValueThroughOtherComprehensiveIncomeFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.04", "ReclassificationAdjustmentsOnFairValueThroughOtherComprehensiveIncomeFinancialAssetsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.BT.05", "GainsLossesOnCashFlowHedgesBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.06", "ReclassificationAdjustmentsOnCashFlowHedgesBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.BT.07", "CarryingAmountOfNonFinancialAssetLiabilityWhoseAcquisitionOrIncurrenceWasHedgedOnHighlyProbableForecastTransactionAdjustedFromEquityBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.08", "GainsLossesOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.09", "ReclassificationAdjustmentsOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.SUB_RAW),
    AccountSpec("OCI.RC.BT.10", "ShareOfOtherComprehensiveIncomeOfAssociatesAccountedForUsingEquityMethodBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.11", "ShareOfOtherComprehensiveIncomeOfJointVenturesAccountedForUsingEquityMethodBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.BT.12", "OtherAdjustmentsToOtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossBeforeTax", parent_code="OCI.RC.BT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.01", "TaxOnOtherComprehensiveIncome", parent_code="OCI", sign_rule=SignRule.SUB_RAW),
)

__all__ = ["BY_NATURE_BEFORE_TAX_HIERARCHY"]
