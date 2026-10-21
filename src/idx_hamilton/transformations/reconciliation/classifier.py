"""Decoupled diagnostic classification engine for accounting equation variances.

Analyzes financial statement reconciliations against AccountingEquationSpecifications
and produces strongly-typed AuditDiscrepancyFinding Patito models, completely decoupled
from any presentation, markdown, or report rendering logic.
"""

from __future__ import annotations

from collections.abc import Sequence
from itertools import combinations

import polars as pl

from idx_hamilton.transformations.equations.domain import (
    AccountingEquationSpecification,
)

from .models import (
    AuditDiscrepancyCategory,
    AuditDiscrepancyFinding,
)

ZERO_THRESHOLD: float = 1e-6
RELATIVE_TOLERANCE_RATIO: float = 0.01


def classify_accounting_equation_discrepancies(
    verified_financial_data: pl.DataFrame,
    equation_specifications: Sequence[AccountingEquationSpecification],
) -> dict[str, list[AuditDiscrepancyFinding]]:
    """Evaluates and classifies every reporting period row for each equation into strongly-typed audit findings.

    Args:
        verified_financial_data: Polars DataFrame enriched by AccountingEquationEngine.
        equation_specifications: Sequence of AccountingEquationSpecification instances to audit.

    Returns:
        Mapping of equation_identifier to a list of AuditDiscrepancyFinding instances per row.
    """
    available_column_names: set[str] = set(verified_financial_data.columns)

    children_by_target_column: dict[str, AccountingEquationSpecification] = {
        equation.target_physical_column_name: equation
        for equation in equation_specifications
    }

    raw_data_rows: list[dict] = verified_financial_data.to_dicts()
    findings_by_equation: dict[str, list[AuditDiscrepancyFinding]] = {}

    for equation in equation_specifications:
        equation_id = equation.equation_identifier
        conformance_column = f"is_conformant_{equation_id}"
        target_balance_column = f"target_{equation_id}"
        recalculated_column = f"recalculated_{equation_id}"
        variance_column = f"variance_{equation_id}"

        if conformance_column not in available_column_names:
            findings_by_equation[equation_id] = [
                AuditDiscrepancyFinding(
                    entity_ticker=str(row.get("ticker", "UNKNOWN")),
                    fiscal_year=int(row.get("year", 0)),
                    fiscal_period=str(row.get("period", "UNKNOWN")),
                    equation_identifier=equation_id,
                    category=AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY,
                    reported_target_balance=0.0,
                    recalculated_components_total=0.0,
                    reconciliation_variance=0.0,
                    deviation_ratio_percent=100.0,
                    diagnostic_audit_notes="Kolom evaluasi persamaan tidak tersedia dalam data",
                )
                for row in raw_data_rows
            ]
            continue

        equation_findings: list[AuditDiscrepancyFinding] = []

        for row in raw_data_rows:
            entity_ticker = str(row.get("ticker", "UNKNOWN"))
            fiscal_year = int(row.get("year", 0))
            fiscal_period = str(row.get("period", "UNKNOWN"))

            reported_target_balance: float = float(
                row.get(target_balance_column) or 0.0
            )
            direct_components_sum: float = float(row.get(recalculated_column) or 0.0)
            reconciliation_variance: float = float(row.get(variance_column) or 0.0)

            is_conformant_flag: bool = bool(row.get(conformance_column))

            # 1. Exact or Conformance within Tolerance
            if is_conformant_flag:
                conformance_category = (
                    AuditDiscrepancyCategory.CONFORMANT_EXACT
                    if reconciliation_variance <= ZERO_THRESHOLD
                    else AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE
                )
                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=conformance_category,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=direct_components_sum,
                        reconciliation_variance=reconciliation_variance,
                        deviation_ratio_percent=0.0,
                        diagnostic_audit_notes="Keterhubungan saldo seimbang konsisten",
                    )
                )
                continue

            numerical_tolerance = max(
                equation.numerical_tolerance,
                abs(reported_target_balance) * RELATIVE_TOLERANCE_RATIO,
            )

            # 2. Rogue Child (Target balance is zero, but component children have non-zero balance)
            if (
                abs(reported_target_balance) <= ZERO_THRESHOLD
                and abs(direct_components_sum) > ZERO_THRESHOLD
            ):
                active_child_accounts: list[tuple[str, float]] = []
                for term in equation.component_terms:
                    child_column = term.target_physical_column_name
                    child_value = float(row.get(child_column) or 0.0)
                    if abs(child_value) > ZERO_THRESHOLD:
                        active_child_accounts.append((child_column, child_value))

                active_summary_strings = [
                    f"`{account_name}` (Rp {abs(nominal):,.0f})"
                    for account_name, nominal in active_child_accounts
                ]
                audit_notes = (
                    f"Saldo induk dilaporkan 0.00; pos rincian terisi: {', '.join(active_summary_strings[:2])}"
                    f"{'...' if len(active_summary_strings) > 2 else ''}"
                )

                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=AuditDiscrepancyCategory.ROGUE_CHILD_WITHOUT_PARENT,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=direct_components_sum,
                        reconciliation_variance=abs(direct_components_sum),
                        deviation_ratio_percent=100.0,
                        active_children_count=len(active_child_accounts),
                        active_leaf_breakdown_accounts=", ".join(
                            account_name for account_name, _ in active_child_accounts
                        ),
                        diagnostic_audit_notes=audit_notes,
                    )
                )
                continue

            # Traversal for skipped intermediate subtotals and leaf terms expansion
            direct_terms_list: list[tuple[str, float, float]] = []
            skipped_subtotals_list: list[tuple[str, float, float]] = []
            expanded_leaf_terms_list: list[tuple[str, float, float]] = []
            gross_scaling_factor = abs(reported_target_balance)

            for term in equation.component_terms:
                term_column_name = term.target_physical_column_name
                raw_term_value = (
                    float(row.get(term_column_name) or 0.0)
                    if term_column_name in available_column_names
                    else 0.0
                )
                multiplier = term.resolve_multiplier()
                child_equation = children_by_target_column.get(term_column_name)

                child_recalculated_col = (
                    f"recalculated_{child_equation.equation_identifier}"
                    if child_equation
                    else ""
                )

                if (
                    child_equation is not None
                    and child_equation.equation_identifier
                    != equation.equation_identifier
                    and child_recalculated_col in available_column_names
                ):
                    child_recalculated_value = float(
                        row.get(child_recalculated_col) or 0.0
                    )

                    if (
                        abs(raw_term_value) <= ZERO_THRESHOLD
                        and abs(child_recalculated_value) > ZERO_THRESHOLD
                    ):
                        skipped_subtotals_list.append(
                            (
                                term_column_name,
                                multiplier * child_recalculated_value,
                                child_recalculated_value,
                            )
                        )
                        for child_term in child_equation.component_terms:
                            leaf_col = child_term.target_physical_column_name
                            leaf_val = (
                                float(row.get(leaf_col) or 0.0)
                                if leaf_col in available_column_names
                                else 0.0
                            )
                            if abs(leaf_val) > ZERO_THRESHOLD:
                                expanded_leaf_terms_list.append(
                                    (
                                        leaf_col,
                                        multiplier
                                        * child_term.resolve_multiplier()
                                        * leaf_val,
                                        leaf_val,
                                    )
                                )
                                gross_scaling_factor = max(
                                    gross_scaling_factor, abs(leaf_val)
                                )
                        continue
                    elif abs(raw_term_value) > ZERO_THRESHOLD:
                        for child_term in child_equation.component_terms:
                            leaf_col = child_term.target_physical_column_name
                            leaf_val = (
                                float(row.get(leaf_col) or 0.0)
                                if leaf_col in available_column_names
                                else 0.0
                            )
                            if abs(leaf_val) > ZERO_THRESHOLD:
                                expanded_leaf_terms_list.append(
                                    (
                                        leaf_col,
                                        multiplier
                                        * child_term.resolve_multiplier()
                                        * leaf_val,
                                        leaf_val,
                                    )
                                )
                                gross_scaling_factor = max(
                                    gross_scaling_factor, abs(leaf_val)
                                )

                if abs(raw_term_value) > ZERO_THRESHOLD:
                    direct_terms_list.append(
                        (
                            term_column_name,
                            multiplier * raw_term_value,
                            raw_term_value,
                        )
                    )
                    gross_scaling_factor = max(
                        gross_scaling_factor, abs(raw_term_value)
                    )

            recalculated_with_skipped_subtotals = direct_components_sum + sum(
                signed_component for _, signed_component, _ in skipped_subtotals_list
            )
            all_active_terms = direct_terms_list + (
                expanded_leaf_terms_list if skipped_subtotals_list else []
            )
            base_recalculated_components = (
                recalculated_with_skipped_subtotals
                if skipped_subtotals_list
                else direct_components_sum
            )

            # 3. Pure Skipped Intermediate Subtotal (reconciles 100% when leaf breakdown expanded)
            variance_after_leaf_expansion = abs(
                reported_target_balance - recalculated_with_skipped_subtotals
            )
            if (
                skipped_subtotals_list
                and variance_after_leaf_expansion <= numerical_tolerance
            ):
                skipped_account_names = [
                    f"`{account_name}`" for account_name, _, _ in skipped_subtotals_list
                ]
                leaf_detail_strings = [
                    f"`{leaf_name}` (Rp {nominal:,.0f})"
                    for leaf_name, nominal, _ in expanded_leaf_terms_list
                ]
                audit_notes = (
                    f"Subtotal perantara {', '.join(skipped_account_names)} kosong (0.00); "
                    f"rincian pos daun terisi {', '.join(leaf_detail_strings[:2])}"
                    f"{'...' if len(leaf_detail_strings) > 2 else ''} (menjumlah klop 100% ke saldo induk)"
                )

                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=AuditDiscrepancyCategory.OMITTED_INTERMEDIATE_SUBTOTAL,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=recalculated_with_skipped_subtotals,
                        reconciliation_variance=variance_after_leaf_expansion,
                        deviation_ratio_percent=(
                            (
                                variance_after_leaf_expansion
                                / abs(reported_target_balance)
                            )
                            * 100.0
                            if abs(reported_target_balance) > ZERO_THRESHOLD
                            else 0.0
                        ),
                        omitted_subtotal_account_name=", ".join(
                            account_name
                            for account_name, _, _ in skipped_subtotals_list
                        ),
                        active_leaf_breakdown_accounts=", ".join(
                            f"{account_name} (Rp {nominal:,.0f})"
                            for account_name, nominal, _ in expanded_leaf_terms_list
                        ),
                        active_children_count=len(expanded_leaf_terms_list),
                        diagnostic_audit_notes=audit_notes,
                    )
                )
                continue

            # 4. Sign Inversion / Double Negative Detection
            is_sign_inversion_detected = False
            inverted_account_name = ""
            inverted_reported_amount = 0.0
            expected_sign_direction = ""
            sign_inversion_notes = ""

            if skipped_subtotals_list:
                for (
                    subtotal_name,
                    signed_subtotal,
                    _,
                ) in skipped_subtotals_list:
                    adjusted_variance = abs(
                        reported_target_balance
                        - (base_recalculated_components - 2.0 * signed_subtotal)
                    )
                    if (
                        adjusted_variance <= numerical_tolerance
                        and adjusted_variance < 0.2 * reconciliation_variance
                    ):
                        is_sign_inversion_detected = True
                        inverted_account_name = subtotal_name
                        inverted_reported_amount = signed_subtotal
                        expected_sign_direction = "-" if signed_subtotal >= 0 else "+"
                        sign_inversion_notes = f"Pembalikan tanda (+/-) pada subtotal perantara `{subtotal_name}` (Rp {signed_subtotal:,.0f})"
                        break

            if not is_sign_inversion_detected:
                negative_subtractive_items = [
                    (account_name, signed_component, raw_val)
                    for account_name, signed_component, raw_val in all_active_terms
                    if raw_val < 0 and signed_component > 0
                ]
                negative_subtractive_sum = sum(
                    signed_comp for _, signed_comp, _ in negative_subtractive_items
                )
                if negative_subtractive_sum > 0:
                    adjusted_variance = abs(
                        reported_target_balance
                        - (
                            base_recalculated_components
                            - 2.0 * negative_subtractive_sum
                        )
                    )
                    if (
                        adjusted_variance <= numerical_tolerance
                        and adjusted_variance < 0.2 * reconciliation_variance
                    ):
                        is_sign_inversion_detected = True
                        inverted_account_name = negative_subtractive_items[0][0]
                        inverted_reported_amount = negative_subtractive_items[0][1]
                        expected_sign_direction = "+"
                        sign_inversion_notes = f"Pembalikan tanda minus ganda pada pos pengurang: {', '.join(f'`{name}`' for name, _, _ in negative_subtractive_items)}"

            if not is_sign_inversion_detected:
                max_combination_degree = 3 if len(all_active_terms) <= 12 else 2
                for combination_degree in range(1, max_combination_degree + 1):
                    if len(all_active_terms) >= combination_degree:
                        for term_combination in combinations(
                            all_active_terms, combination_degree
                        ):
                            adjustment_sum = sum(
                                signed_comp for _, signed_comp, _ in term_combination
                            )
                            adjusted_variance = abs(
                                reported_target_balance
                                - (base_recalculated_components - 2.0 * adjustment_sum)
                            )
                            if (
                                adjusted_variance <= numerical_tolerance
                                and adjusted_variance < 0.2 * reconciliation_variance
                            ):
                                is_sign_inversion_detected = True
                                inverted_account_name = ", ".join(
                                    f"`{term_tuple[0]}`"
                                    for term_tuple in term_combination
                                )
                                inverted_reported_amount = adjustment_sum
                                expected_sign_direction = "-/+"
                                sign_inversion_notes = f"Pembalikan tanda (+/-) pada pos: {', '.join(f'`{t[0]}` (Rp {t[1]:,.0f})' for t in term_combination)}"
                                break
                    if is_sign_inversion_detected:
                        break

            if is_sign_inversion_detected:
                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=AuditDiscrepancyCategory.SIGN_INVERSION,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=base_recalculated_components,
                        reconciliation_variance=reconciliation_variance,
                        deviation_ratio_percent=(
                            (reconciliation_variance / abs(reported_target_balance))
                            * 100.0
                            if abs(reported_target_balance) > ZERO_THRESHOLD
                            else 0.0
                        ),
                        inverted_account_name=inverted_account_name,
                        inverted_reported_amount=inverted_reported_amount,
                        expected_sign_direction=expected_sign_direction,
                        diagnostic_audit_notes=sign_inversion_notes,
                    )
                )
                continue

            # 5. Duplicate Entry / Redundant Disclosure Detection
            is_duplicate_entry_detected = False
            duplicate_account_name = ""
            paired_reference_account = ""
            duplicate_reported_amount = 0.0
            duplicate_audit_notes = ""
            all_raw_nominal_values = [
                abs(raw_nominal) for _, _, raw_nominal in all_active_terms
            ]

            for (
                account_name,
                signed_nominal,
                raw_nominal,
            ) in all_active_terms:
                variance_minus = abs(
                    reported_target_balance
                    - (base_recalculated_components - signed_nominal)
                )
                variance_plus = abs(
                    reported_target_balance
                    - (base_recalculated_components + signed_nominal)
                )

                if (
                    variance_minus <= numerical_tolerance
                    and variance_minus < 0.2 * reconciliation_variance
                ) or (
                    variance_plus <= numerical_tolerance
                    and variance_plus < 0.2 * reconciliation_variance
                ):
                    duplicate_count = sum(
                        1
                        for candidate_value in all_raw_nominal_values
                        if abs(candidate_value - abs(raw_nominal))
                        <= max(1.0, abs(raw_nominal) * 0.001)
                    )
                    if (
                        abs(abs(raw_nominal) - abs(reported_target_balance))
                        <= numerical_tolerance
                        or duplicate_count >= 2
                    ):
                        is_duplicate_entry_detected = True
                        duplicate_account_name = account_name
                        duplicate_reported_amount = abs(raw_nominal)
                        matching_candidates = [
                            c_name
                            for c_name, _, c_val in all_active_terms
                            if c_name != account_name
                            and abs(abs(c_val) - abs(raw_nominal))
                            <= max(1.0, abs(raw_nominal) * 0.001)
                        ]
                        if matching_candidates:
                            paired_reference_account = matching_candidates[0]
                            duplicate_audit_notes = f"Duplikasi nominal: pos `{account_name}` bernilai kembar identik dengan `{matching_candidates[0]}` (Rp {abs(raw_nominal):,.0f})"
                        elif (
                            abs(abs(raw_nominal) - abs(reported_target_balance))
                            <= numerical_tolerance
                        ):
                            paired_reference_account = "Saldo Total Induk"
                            duplicate_audit_notes = f"Pos `{account_name}` (Rp {abs(raw_nominal):,.0f}) bernilai identik dengan saldo induk (duplikasi pos agregat ke pos rincian)"
                        else:
                            paired_reference_account = "Akun Komponen Sejenis"
                            duplicate_audit_notes = f"Pos redundan `{account_name}` (Rp {abs(signed_nominal):,.0f}) menyebabkan saldo rincian berlebih"
                        break

                if (
                    len(all_active_terms) >= 2
                    and abs(reported_target_balance) > ZERO_THRESHOLD
                    and abs(abs(raw_nominal) - abs(reported_target_balance))
                    <= max(
                        equation.numerical_tolerance,
                        abs(reported_target_balance) * 0.0001,
                    )
                ):
                    is_duplicate_entry_detected = True
                    duplicate_account_name = account_name
                    paired_reference_account = "Saldo Total Induk"
                    duplicate_reported_amount = abs(raw_nominal)
                    duplicate_audit_notes = f"Pos `{account_name}` (Rp {abs(raw_nominal):,.0f}) sama persis dengan saldo total induk (duplikasi pengungkapan)"
                    break

            if is_duplicate_entry_detected:
                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=AuditDiscrepancyCategory.DUPLICATE_LINE_ITEM,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=base_recalculated_components,
                        reconciliation_variance=abs(
                            reported_target_balance - base_recalculated_components
                        ),
                        deviation_ratio_percent=(
                            (
                                abs(
                                    reported_target_balance
                                    - base_recalculated_components
                                )
                                / abs(reported_target_balance)
                            )
                            * 100.0
                            if abs(reported_target_balance) > ZERO_THRESHOLD
                            else 0.0
                        ),
                        duplicate_account_name=duplicate_account_name,
                        paired_reference_account=paired_reference_account,
                        duplicate_reported_amount=duplicate_reported_amount,
                        diagnostic_audit_notes=duplicate_audit_notes,
                    )
                )
                continue

            # 6. Skipped Intermediate Subtotal with Incomplete Leaf Breakdown
            if skipped_subtotals_list and abs(reported_target_balance) > ZERO_THRESHOLD:
                neg_sub_sum = sum(
                    signed_comp
                    for _, signed_comp, raw_val in all_active_terms
                    if raw_val < 0 and signed_comp > 0
                )
                best_after_skip_expansion = min(
                    abs(reported_target_balance - base_recalculated_components),
                    (
                        abs(
                            reported_target_balance
                            - (base_recalculated_components - 2.0 * neg_sub_sum)
                        )
                        if neg_sub_sum > 0
                        else abs(reported_target_balance - base_recalculated_components)
                    ),
                )

                if best_after_skip_expansion < max(
                    abs(reported_target_balance), 0.25 * gross_scaling_factor
                ):
                    skipped_names = [
                        f"`{name}`" for name, _, _ in skipped_subtotals_list
                    ]
                    partial_skip_notes = (
                        f"Subtotal perantara {', '.join(skipped_names)} dilewati, namun rincian daun yang dilaporkan "
                        f"belum lengkap mencakup seluruh saldo induk (sisa selisih Rp {best_after_skip_expansion:,.0f})"
                    )
                    equation_findings.append(
                        AuditDiscrepancyFinding(
                            entity_ticker=entity_ticker,
                            fiscal_year=fiscal_year,
                            fiscal_period=fiscal_period,
                            equation_identifier=equation_id,
                            category=AuditDiscrepancyCategory.OMITTED_PARTIAL_SUBTOTAL,
                            reported_target_balance=reported_target_balance,
                            recalculated_components_total=base_recalculated_components,
                            reconciliation_variance=best_after_skip_expansion,
                            deviation_ratio_percent=(
                                (
                                    best_after_skip_expansion
                                    / abs(reported_target_balance)
                                )
                                * 100.0
                            ),
                            omitted_subtotal_account_name=", ".join(
                                name for name, _, _ in skipped_subtotals_list
                            ),
                            active_leaf_breakdown_accounts=", ".join(
                                f"{name} (Rp {nom:,.0f})"
                                for name, nom, _ in expanded_leaf_terms_list
                            ),
                            diagnostic_audit_notes=partial_skip_notes,
                        )
                    )
                    continue

            # 7. Lump-Sum Aggregate Presentation (Target reported, but all component breakdown items are 0.00)
            if (
                abs(reported_target_balance) > ZERO_THRESHOLD
                and abs(direct_components_sum) <= ZERO_THRESHOLD
            ):
                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=AuditDiscrepancyCategory.LUMP_SUM_AGGREGATE_PRESENTATION,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=direct_components_sum,
                        reconciliation_variance=abs(reported_target_balance),
                        deviation_ratio_percent=100.0,
                        diagnostic_audit_notes="Saldo total dilaporkan pada pos induk, seluruh pos rincian anak bernilai 0.00 (lump-sum agregat)",
                    )
                )
                continue

            # 8. Rounding Variance (<= 1.0% relative tolerance)
            effective_recalculated_total = (
                base_recalculated_components
                if skipped_subtotals_list
                else direct_components_sum
            )
            effective_variance = abs(
                reported_target_balance - effective_recalculated_total
            )
            percentage_deviation = (
                (effective_variance / abs(reported_target_balance)) * 100.0
                if abs(reported_target_balance) > ZERO_THRESHOLD
                else 0.0
            )

            if percentage_deviation <= 1.0:
                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=effective_recalculated_total,
                        reconciliation_variance=effective_variance,
                        deviation_ratio_percent=percentage_deviation,
                        diagnostic_audit_notes=f"Toleransi selisih pembulatan wajar desimal / jutaan rupiah (selisih Rp {effective_variance:,.0f} atau {percentage_deviation:.2f}%)",
                    )
                )
                continue

            # 9. Partial Breakdown Discrepancy (1.0% < deviation < 100%)
            active_components_summary = [
                (acc_name, signed_val)
                for acc_name, signed_val, _ in all_active_terms
                if abs(signed_val) > ZERO_THRESHOLD
            ]
            active_components_strings = [
                f"`{acc_name}` (Rp {signed_val:,.0f})"
                for acc_name, signed_val in active_components_summary
            ]

            if percentage_deviation < 99.99:
                partial_notes = (
                    f"Rincian komponen terisi sebagian: {', '.join(active_components_strings[:2])}"
                    f"{'...' if len(active_components_strings) > 2 else ''} (sisa belum terinci Rp {effective_variance:,.0f} / {percentage_deviation:.1f}%)"
                )
                equation_findings.append(
                    AuditDiscrepancyFinding(
                        entity_ticker=entity_ticker,
                        fiscal_year=fiscal_year,
                        fiscal_period=fiscal_period,
                        equation_identifier=equation_id,
                        category=AuditDiscrepancyCategory.PARTIAL_BREAKDOWN_DISCREPANCY,
                        reported_target_balance=reported_target_balance,
                        recalculated_components_total=effective_recalculated_total,
                        reconciliation_variance=effective_variance,
                        deviation_ratio_percent=percentage_deviation,
                        active_children_count=len(active_components_summary),
                        diagnostic_audit_notes=partial_notes,
                    )
                )
                continue

            # 10. Material Reporting Discrepancy (>= 100% deviation)
            material_notes = (
                f"Diskrepansi nilai (terlapor: {', '.join(active_components_strings[:2])}{'...' if len(active_components_strings) > 2 else ''}; "
                f"selisih Rp {effective_variance:,.0f} / {percentage_deviation:.1f}%)"
                if active_components_summary
                else f"Diskrepansi nilai material (selisih Rp {effective_variance:,.0f})"
            )
            equation_findings.append(
                AuditDiscrepancyFinding(
                    entity_ticker=entity_ticker,
                    fiscal_year=fiscal_year,
                    fiscal_period=fiscal_period,
                    equation_identifier=equation_id,
                    category=AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY,
                    reported_target_balance=reported_target_balance,
                    recalculated_components_total=effective_recalculated_total,
                    reconciliation_variance=effective_variance,
                    deviation_ratio_percent=percentage_deviation,
                    active_children_count=len(active_components_summary),
                    diagnostic_audit_notes=material_notes,
                )
            )

        findings_by_equation[equation_id] = equation_findings

    return findings_by_equation
