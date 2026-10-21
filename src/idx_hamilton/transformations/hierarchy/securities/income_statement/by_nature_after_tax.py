"""Definisi hierarki akun untuk:
Entry Point : securities
Statement   : income_statement
Variant     : by_nature_after_tax
"""

from ... import AccountSpec, SignRule

BY_NATURE_AFTER_TAX_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CI", "ComprehensiveIncome", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CI.NCI", "ComprehensiveIncomeAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("CI.P", "ComprehensiveIncomeAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.B.C", "BasicEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.B.D", "BasicEarningsLossPerShareFromDiscontinuedOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.D.C", "DilutedEarningsLossPerShareFromContinuingOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("EPS.D.D", "DilutedEarningsLossPerShareFromDiscontinuedOperations", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("OCI", "OtherComprehensiveIncomeAfterTax", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.AT", "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.NR.AT.02", "OtherComprehensiveIncomeForRemeasurementOfDefinedBenefitObligationAfterTax", parent_code="OCI.NR.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.AT.03", "OtherAdjustmentsToOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI.NR.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.NR.AT.04", "OtherComprehensiveIncomeForGainsLossesOnRevaluationOfPropertyAndEquipmentAfterTax", parent_code="OCI.NR.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT", "OtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("OCI.RC.AT.02", "UnrealisedGainsLossesOnChangesInFairValueOfAvailableForSaleFinancialAssetsAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.10", "ReclassificationAdjustmentsOnAvailableForSaleFinancialAssetsAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("OCI.RC.AT.12", "OtherAdjustmentsToOtherComprehensiveIncomeThatMayBeReclassifiedToProfitOrLossAfterTax", parent_code="OCI.RC.AT", sign_rule=SignRule.RAW),
    AccountSpec("PL", "ProfitLoss", parent_code="CI", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C", "ProfitLossFromContinuingOperations", parent_code="PL", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT", "ProfitLossBeforeIncomeTax", parent_code="PL.C", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("PL.C.EBT.FIN.02", "FinalTaxExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.FIN.03", "FinanceIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.FIN.04", "FinanceCosts", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.FIN.07", "DividendsIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.FIN.08", "RealisedGainsLossesOnTradingOfMarketableSecurities", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.FIN.11", "GainsLossesOnChangesInFairValueOfMarketableSecurities", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.OF.01", "SellingExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.OF.02", "GeneralAndAdministrativeExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.EBT.OTH.01", "OtherGainsLosses", parent_code="PL.C.EBT", sign_rule=SignRule.RAW),
    AccountSpec("PL.C.EBT.OTH.02", "OtherIncome", parent_code="PL.C.EBT", sign_rule=SignRule.ADD),
    AccountSpec("PL.C.EBT.OTH.03", "OtherExpenses", parent_code="PL.C.EBT", sign_rule=SignRule.SUB),
    AccountSpec("PL.C.TAX", "TaxBenefitExpenses", parent_code="PL.C", sign_rule=SignRule.RAW),
    AccountSpec("PL.NCI", "ProfitLossAttributableToNonControllingInterests", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("PL.P", "ProfitLossAttributableToParentEntity", parent_code=None, sign_rule=SignRule.RAW),
)

__all__ = ["BY_NATURE_AFTER_TAX_HIERARCHY"]
