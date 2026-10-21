"""Definisi hierarki akun untuk:
Entry Point : insurance
Statement   : cash_flow_statement
Variant     : direct_method
Berdasarkan  : IDX-rt_role-2020-01-01_6510000 (46 Calculation Arcs)
"""

from ... import AccountSpec, SignRule, AccountOrigin, AccountRole

DIRECT_METHOD_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("CFS.NET", "NetIncreaseDecreaseInCashAndCashEquivalents", parent_code=None, sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFO", "NetCashFlowsReceivedFromUsedInOperatingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFO.01", "ReceiptsFromInsurancePremiums", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.02", "ReceiptsFromReinsuranceClaims", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.03", "ReceiptsFromCommission", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.04", "ReceiptsFromRetrocessionClaims", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.05", "PaymentsOfCommission", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.06", "PaymentsForReinsurancePremiums", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.07", "PaymentsForInsuranceClaimsAndBenefits", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.08", "PaymentsForRetrocessionPremiums", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.09", "PaymentsForOtherUnderwritingExpenses", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.10", "PaymentsForGeneralAndAdministrativeExpense", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.10.PLURAL", "PaymentsForGeneralAndAdministrativeExpenses", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.11", "PaymentsForMarketingExpenses", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.12", "PaymentsForSalariesAndAllowances", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.13", "PaymentsForCorporateIncomeTax", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.14", "InterestsReceivedFromOperatingActivities", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.15", "InterestsPaidFromOperatingActivities", parent_code="CFO", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFO.16", "IncomeTaxesRefundedPaidFromOperatingActivities", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.17", "RepaymentPlacementOfRefundableDeposits", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFO.18", "OtherCashInflowsOutflowsFromOperatingActivities", parent_code="CFO", sign_rule=SignRule.RAW),
    AccountSpec("CFI", "NetCashFlowsReceivedFromUsedInInvestingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFI.01", "ReceiptsOfInvestmentIncome", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.02", "ProceedsFromSalesOfInvestments", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.03", "ProceedsFromDisposalOfPropertyAndEquipment", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.04", "PaymentsForAcquisitionOfPropertyAndEquipment", parent_code="CFI", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFI.05", "ProceedsFromDisposalOfInvestmentProperties", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.06", "PaymentsForAcquisitionOfInvestmentProperties", parent_code="CFI", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFI.07", "ProceedsFromDisposalOfIntangibleAssets", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.08", "PaymentsForAcquisitionOfIntangibleAssets", parent_code="CFI", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFI.09", "ProceedsFromDisposalOfOtherNonFinancialAssets", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.10", "PaymentsForAcquisitionOfOtherNonFinancialAssets", parent_code="CFI", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFI.11", "ReceiptsFromPaymentsForPolicyLoans", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.12", "DividendsReceivedFromInvestingActivities", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.13", "InterestsReceivedFromInvestingActivities", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.14", "InterestsPaidFromInvestingActivities", parent_code="CFI", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFI.15", "IncomeTaxesRefundedPaidFromInvestingActivities", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.16", "OtherCashInflowsOutflowsFromInvestingActivities", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFF", "NetCashFlowsReceivedFromUsedInFinancingActivities", parent_code="CFS.NET", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("CFF.01", "DividendsPaidFromFinancingActivities", parent_code="CFF", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFF.02", "ProceedsFromIssuanceOfCommonStocks", parent_code="CFF", sign_rule=SignRule.RAW),
    AccountSpec("CFF.03", "ProceedsFromIssuanceOfPreferredStocks", parent_code="CFF", sign_rule=SignRule.RAW),
    AccountSpec("CFF.04", "ProceedFromIncreaseOfNonControllingInterest", parent_code="CFF", sign_rule=SignRule.RAW),
    AccountSpec("CFF.05", "PaymentsOfStockIssuanceCosts", parent_code="CFF", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFF.06", "InterestsReceivedFromFinancingActivities", parent_code="CFF", sign_rule=SignRule.RAW),
    AccountSpec("CFF.07", "InterestsPaidFromFinancingActivities", parent_code="CFF", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFF.08", "IncomeTaxesRefundedPaidFromFinancingActivities", parent_code="CFF", sign_rule=SignRule.RAW),
    AccountSpec("CFF.09", "OtherCashInflowsOutflowsFromFinancingActivities", parent_code="CFF", sign_rule=SignRule.RAW),
    AccountSpec("CFI.FVOCI", "WithdrawalPlacementOfFinancialAssetsFairValueThroughOtherComprehensiveIncome", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFI.AC_P", "PlacementOfFinancialAssetsAmortizedCostInvestments", parent_code="CFI", sign_rule=SignRule.SUB_RAW),
    AccountSpec("CFI.AC_W", "WithdrawalOfFinancialAssetsAmortizedCostInvestments", parent_code="CFI", sign_rule=SignRule.RAW),
    AccountSpec("CFS.FX", "EffectOfExchangeRateChangesOnCashAndCashEquivalents", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("CFS.OTH", "OtherIncreaseDecreaseInCashAndCashEquivalents", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("CFS.DEC", "CashAndCashEquivalentOfDeconsolidatedSubsidiaries", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("CFS.CASH", "CashAndCashEquivalentsCashFlows", parent_code=None, sign_rule=SignRule.RAW, role=AccountRole.BRIDGE, origin=AccountOrigin.REPORTED),
)

__all__ = ["DIRECT_METHOD_HIERARCHY"]
