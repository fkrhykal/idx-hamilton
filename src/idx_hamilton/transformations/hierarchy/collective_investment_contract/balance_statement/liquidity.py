"""Definisi hierarki akun untuk:
Entry Point : collective_investment_contract
Statement   : balance_statement
Variant     : liquidity
"""

from ... import AccountSpec, SignRule

LIQUIDITY_HIERARCHY: tuple[AccountSpec, ...] = (
    AccountSpec("A", "Assets", parent_code=None, sign_rule=SignRule.ADD, is_total=True),
    AccountSpec("A.C.01", "CashAndCashEquivalents", parent_code="A", sign_rule=SignRule.ADD),
    AccountSpec("A.L.110", "OtherReceivables", parent_code="A", sign_rule=SignRule.ADD),
    AccountSpec("A.L.17", "PrepaidTaxes", parent_code="A", sign_rule=SignRule.ADD),
    AccountSpec("A.L.49", "SecuritiesPortfolioInEquityInstruments", parent_code="A", sign_rule=SignRule.ADD),
    AccountSpec("L", "Liabilities", parent_code="LNA", sign_rule=SignRule.ADD, is_total=True),
    AccountSpec("L.C.25", "TaxesPayable", parent_code="L", sign_rule=SignRule.ADD),
    AccountSpec("L.L.10", "AccruedExpenses", parent_code="L", sign_rule=SignRule.ADD),
    AccountSpec("L.L.57", "AccountsPayable", parent_code="L", sign_rule=SignRule.ADD),
    AccountSpec("LNA", "LiabilitiesAndNetAssets", parent_code=None, sign_rule=SignRule.ADD, is_total=True),
    AccountSpec("NA", "NetAssets", parent_code="LNA", sign_rule=SignRule.RAW, is_total=True),
    AccountSpec("NA.NAV", "NetAssetsAttributableToUnitHoldersPerInvestmentUnit", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("NA.SH", "OutstandingInvestmentUnits", parent_code=None, sign_rule=SignRule.RAW),
    AccountSpec("NA.U", "NetAssetsAttributableToParticipationUnitHolders", parent_code="NA", sign_rule=SignRule.ADD),
)

__all__ = ["LIQUIDITY_HIERARCHY"]
