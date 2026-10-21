"""Definisi hierarki akun untuk:
Entry Point : securities
Statement   : balance_statement
Variant     : current_and_non_current
"""

from ... import AccountSpec, SignRule

CURRENT_AND_NON_CURRENT_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("A", "Assets", parent_code=None, sign_rule=SignRule.ADD, is_total=True),
    AccountSpec("A.C.01", "CashAndCashEquivalents", parent_code="A.C", sign_rule=SignRule.ADD),
    AccountSpec("A.C.20", "MarginReceivables", parent_code="A.C", sign_rule=SignRule.ADD),
    AccountSpec("A.C.21", "ReceivablesFromClearingAndSettlementGuaranteeInstitution", parent_code="A.C", sign_rule=SignRule.ADD),
    AccountSpec("A.N.33", "PropertyPlantAndEquipment", parent_code="A.N", sign_rule=SignRule.ADD),
    AccountSpec("A.N.35", "InvestmentProperties", parent_code="A.N", sign_rule=SignRule.ADD),
    AccountSpec("A.N.36", "InvestmentsInAssociates", parent_code="A.N", sign_rule=SignRule.ADD),
    AccountSpec("A.N.39", "Goodwill", parent_code="A.N", sign_rule=SignRule.ADD),
    AccountSpec("A.N.40", "IntangibleAssetsOtherThanGoodwill", parent_code="A.N", sign_rule=SignRule.ADD),
    AccountSpec("A.N.41", "DeferredTaxAssets", parent_code="A.N", sign_rule=SignRule.ADD),
    AccountSpec("A.N.62", "PropertyAndEquipment", parent_code="A.N", sign_rule=SignRule.ADD),
    AccountSpec("E", "Equity", parent_code="LE", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("E.NCI", "NonControllingInterests", parent_code="E", sign_rule=SignRule.RAW),
    AccountSpec("E.P", "EquityAttributableToEquityOwnersOfParentEntity", parent_code="E", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("E.P.01", "CommonStocks", parent_code="E.P", sign_rule=SignRule.ADD),
    AccountSpec("E.P.02", "AdditionalPaidInCapital", parent_code="E.P", sign_rule=SignRule.RAW),
    AccountSpec("E.P.04", "TreasuryStocks", parent_code="E.P", sign_rule=SignRule.SUB),
    AccountSpec("E.P.05", "UnappropriatedRetainedEarnings", parent_code="E.P", sign_rule=SignRule.RAW),
    AccountSpec("E.P.06", "AppropriatedRetainedEarnings", parent_code="E.P", sign_rule=SignRule.RAW),
    AccountSpec("E.P.11", "ReserveOfRemeasurementsOfDefinedBenefitPlans", parent_code="E.P", sign_rule=SignRule.RAW),
    AccountSpec("E.P.13", "OtherReserves", parent_code="E.P", sign_rule=SignRule.RAW),
    AccountSpec("E.P.14", "OtherComponentsOfEquity", parent_code="E.P", sign_rule=SignRule.RAW),
    AccountSpec("L", "Liabilities", parent_code="LE", sign_rule=SignRule.ADD, is_total=True),
    AccountSpec("L.C.24", "DividendsPayable", parent_code="L.C", sign_rule=SignRule.ADD),
    AccountSpec("L.C.25", "TaxesPayable", parent_code="L.C", sign_rule=SignRule.ADD),
    AccountSpec("L.C.37", "PayablesToCustomersThirdParties", parent_code="L.C", sign_rule=SignRule.ADD),
    AccountSpec("L.C.38", "PayablesToClearingAndSettlementGuaranteeInstitution", parent_code="L.C", sign_rule=SignRule.ADD),
    AccountSpec("L.C.49", "PayablesToCustomersRelatedParties", parent_code="L.C", sign_rule=SignRule.ADD),
    AccountSpec("L.N.17", "DeferredTaxLiabilities", parent_code="L.N", sign_rule=SignRule.ADD),
    AccountSpec("LE", "LiabilitiesAndEquity", parent_code=None, sign_rule=SignRule.ADD, is_total=True),
)

__all__ = ["CURRENT_AND_NON_CURRENT_HIERARCHY"]
