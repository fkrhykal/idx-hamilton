"""Cross-statement and inter-temporal equation specifications.

Validates fundamental accounting identities connecting multiple financial statements:
1. Cash Tie-Out: Balance Sheet Ending Cash == Cash Flow Ending Cash
2. Prior Cash Tie-Out: Balance Sheet Beginning Cash == Cash Flow Beginning Cash
3. Cash Roll-Forward: CFS Ending Cash == Beginning Cash + Net Change + FX + Decon + Other
4. Operating Profit Tie-Out: Income Statement Profit == Cash Flow Operating Profit (Indirect Method Only)
"""

from __future__ import annotations

from idx_hamilton.transformations.hierarchy import (
    AccountRole,
    AccountSpec,
    SignRule,
)

from .domain import (
    AccountingEquationCategory,
    AccountingEquationOperator,
    AccountingEquationSpecification,
    EquationComponentTerm,
)

# 1. Cross-Statement Account Specs
_SPEC_BS_CASH = AccountSpec(
    code="BS.CASH",
    account="CashAndCashEquivalents",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_BS_BANK_CASH = AccountSpec(
    code="BS.BANK.CASH",
    account="Cash",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_BS_CA_BI = AccountSpec(
    code="BS.CA.BI",
    account="CurrentAccountsWithBankIndonesia",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_BS_CA_OB_TP = AccountSpec(
    code="BS.CA.OB_TP",
    account="CurrentAccountsWithOtherBanksThirdParties",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_BS_CA_OB_RP = AccountSpec(
    code="BS.CA.OB_RP",
    account="CurrentAccountsWithOtherBanksRelatedParties",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_BS_PL_BI_TP = AccountSpec(
    code="BS.PL.BI_TP",
    account="PlacementsWithBankIndonesiaAndOtherBanksThirdParties",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_BS_PL_BI_RP = AccountSpec(
    code="BS.PL.BI_RP",
    account="PlacementsWithBankIndonesiaAndOtherBanksRelatedParties",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_BS_CASH_PRIOR = AccountSpec(
    code="BS.CASH.PRIOR",
    account="CashAndCashEquivalents",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_CFS_CASH_END = AccountSpec(
    code="CFS.CASH.END",
    account="CashAndCashEquivalentsCashFlows",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_CFS_CASH_BEG = AccountSpec(
    code="CFS.CASH.BEG",
    account="CashAndCashEquivalentsCashFlows",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_CFS_NET = AccountSpec(
    code="CFS.NET",
    account="NetIncreaseDecreaseInCashAndCashEquivalents",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=True,
    role=AccountRole.SUMMATIVE,
)

_SPEC_CFS_FX = AccountSpec(
    code="CFS.FX",
    account="EffectOfExchangeRateChangesOnCashAndCashEquivalents",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_CFS_DEC = AccountSpec(
    code="CFS.DEC",
    account="CashAndCashEquivalentOfDeconsolidatedSubsidiaries",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_CFS_OTH = AccountSpec(
    code="CFS.OTH",
    account="OtherIncreaseDecreaseInCashAndCashEquivalents",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

_SPEC_IS_PL = AccountSpec(
    code="IS.PL",
    account="ProfitLoss",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=True,
    role=AccountRole.SUMMATIVE,
)

_SPEC_CFS_PL = AccountSpec(
    code="CFS.PL",
    account="ProfitLoss",
    parent_code=None,
    sign_rule=SignRule.ADD,
    is_total=False,
    role=AccountRole.SUMMATIVE,
)

# 2. Individual Equation Specifications
CROSS_BS_CASH = AccountingEquationSpecification(
    equation_name="Cross-Statement Cash Tie-Out: Balance Sheet Cash == Cash Flow Ending Cash",
    statement_type="cross_statement",
    target_account=_SPEC_BS_CASH,
    component_terms=(
        EquationComponentTerm(
            account_specification=_SPEC_CFS_CASH_END,
            statement_namespace="cash_flow_statement",
            reporting_context="CurrentYearInstant",
        ),
    ),
    operator=AccountingEquationOperator.EQUALS,
    equation_category=AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION,
    target_statement_namespace="balance_statement",
    target_reporting_context="CurrentYearInstant",
)

CROSS_BS_CASH_PRIOR = AccountingEquationSpecification(
    equation_name="Cross-Statement Prior Cash Tie-Out: Balance Sheet Prior Cash == Cash Flow Beginning Cash",
    statement_type="cross_statement",
    target_account=_SPEC_BS_CASH_PRIOR,
    component_terms=(
        EquationComponentTerm(
            account_specification=_SPEC_CFS_CASH_BEG,
            statement_namespace="cash_flow_statement",
            reporting_context="PriorEndYearInstant",
        ),
    ),
    operator=AccountingEquationOperator.EQUALS,
    equation_category=AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION,
    target_statement_namespace="balance_statement",
    target_reporting_context="PriorEndYearInstant",
)

CROSS_CFS_ROLL_FORWARD = AccountingEquationSpecification(
    equation_name="Inter-Temporal Cash Roll-Forward: Cash Ending == Beginning + Net + FX + Decon + Other",
    statement_type="cross_statement",
    target_account=_SPEC_CFS_CASH_END,
    component_terms=(
        EquationComponentTerm(
            account_specification=_SPEC_CFS_CASH_BEG,
            statement_namespace="cash_flow_statement",
            reporting_context="PriorEndYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_CFS_NET,
            statement_namespace="cash_flow_statement",
            reporting_context="CurrentYearDuration",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_CFS_FX,
            statement_namespace="cash_flow_statement",
            reporting_context="CurrentYearDuration",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_CFS_DEC,
            statement_namespace="cash_flow_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_CFS_OTH,
            statement_namespace="cash_flow_statement",
            reporting_context="CurrentYearDuration",
        ),
    ),
    operator=AccountingEquationOperator.EQUALS,
    equation_category=AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION,
    target_statement_namespace="cash_flow_statement",
    target_reporting_context="CurrentYearInstant",
)

CROSS_IS_PL = AccountingEquationSpecification(
    equation_name="Cross-Statement Operating Profit Tie-Out: Income Statement Profit == Cash Flow Profit",
    statement_type="cross_statement",
    target_account=_SPEC_IS_PL,
    component_terms=(
        EquationComponentTerm(
            account_specification=_SPEC_CFS_PL,
            statement_namespace="cash_flow_statement",
            reporting_context="CurrentYearDuration",
        ),
    ),
    operator=AccountingEquationOperator.EQUALS,
    equation_category=AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION,
    target_statement_namespace="income_statement",
    target_reporting_context="CurrentYearDuration",
)

CROSS_FINANCING_BS_CASH = AccountingEquationSpecification(
    equation_name="Cross-Statement Financing Cash Tie-Out: CFS Ending Cash == BS Cash + Giro BI + Giro Bank Lain + Penempatan",
    statement_type="cross_statement",
    target_account=_SPEC_CFS_CASH_END,
    component_terms=(
        EquationComponentTerm(
            account_specification=_SPEC_BS_CASH,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_CA_BI,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_CA_OB_TP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_CA_OB_RP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_PL_BI_TP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_PL_BI_RP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
    ),
    operator=AccountingEquationOperator.EQUALS,
    equation_category=AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION,
    target_statement_namespace="cash_flow_statement",
    target_reporting_context="CurrentYearInstant",
)

CROSS_BANK_BS_CASH = AccountingEquationSpecification(
    equation_name="Cross-Statement Bank Cash Tie-Out: CFS Ending Cash == BS Cash + Giro BI + Giro Bank Lain + Penempatan",
    statement_type="cross_statement",
    target_account=_SPEC_CFS_CASH_END,
    component_terms=(
        EquationComponentTerm(
            account_specification=_SPEC_BS_BANK_CASH,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_CA_BI,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_CA_OB_TP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_CA_OB_RP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_PL_BI_TP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
        EquationComponentTerm(
            account_specification=_SPEC_BS_PL_BI_RP,
            statement_namespace="balance_statement",
            reporting_context="CurrentYearInstant",
        ),
    ),
    operator=AccountingEquationOperator.EQUALS,
    equation_category=AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION,
    target_statement_namespace="cash_flow_statement",
    target_reporting_context="CurrentYearInstant",
)

# Tuple of all unique cross-statement equations (Current period only)
CROSS_STATEMENT_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    CROSS_BS_CASH,
    CROSS_FINANCING_BS_CASH,
    CROSS_BANK_BS_CASH,
    CROSS_IS_PL,
)

# Modular mapping per Entry Point and CFS Variant (Customized per Sector & Variant)
ENTRY_POINT_CROSS_EQUATIONS: dict[
    str, dict[str, tuple[AccountingEquationSpecification, ...]]
] = {
    "general": {
        "direct_method": (CROSS_BS_CASH,),
        "indirect_method": (CROSS_BS_CASH, CROSS_IS_PL),
    },
    "property": {
        "direct_method": (CROSS_BS_CASH,),
        "indirect_method": (CROSS_BS_CASH, CROSS_IS_PL),
    },
    "infrastructure": {
        "direct_method": (CROSS_BS_CASH,),
        "indirect_method": (CROSS_BS_CASH, CROSS_IS_PL),
    },
    "financing": {
        "direct_method": (CROSS_FINANCING_BS_CASH,),
    },
    "insurance": {
        "direct_method": (CROSS_BS_CASH,),
    },
    "securities": {
        "direct_method": (CROSS_BS_CASH,),
    },
    "financial_and_sharia": {
        "direct_method": (CROSS_BANK_BS_CASH,),
        "indirect_method": (CROSS_BANK_BS_CASH, CROSS_IS_PL),
    },
    "collective_investment_contract": {
        "direct_method": (CROSS_BS_CASH,),
    },
}


def get_cross_equations(
    entry_point: str, cfs_variant: str
) -> tuple[AccountingEquationSpecification, ...]:
    """Retrieves tuple of Cross-Statement EquationSpecs for a given Entry Point and CFS Variant."""
    return ENTRY_POINT_CROSS_EQUATIONS.get(entry_point, {}).get(cfs_variant, ())


__all__ = [
    "CROSS_BANK_BS_CASH",
    "CROSS_BS_CASH",
    "CROSS_BS_CASH_PRIOR",
    "CROSS_CFS_ROLL_FORWARD",
    "CROSS_FINANCING_BS_CASH",
    "CROSS_IS_PL",
    "CROSS_STATEMENT_EQUATIONS",
    "ENTRY_POINT_CROSS_EQUATIONS",
    "get_cross_equations",
]
