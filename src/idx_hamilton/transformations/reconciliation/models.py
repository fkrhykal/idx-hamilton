"""Strongly-typed Patito models and schemas for accounting discrepancy classification.

Provides self-documenting data structures and validation schemas for audit findings,
decoupled from any presentation, rendering, or report generation layers.
"""

from __future__ import annotations

from enum import StrEnum

import patito as pt

from idx_hamilton.models import Model


class AuditDiscrepancyCategory(StrEnum):
    """Categorization of audit reconciliation findings based on structural and mathematical patterns."""

    CONFORMANT_EXACT = "conformant_exact"
    CONFORMANT_WITHIN_ROUNDING_TOLERANCE = "conformant_within_rounding_tolerance"
    DUPLICATE_LINE_ITEM = "duplicate_line_item"
    SIGN_INVERSION = "sign_inversion"
    OMITTED_INTERMEDIATE_SUBTOTAL = "omitted_intermediate_subtotal"
    ROGUE_CHILD_WITHOUT_PARENT = "rogue_child_without_parent"
    LUMP_SUM_AGGREGATE_PRESENTATION = "lump_sum_aggregate_presentation"
    MATERIAL_REPORTING_DISCREPANCY = "material_reporting_discrepancy"
    OMITTED_PARTIAL_SUBTOTAL = "omitted_partial_subtotal"
    PARTIAL_BREAKDOWN_DISCREPANCY = "partial_breakdown_discrepancy"


class AuditDiscrepancyFinding(Model):
    """Strongly-typed, self-documenting record of an accounting equation audit discrepancy.

    Encapsulates all relevant diagnostic attributes needed by audit reports, API consumers,
    or downstream data pipelines without coupling to presentation formatting.
    """

    entity_ticker: str = pt.Field(
        description="Stock ticker symbol of the reporting issuer on the Indonesia Stock Exchange."
    )
    fiscal_year: int = pt.Field(
        description="Fiscal reporting year of the audited financial statement."
    )
    fiscal_period: str = pt.Field(
        description="Fiscal reporting period (e.g., Audit, TW1, TW2, TW3)."
    )
    equation_identifier: str = pt.Field(
        description="Deterministic unique identifier of the accounting equation being verified."
    )
    category: AuditDiscrepancyCategory = pt.Field(
        description="Classified diagnostic pattern category of the reconciliation variance."
    )
    reported_target_balance: float = pt.Field(
        description="Reported benchmark balance of the primary target account."
    )
    recalculated_components_total: float = pt.Field(
        description="Sum of component accounts or counterpart articulated balance."
    )
    reconciliation_variance: float = pt.Field(
        description="Absolute deviation between reported target balance and recalculated total."
    )
    deviation_ratio_percent: float = pt.Field(
        description="Percentage ratio of variance relative to reported target balance."
    )

    # Diagnostic attributes specific to particular discrepancy patterns
    duplicate_account_name: str | None = pt.Field(
        default=None,
        description="Account name identified as duplicate disclosure.",
    )
    duplicate_reported_amount: float | None = pt.Field(
        default=None,
        description="Reported nominal balance of the duplicated line item.",
    )
    paired_reference_account: str | None = pt.Field(
        default=None,
        description="Reference account against which duplicate equivalence was confirmed.",
    )

    inverted_account_name: str | None = pt.Field(
        default=None,
        description="Account name identified as suffering from opposite algebraic sign polarity.",
    )
    inverted_reported_amount: float | None = pt.Field(
        default=None,
        description="Reported nominal input value of the sign-inverted account.",
    )
    expected_sign_direction: str | None = pt.Field(
        default=None,
        description="Expected algebraic sign direction (e.g. positive vs negative).",
    )

    omitted_subtotal_account_name: str | None = pt.Field(
        default=None,
        description="Intermediate subtotal taxonomy account left unpopulated (0.00).",
    )
    active_leaf_breakdown_accounts: str | None = pt.Field(
        default=None,
        description="Summary of active lowest-grain leaf accounts populating the target balance.",
    )
    active_children_count: int | None = pt.Field(
        default=None,
        description="Count of active child line items carrying non-zero balances.",
    )
    diagnostic_audit_notes: str = pt.Field(
        description="Objective, factual audit summary note describing the finding."
    )
