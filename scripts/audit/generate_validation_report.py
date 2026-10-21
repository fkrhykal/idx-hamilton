"""Generates executive summary validation report markdown (docs/accounts/equation_validation_report.md).

Decoupled from scratch scripts; consumes production Patito models from:
`idx_hamilton.transformations.reconciliation` and `idx_hamilton.transformations.equations`.
"""

from __future__ import annotations

from collections import Counter

import polars as pl

from idx_hamilton.transformations.equations import (
    ENTRY_POINT_CROSS_EQUATIONS,
    ENTRY_POINT_EQUATIONS,
    AccountingEquationCategory,
    AccountingEquationEngine,
    AccountingEquationSpecification,
)
from idx_hamilton.transformations.reconciliation import (
    AuditDiscrepancyCategory,
    classify_accounting_equation_discrepancies,
)


def format_detail_cell(count_value: int, is_rounding: bool = False) -> str:
    """Formats numeric report count cell with visual badge styling."""
    if count_value == 0:
        return '<span style="color: #94a3b8;">&mdash;</span>'
    if is_rounding:
        return f'<span style="background-color: #f1f5f9; color: #475569; padding: 2px 6px; border-radius: 4px; font-weight: 500;">{count_value:,}</span>'
    return f'<span style="background-color: #fee2e2; color: #991b1b; padding: 2px 6px; border-radius: 4px; font-weight: 600;">{count_value:,}</span>'


def main():
    print("Memindai data Parquet statements...")
    raw_dataframe = (
        pl.scan_parquet(
            ".data/stagings/statements/*/*/*.parquet",
            include_file_paths="file_path",
        )
        .filter(pl.col("value").is_not_null())
        .with_columns(
            entry_point=pl.col("file_path")
            .str.replace_all(r"\\", "/")
            .str.extract(r"statements/([^/]+)/", 1)
        )
        .unique(
            subset=[
                "entry_point",
                "emiten_code",
                "year",
                "period",
                "statement",
                "variant",
                "context",
                "account",
            ],
            keep="first",
        )
        .collect()
    )

    print(f"Data Parquet termuat: {len(raw_dataframe):,} baris fakta.")

    entry_point_counts = (
        raw_dataframe.group_by("entry_point")
        .agg(pl.col("account").n_unique().alias("unique_accounts"))
        .sort("unique_accounts", descending=True)
    )
    ordered_entry_points: list[str] = entry_point_counts["entry_point"].to_list()

    statement_densities = (
        raw_dataframe.group_by(["entry_point", "statement", "variant"])
        .agg(
            [
                pl.col("account").n_unique().alias("unique_accounts"),
                pl.col("emiten_code").n_unique().alias("unique_emitens"),
            ]
        )
        .to_dicts()
    )
    density_map = {
        (item["entry_point"], item["statement"], item["variant"]): (
            item["unique_accounts"],
            item["unique_emitens"],
        )
        for item in statement_densities
    }

    current_period_df = raw_dataframe.filter(
        pl.col("context").str.starts_with("Current")
    )
    evaluation_records: list[dict] = []

    target_statements = [
        "balance_statement",
        "income_statement",
        "cash_flow_statement",
    ]

    for entry_point in ordered_entry_points:
        sector_dict = ENTRY_POINT_EQUATIONS.get(entry_point, {})
        for statement_name in target_statements:
            statement_dict = sector_dict.get(statement_name, {})
            if not statement_dict:
                continue

            sorted_variants = sorted(
                statement_dict.keys(),
                key=lambda v_name: (
                    -density_map.get((entry_point, statement_name, v_name), (0, 0))[0],
                    -density_map.get((entry_point, statement_name, v_name), (0, 0))[1],
                ),
            )

            for variant in sorted_variants:
                equations: tuple[AccountingEquationSpecification, ...] = statement_dict[
                    variant
                ]
                if not equations:
                    continue

                variant_data = current_period_df.filter(
                    (pl.col("entry_point") == entry_point)
                    & (pl.col("statement") == statement_name)
                    & (pl.col("variant") == variant)
                )
                if len(variant_data) == 0:
                    continue

                pivoted_df = variant_data.pivot(
                    index=["emiten_code", "year", "period"],
                    on="account",
                    values="value",
                    aggregate_function="first",
                ).rename({"emiten_code": "ticker"})

                verified_df = AccountingEquationEngine.evaluate_financial_statements(
                    pivoted_df, equations
                )
                findings_by_eq = classify_accounting_equation_discrepancies(
                    verified_df, equations
                )

                total_reports_count = len(verified_df)

                for equation in equations:
                    equation_id = equation.equation_identifier
                    conformance_col = f"is_conformant_{equation_id}"

                    if conformance_col not in verified_df.columns:
                        continue

                    category_counter = Counter(
                        f.category for f in findings_by_eq.get(equation_id, [])
                    )
                    exact_count = category_counter[
                        AuditDiscrepancyCategory.CONFORMANT_EXACT
                    ]
                    rounding_count = category_counter[
                        AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE
                    ]
                    total_conforming_count = exact_count + rounding_count

                    pct_exact = (
                        round(exact_count / total_reports_count * 100.0, 2)
                        if total_reports_count > 0
                        else 0.0
                    )
                    pct_conforming = (
                        round(
                            total_conforming_count / total_reports_count * 100.0,
                            2,
                        )
                        if total_reports_count > 0
                        else 0.0
                    )

                    evaluation_records.append(
                        {
                            "entry_point": entry_point,
                            "statement": statement_name,
                            "variant": variant,
                            "equation_identifier": equation_id,
                            "equation_name": equation.equation_name,
                            "formula_representation": equation.formula_representation,
                            "equation_category": str(equation.equation_category),
                            "target_code": equation.target_account.code,
                            "target_account": equation.target_account.account,
                            "components_count": len(equation.component_terms),
                            "total_reports": total_reports_count,
                            "match_count": exact_count,
                            "pct_match": pct_exact,
                            "match_round_count": total_conforming_count,
                            "pct_match_round": pct_conforming,
                            "count_material_discrepancy": category_counter[
                                AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY
                            ],
                            "count_partial_breakdown": category_counter[
                                AuditDiscrepancyCategory.PARTIAL_BREAKDOWN_DISCREPANCY
                            ],
                            "count_omitted_partial": category_counter[
                                AuditDiscrepancyCategory.OMITTED_PARTIAL_SUBTOTAL
                            ],
                            "count_sign_inversion": category_counter[
                                AuditDiscrepancyCategory.SIGN_INVERSION
                            ],
                            "count_duplicate_entry": category_counter[
                                AuditDiscrepancyCategory.DUPLICATE_LINE_ITEM
                            ],
                            "count_omitted_subtotal": category_counter[
                                AuditDiscrepancyCategory.OMITTED_INTERMEDIATE_SUBTOTAL
                            ],
                            "count_rogue_child": category_counter[
                                AuditDiscrepancyCategory.ROGUE_CHILD_WITHOUT_PARENT
                            ],
                            "count_lump_sum": category_counter[
                                AuditDiscrepancyCategory.LUMP_SUM_AGGREGATE_PRESENTATION
                            ],
                            "count_rounding": rounding_count,
                        }
                    )

    # 2. Evaluasi Cross-Statement Equations
    print("Mengevaluasi artikulasi saldo lintas pernyataan (cross-statement)...")
    cfs_metadata = (
        raw_dataframe.filter(pl.col("statement") == "cash_flow_statement")
        .select(
            [
                "emiten_code",
                "year",
                "period",
                "entry_point",
                pl.col("variant").alias("cfs_variant"),
            ]
        )
        .unique()
    )

    for entry_point in ordered_entry_points:
        cross_sector_dict = ENTRY_POINT_CROSS_EQUATIONS.get(entry_point, {})
        for cfs_variant, cross_equations in cross_sector_dict.items():
            if not cross_equations:
                continue

            sub_metadata = cfs_metadata.filter(
                (pl.col("entry_point") == entry_point)
                & (pl.col("cfs_variant") == cfs_variant)
            )
            if len(sub_metadata) == 0:
                continue

            cross_raw = (
                raw_dataframe.filter(pl.col("entry_point") == entry_point)
                .join(
                    sub_metadata.select(["emiten_code", "year", "period"]),
                    on=["emiten_code", "year", "period"],
                    how="inner",
                )
                .with_columns(
                    column_id=pl.concat_str(
                        [
                            pl.col("statement"),
                            pl.lit("__"),
                            pl.col("context"),
                            pl.lit("__"),
                            pl.col("account"),
                        ]
                    )
                )
            )

            cross_pivoted_df = cross_raw.pivot(
                index=["emiten_code", "year", "period"],
                on="column_id",
                values="value",
                aggregate_function="first",
            ).rename({"emiten_code": "ticker"})

            cross_verified_df = AccountingEquationEngine.evaluate_financial_statements(
                cross_pivoted_df, cross_equations
            )
            cross_findings_by_eq = classify_accounting_equation_discrepancies(
                cross_verified_df, cross_equations
            )

            tot_reports = len(cross_verified_df)

            for equation in cross_equations:
                eq_id = equation.equation_identifier
                conformance_col = f"is_conformant_{eq_id}"

                if conformance_col not in cross_verified_df.columns:
                    continue

                category_counter = Counter(
                    f.category for f in cross_findings_by_eq.get(eq_id, [])
                )
                exact_count = category_counter[
                    AuditDiscrepancyCategory.CONFORMANT_EXACT
                ]
                rounding_count = category_counter[
                    AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE
                ]
                total_conforming_count = exact_count + rounding_count

                pct_exact = (
                    round(exact_count / tot_reports * 100.0, 2)
                    if tot_reports > 0
                    else 0.0
                )
                pct_conforming = (
                    round(total_conforming_count / tot_reports * 100.0, 2)
                    if tot_reports > 0
                    else 0.0
                )

                evaluation_records.append(
                    {
                        "entry_point": entry_point,
                        "statement": "cross_statement",
                        "variant": cfs_variant,
                        "equation_identifier": eq_id,
                        "equation_name": equation.equation_name,
                        "formula_representation": equation.formula_representation,
                        "equation_category": str(equation.equation_category),
                        "target_code": equation.target_account.code,
                        "target_account": equation.target_account.account,
                        "components_count": len(equation.component_terms),
                        "total_reports": tot_reports,
                        "match_count": exact_count,
                        "pct_match": pct_exact,
                        "match_round_count": total_conforming_count,
                        "pct_match_round": pct_conforming,
                        "count_material_discrepancy": category_counter[
                            AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY
                        ],
                        "count_partial_breakdown": category_counter[
                            AuditDiscrepancyCategory.PARTIAL_BREAKDOWN_DISCREPANCY
                        ],
                        "count_omitted_partial": category_counter[
                            AuditDiscrepancyCategory.OMITTED_PARTIAL_SUBTOTAL
                        ],
                        "count_sign_inversion": category_counter[
                            AuditDiscrepancyCategory.SIGN_INVERSION
                        ],
                        "count_duplicate_entry": category_counter[
                            AuditDiscrepancyCategory.DUPLICATE_LINE_ITEM
                        ],
                        "count_omitted_subtotal": category_counter[
                            AuditDiscrepancyCategory.OMITTED_INTERMEDIATE_SUBTOTAL
                        ],
                        "count_rogue_child": category_counter[
                            AuditDiscrepancyCategory.ROGUE_CHILD_WITHOUT_PARENT
                        ],
                        "count_lump_sum": category_counter[
                            AuditDiscrepancyCategory.LUMP_SUM_AGGREGATE_PRESENTATION
                        ],
                        "count_rounding": rounding_count,
                    }
                )

    df_eval = pl.DataFrame(evaluation_records)
    print(f"Selesai evaluasi {len(df_eval)} keterhubungan akun.")

    total_checks = len(df_eval)
    perfect_exact_count = df_eval.filter(
        pl.col("match_count") == pl.col("total_reports")
    ).shape[0]
    reliable_exact_count = df_eval.filter(
        (pl.col("pct_match") >= 95.0)
        & (pl.col("match_count") < pl.col("total_reports"))
    ).shape[0]
    attention_exact_count = df_eval.filter(pl.col("pct_match") < 95.0).shape[0]

    perfect_conforming_count = df_eval.filter(
        pl.col("match_round_count") == pl.col("total_reports")
    ).shape[0]
    reliable_conforming_count = df_eval.filter(
        (pl.col("pct_match_round") >= 95.0)
        & (pl.col("match_round_count") < pl.col("total_reports"))
    ).shape[0]
    attention_conforming_count = df_eval.filter(pl.col("pct_match_round") < 95.0).shape[
        0
    ]

    horiz_df = df_eval.filter(
        pl.col("equation_category")
        == AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY.value
    )
    rollup_df = df_eval.filter(
        pl.col("equation_category")
        == AccountingEquationCategory.VERTICAL_AGGREGATION.value
    )
    cross_df = df_eval.filter(
        pl.col("equation_category")
        == AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION.value
    )

    horiz_round_perfect = horiz_df.filter(
        pl.col("match_round_count") == pl.col("total_reports")
    ).shape[0]
    horiz_round_reliable = horiz_df.filter(
        (pl.col("pct_match_round") >= 95.0)
        & (pl.col("match_round_count") < pl.col("total_reports"))
    ).shape[0]
    horiz_round_attention = horiz_df.filter(pl.col("pct_match_round") < 95.0).shape[0]

    rollup_round_perfect = rollup_df.filter(
        pl.col("match_round_count") == pl.col("total_reports")
    ).shape[0]
    rollup_round_reliable = rollup_df.filter(
        (pl.col("pct_match_round") >= 95.0)
        & (pl.col("match_round_count") < pl.col("total_reports"))
    ).shape[0]
    rollup_round_attention = rollup_df.filter(pl.col("pct_match_round") < 95.0).shape[0]

    cross_round_perfect = cross_df.filter(
        pl.col("match_round_count") == pl.col("total_reports")
    ).shape[0]
    cross_round_reliable = cross_df.filter(
        (pl.col("pct_match_round") >= 95.0)
        & (pl.col("match_round_count") < pl.col("total_reports"))
    ).shape[0]
    cross_round_attention = cross_df.filter(pl.col("pct_match_round") < 95.0).shape[0]

    BADGE_PERFECT = '<span style="background-color: #dcfce7; color: #166534; padding: 2px 7px; border-radius: 4px; font-size: 0.85em;">[KONSISTEN 100%]</span>'
    BADGE_RELIABLE = '<span style="background-color: #e0f2fe; color: #075985; padding: 2px 7px; border-radius: 4px; font-size: 0.85em;">[ANDAL &ge;95%]</span>'
    BADGE_ATTENTION = '<span style="background-color: #fef9c3; color: #854d0e; padding: 2px 7px; border-radius: 4px; font-size: 0.85em;">[PERHATIAN &lt;95%]</span>'

    BADGE_HORIZ = '<span style="background-color: #ede9fe; color: #5b21b6; padding: 2px 6px; border-radius: 4px; font-size: 0.82em;">Keseimbangan Makro</span>'
    BADGE_VERT = '<span style="background-color: #f1f5f9; color: #334155; padding: 2px 6px; border-radius: 4px; font-size: 0.82em;">Penjumlahan Rincian</span>'
    BADGE_CROSS = '<span style="background-color: #fef3c7; color: #92400e; padding: 2px 6px; border-radius: 4px; font-size: 0.82em;">Artikulasi Lintas Laporan</span>'

    def make_conformance_badge(acc_val: float, match_c: int, tot_reports: int) -> str:
        if match_c == tot_reports:
            return f'<span style="background-color: #dcfce7; color: #166534; padding: 2px 7px; border-radius: 4px; font-size: 0.88em;">{acc_val:.2f}%</span>'
        elif acc_val >= 95.0:
            return f'<span style="background-color: #e0f2fe; color: #075985; padding: 2px 7px; border-radius: 4px; font-size: 0.88em;">{acc_val:.2f}%</span>'
        return f'<span style="background-color: #fef9c3; color: #854d0e; padding: 2px 7px; border-radius: 4px; font-size: 0.88em;">{acc_val:.2f}%</span>'

    markdown_lines = [
        "# Laporan Hasil Validasi Keterhubungan Saldo Laporan Keuangan IDX\n\n",
        "> Dokumen ini memuat hasil pengujian keterhubungan aljabar dan konsistensi saldo laporan keuangan lintas *entry point*, *statement*, dan *variant*. Pengujian mengevaluasi keseimbangan makro (keseimbangan Aset = Liabilitas + Ekuitas), penjumlahan rincian pos anak ke pos induk (*vertical rollup*), serta artikulasi konsistensi saldo antar-laporan keuangan pada pelaporan iXBRL BEI (2020–2025).\n\n",
        """<style>
table {
    display: block;
    width: 100%;
    max-height: 480px;
    overflow-x: auto;
    overflow-y: auto;
}
th {
    position: sticky;
    top: 0;
    background-color: #f8fafc;
    z-index: 2;
}
@media (prefers-color-scheme: dark) {
    th {
        background-color: #1e293b;
    }
}
th, td {
    white-space: nowrap;
}
table.diagnostic-table {
    display: table !important;
    width: 100% !important;
    max-height: none !important;
    overflow-y: visible !important;
}
table.diagnostic-table th, table.diagnostic-table td {
    white-space: normal !important;
    word-break: normal !important;
    position: static !important;
}
</style>
""",
        "## Ringkasan Eksekutif Validasi Keterhubungan Saldo\n\n",
        "### Perbandingan Evaluasi: Keseimbangan Eksak vs Toleransi Pembulatan (&le; 1.0%)\n\n",
        "| Tingkat Konsistensi Saldo | Evaluasi Eksak (0 Rupiah) | Evaluasi Toleransi Pembulatan (&le; 1.0%) | Kenaikan Bersih | Karakteristik Kualitas Pelaporan |\n",
        "| :--- | :---: | :---: | :---: | :--- |\n",
        f"| {BADGE_PERFECT} | {perfect_exact_count} ({perfect_exact_count / total_checks * 100:.2f}%) | {perfect_conforming_count} ({perfect_conforming_count / total_checks * 100:.2f}%) | +{perfect_conforming_count - perfect_exact_count} persamaan | Seluruh laporan emiten seimbang sempurna tanpa selisih material |\n",
        f"| {BADGE_RELIABLE} | {reliable_exact_count} ({reliable_exact_count / total_checks * 100:.2f}%) | {reliable_conforming_count} ({reliable_conforming_count / total_checks * 100:.2f}%) | {reliable_conforming_count - reliable_exact_count} persamaan | Struktur baku sangat andal; selisih minor wajar akibat gaya pelaporan emiten |\n",
        f"| {BADGE_ATTENTION} | {attention_exact_count} ({attention_exact_count / total_checks * 100:.2f}%) | {attention_conforming_count} ({attention_conforming_count / total_checks * 100:.2f}%) | {attention_conforming_count - attention_exact_count} persamaan | Pelaporan agregat tanpa rincian, restricted cash, atau perbedaan taksonomi industri |\n",
        f"| Total Pengujian Akun | {total_checks} (100.00%) | {total_checks} (100.00%) | &mdash; | Seluruh keterhubungan akun lintas 8 entry point sektor industri |\n\n",
        "### Rincian Keandalan per Tipe Keterhubungan Saldo\n\n",
        "| Kategori Keterhubungan Akun | Total Persamaan | Konsisten 100% (+Pembulatan) | Andal &ge;95% (+Pembulatan) | Perhatian &lt;95% | Rasio Keandalan Total (&ge;95%) |\n",
        "| :--- | :---: | :---: | :---: | :---: | :---: |\n",
        f"| {BADGE_HORIZ} | {len(horiz_df)} | {horiz_round_perfect} ({horiz_round_perfect / len(horiz_df) * 100:.2f}%) | {horiz_round_reliable} ({horiz_round_reliable / len(horiz_df) * 100:.2f}%) | {horiz_round_attention} ({horiz_round_attention / len(horiz_df) * 100:.2f}%) | {(horiz_round_perfect + horiz_round_reliable) / len(horiz_df) * 100:.2f}% |\n",
        f"| {BADGE_VERT} | {len(rollup_df)} | {rollup_round_perfect} ({rollup_round_perfect / len(rollup_df) * 100:.2f}%) | {rollup_round_reliable} ({rollup_round_reliable / len(rollup_df) * 100:.2f}%) | {rollup_round_attention} ({rollup_round_attention / len(rollup_df) * 100:.2f}%) | {(rollup_round_perfect + rollup_round_reliable) / len(rollup_df) * 100:.2f}% |\n",
        f"| {BADGE_CROSS} | {len(cross_df)} | {cross_round_perfect} ({cross_round_perfect / len(cross_df) * 100:.2f}%) | {cross_round_reliable} ({cross_round_reliable / len(cross_df) * 100:.2f}%) | {cross_round_attention} ({cross_round_attention / len(cross_df) * 100:.2f}%) | {(cross_round_perfect + cross_round_reliable) / len(cross_df) * 100:.2f}% |\n",
        f"| Total Seluruh Keterhubungan | {total_checks} | {perfect_conforming_count} ({perfect_conforming_count / total_checks * 100:.2f}%) | {reliable_conforming_count} ({reliable_conforming_count / total_checks * 100:.2f}%) | {attention_conforming_count} ({attention_conforming_count / total_checks * 100:.2f}%) | {(perfect_conforming_count + reliable_conforming_count) / total_checks * 100:.2f}% |\n\n",
        "### Daftar Sektor Berdasarkan Kelengkapan Taksonomi Akun\n\n",
        "> Rekapitulasi pos akun unik pada taksonomi iXBRL BEI per sektor industri (disajikan terurut dari jumlah akun terbanyak).\n\n",
        "| Sektor Industri (`entry_point`) | Jumlah Akun Unik | Total Emiten | Fakta Dilaporkan | Karakteristik Pelaporan Sektor |\n",
        "| :--- | :---: | :---: | :---: | :--- |\n",
    ]

    sector_descriptions = {
        "general": "Sektor manufaktur, perdagangan, jasa & konsumer; cakupan emiten terbesar di BEI.",
        "infrastructure": "Sektor infrastruktur, utilitas & telekomunikasi.",
        "financial_and_sharia": "Perbankan konvensional dan syariah.",
        "property": "Properti, perumahan dan real estat.",
        "financing": "Lembaga pembiayaan dan multifinance.",
        "securities": "Perusahaan sekuritas dan perantara efek.",
        "insurance": "Perusahaan asuransi jiwa dan umum.",
        "collective_investment_contract": "Kontrak investasi kolektif (KIK-EBA / KIK-DIRE).",
    }

    for entry_point in ordered_entry_points:
        sub_ep = raw_dataframe.filter(pl.col("entry_point") == entry_point)
        unique_accounts = sub_ep["account"].n_unique()
        unique_emitens = sub_ep["emiten_code"].n_unique()
        total_facts = len(sub_ep)
        desc = sector_descriptions.get(
            entry_point, "Sektor industri pasar modal Indonesia."
        )
        markdown_lines.append(
            f"| `{entry_point}` | {unique_accounts:,} akun | {unique_emitens:,} emiten | {total_facts:,} | {desc} |\n"
        )

    markdown_lines.append("\n")
    markdown_lines.append("## Daftar Isi Laporan Validasi\n\n")
    markdown_lines.append(
        "- [Laporan Posisi Keuangan (Balance Statement)](#laporan-posisi-keuangan-balance-statement)\n"
    )
    markdown_lines.append(
        "- [Laporan Laba Rugi dan Penghasilan Komprehensif Lain (Income Statement)](#laporan-laba-rugi-dan-penghasilan-komprehensif-lain-income-statement)\n"
    )
    markdown_lines.append(
        "- [Laporan Arus Kas (Cash Flow Statement)](#laporan-arus-kas-cash-flow-statement)\n"
    )
    markdown_lines.append(
        "- [Artikulasi Saldo Lintas Laporan (Inter-Statement Articulation)](#artikulasi-saldo-lintas-laporan-inter-statement-articulation)\n\n"
    )

    target_statement_sections = [
        ("balance_statement", "Laporan Posisi Keuangan (Balance Statement)"),
        (
            "income_statement",
            "Laporan Laba Rugi dan Penghasilan Komprehensif Lain (Income Statement)",
        ),
        ("cash_flow_statement", "Laporan Arus Kas (Cash Flow Statement)"),
    ]

    for statement_name, statement_label in target_statement_sections:
        markdown_lines.append(f"## {statement_label}\n\n")

        for entry_point in ordered_entry_points:
            sector_dict = ENTRY_POINT_EQUATIONS.get(entry_point, {}).get(
                statement_name, {}
            )
            if not sector_dict:
                continue

            sorted_variants = sorted(
                sector_dict.keys(),
                key=lambda var_name: (
                    -density_map.get((entry_point, statement_name, var_name), (0, 0))[
                        0
                    ],
                    -density_map.get((entry_point, statement_name, var_name), (0, 0))[
                        1
                    ],
                ),
            )

            for variant in sorted_variants:
                sub_eval = df_eval.filter(
                    (pl.col("entry_point") == entry_point)
                    & (pl.col("statement") == statement_name)
                    & (pl.col("variant") == variant)
                )
                if len(sub_eval) == 0:
                    continue

                markdown_lines.append(f"### `{entry_point}` &mdash; `{variant}`\n\n")
                markdown_lines.append(
                    "| Status | Formula Persamaan | Akun Sasaran Terlapor | Keseimbangan (Eksak) | Keseimbangan (+Pembulatan) | Rasio Lolos (+Pembulatan) | Duplikasi Pos | Inversi (+/-) | Omisi Subtotal | Omisi Sebagian | Tanpa Induk | Lump-Sum | Pembulatan | Rincian Terisi | Diskrepansi Lain |\n"
                )
                markdown_lines.append(
                    "| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
                )

                for row in sub_eval.iter_rows(named=True):
                    exact_badge = make_conformance_badge(
                        row["pct_match"],
                        row["match_count"],
                        row["total_reports"],
                    )
                    round_badge = make_conformance_badge(
                        row["pct_match_round"],
                        row["match_round_count"],
                        row["total_reports"],
                    )
                    if row["count_rounding"] > 0:
                        ratio_str = f"{row['match_count']:,} (+{row['count_rounding']:,}) / {row['total_reports']:,}"
                    else:
                        ratio_str = f"{row['match_count']:,} / {row['total_reports']:,}"

                    type_badge = (
                        BADGE_HORIZ
                        if row["equation_category"]
                        == AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY.value
                        else BADGE_VERT
                    )
                    formula_str = row["formula_representation"]
                    target_str = f"`[{row['target_code']}]` `{row['target_account']}`"

                    dup_str = format_detail_cell(row["count_duplicate_entry"])
                    sign_str = format_detail_cell(row["count_sign_inversion"])
                    subtotal_str = format_detail_cell(row["count_omitted_subtotal"])
                    skip_part_str = format_detail_cell(row["count_omitted_partial"])
                    rogue_str = format_detail_cell(row["count_rogue_child"])
                    lump_str = format_detail_cell(row["count_lump_sum"])
                    round_str = format_detail_cell(
                        row["count_rounding"], is_rounding=True
                    )
                    part_str = format_detail_cell(row["count_partial_breakdown"])
                    discrepancy_str = format_detail_cell(
                        row["count_material_discrepancy"]
                    )

                    markdown_lines.append(
                        f"| {type_badge} | <code>{formula_str}</code> | {target_str} | {exact_badge} | {round_badge} | {ratio_str} | {dup_str} | {sign_str} | {subtotal_str} | {skip_part_str} | {rogue_str} | {lump_str} | {round_str} | {part_str} | {discrepancy_str} |\n"
                    )

                markdown_lines.append("\n")

        markdown_lines.append(
            '<hr style="border: none; border-top: 4px double #64748b; margin: 48px 0;" />\n\n'
        )

    # 4. Artikulasi Lintas Laporan
    markdown_lines.append(
        "## Artikulasi Saldo Lintas Laporan (Inter-Statement Articulation)\n\n"
    )
    markdown_lines.append(
        "> Bagian ini memuat evaluasi keterkaitan antar-laporan keuangan (*inter-statement articulation*) periode berjalan (*Current Period*).\n\n"
    )
    markdown_lines.append(
        "### Panduan Formula Artikulasi Lintas Laporan per Sektor\n\n"
    )
    markdown_lines.append(
        """<table class="diagnostic-table" style="display: table !important; width: 100% !important;">
  <thead>
    <tr>
      <th width="5%">No</th>
      <th width="35%">Formula Artikulasi Saldo</th>
      <th width="25%">Penjelasan Akuntansi &amp; Sektor Berlaku</th>
      <th width="35%">Komponen &amp; Pemetaan Akun Riil IDX</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>1</b></td>
      <td><code>[BS.CASH] == [CFS.CASH.END]</code></td>
      <td><b>Artikulasi Kas Akhir Neraca &amp; Arus Kas Sektor Non-Keuangan</b><br>Berlaku untuk sektor umum, properti, infrastruktur, sekuritas, dan asuransi. Keduanya berkonteks <code>CurrentYearInstant</code>.</td>
      <td>&bull; <code>[BS.CASH]</code>: <i>balance_statement</i> &rarr; <code>CurrentYearInstant</code> &rarr; <code>CashAndCashEquivalents</code><br>&bull; <code>[CFS.CASH.END]</code>: <i>cash_flow_statement</i> &rarr; <code>CurrentYearInstant</code> &rarr; <code>CashAndCashEquivalentsCashFlows</code></td>
    </tr>
    <tr>
      <td align="center"><b>2</b></td>
      <td><code>[CFS.CASH.END] == [BS.CASH] + [BS.CA.BI] + [BS.CA.OB_TP] + [BS.CA.OB_RP] + [BS.PL.BI_TP] + [BS.PL.BI_RP]</code></td>
      <td><b>Artikulasi Kas Akhir Lembaga Pembiayaan</b><br>Berlaku khusus untuk <code>financing</code> (multifinance). Menggabungkan kas fisik, giro BI, giro bank lain (pihak ketiga &amp; berelasi), dan penempatan BI/bank lain di neraca terhadap kas akhir arus kas.</td>
      <td>&bull; <code>[CFS.CASH.END]</code>: <i>cash_flow_statement</i> &rarr; <code>CurrentYearInstant</code> &rarr; <code>CashAndCashEquivalentsCashFlows</code><br>&bull; <code>[BS.CASH]</code>: <i>balance_statement</i> &rarr; <code>CashAndCashEquivalents</code><br>&bull; <code>[BS.CA.BI]</code>: <i>balance_statement</i> &rarr; <code>CurrentAccountsWithBankIndonesia</code><br>&bull; <code>[BS.CA.OB_TP]</code> &amp; <code>[BS.CA.OB_RP]</code>: <i>balance_statement</i> &rarr; <code>CurrentAccountsWithOtherBanks...</code><br>&bull; <code>[BS.PL.BI_TP]</code> &amp; <code>[BS.PL.BI_RP]</code>: <i>balance_statement</i> &rarr; <code>PlacementsWithBankIndonesiaAndOtherBanks...</code></td>
    </tr>
    <tr>
      <td align="center"><b>3</b></td>
      <td><code>[CFS.CASH.END] == [BS.BANK.CASH] + [BS.CA.BI] + [BS.CA.OB_TP] + [BS.CA.OB_RP] + [BS.PL.BI_TP] + [BS.PL.BI_RP]</code></td>
      <td><b>Artikulasi Kas Akhir Perbankan</b><br>Berlaku khusus untuk <code>financial_and_sharia</code> (bank). Menghubungkan kas fisik bank, giro BI, giro bank lain, dan penempatan antarbank terhadap kas akhir arus kas.</td>
      <td>&bull; <code>[CFS.CASH.END]</code>: <i>cash_flow_statement</i> &rarr; <code>CurrentYearInstant</code> &rarr; <code>CashAndCashEquivalentsCashFlows</code><br>&bull; <code>[BS.BANK.CASH]</code>: <i>balance_statement</i> &rarr; <code>Cash</code><br>&bull; <code>[BS.CA.BI]</code>: <i>balance_statement</i> &rarr; <code>CurrentAccountsWithBankIndonesia</code><br>&bull; <code>[BS.CA.OB_TP]</code> &amp; <code>[BS.CA.OB_RP]</code>: <i>balance_statement</i> &rarr; <code>CurrentAccountsWithOtherBanks...</code><br>&bull; <code>[BS.PL.BI_TP]</code> &amp; <code>[BS.PL.BI_RP]</code>: <i>balance_statement</i> &rarr; <code>PlacementsWithBankIndonesiaAndOtherBanks...</code></td>
    </tr>
    <tr>
      <td align="center"><b>4</b></td>
      <td><code>[IS.PL] == [CFS.PL]</code></td>
      <td><b>Artikulasi Laba Bersih Metode Tidak Langsung</b><br>Hanya dievaluasi pada varian <code>indirect_method</code>. Laba bersih tahun berjalan pada laporan laba rugi menjadi titik awal rekonsiliasi arus kas aktivitas operasi. Keduanya berkonteks <code>CurrentYearDuration</code>.</td>
      <td>&bull; <code>[IS.PL]</code>: <i>income_statement</i> &rarr; <code>CurrentYearDuration</code> &rarr; <code>ProfitLoss</code><br>&bull; <code>[CFS.PL]</code>: <i>cash_flow_statement</i> &rarr; <code>CurrentYearDuration</code> &rarr; <code>ProfitLoss</code></td>
    </tr>
  </tbody>
</table>
"""
    )

    cross_eval_df = df_eval.filter(pl.col("statement") == "cross_statement")
    raw_cross_groups = (
        cross_eval_df.select(["entry_point", "variant"]).unique().to_dicts()
    )
    cross_groups = sorted(
        raw_cross_groups,
        key=lambda g: (
            (
                ordered_entry_points.index(g["entry_point"])
                if g["entry_point"] in ordered_entry_points
                else 999
            ),
            -density_map.get(
                (g["entry_point"], "cash_flow_statement", g["variant"]), (0, 0)
            )[0],
        ),
    )

    for group in cross_groups:
        entry_point = group["entry_point"]
        variant = group["variant"]
        sub_cross = cross_eval_df.filter(
            (pl.col("entry_point") == entry_point) & (pl.col("variant") == variant)
        )
        if len(sub_cross) == 0:
            continue

        markdown_lines.append(f"### `{entry_point}` &mdash; `{variant}`\n\n")
        markdown_lines.append(
            "| Status | Formula Persamaan | Akun Sasaran Terlapor | Keseimbangan (Eksak) | Keseimbangan (+Pembulatan) | Rasio Lolos (+Pembulatan) | Duplikasi Pos | Inversi (+/-) | Omisi Subtotal | Omisi Sebagian | Tanpa Induk | Lump-Sum | Pembulatan | Rincian Terisi | Diskrepansi Lain |\n"
        )
        markdown_lines.append(
            "| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
        )

        for row in sub_cross.iter_rows(named=True):
            exact_badge = make_conformance_badge(
                row["pct_match"], row["match_count"], row["total_reports"]
            )
            round_badge = make_conformance_badge(
                row["pct_match_round"],
                row["match_round_count"],
                row["total_reports"],
            )
            if row["count_rounding"] > 0:
                ratio_str = f"{row['match_count']:,} (+{row['count_rounding']:,}) / {row['total_reports']:,}"
            else:
                ratio_str = f"{row['match_count']:,} / {row['total_reports']:,}"

            type_badge = BADGE_CROSS
            formula_str = row["formula_representation"]
            target_str = f"`[{row['target_code']}]` `{row['target_account']}`"

            dup_str = format_detail_cell(row["count_duplicate_entry"])
            sign_str = format_detail_cell(row["count_sign_inversion"])
            subtotal_str = format_detail_cell(row["count_omitted_subtotal"])
            skip_part_str = format_detail_cell(row["count_omitted_partial"])
            rogue_str = format_detail_cell(row["count_rogue_child"])
            lump_str = format_detail_cell(row["count_lump_sum"])
            round_str = format_detail_cell(row["count_rounding"], is_rounding=True)
            part_str = format_detail_cell(row["count_partial_breakdown"])
            discrepancy_str = format_detail_cell(row["count_material_discrepancy"])

            markdown_lines.append(
                f"| {type_badge} | <code>{formula_str}</code> | {target_str} | {exact_badge} | {round_badge} | {ratio_str} | {dup_str} | {sign_str} | {subtotal_str} | {skip_part_str} | {rogue_str} | {lump_str} | {round_str} | {part_str} | {discrepancy_str} |\n"
            )

        markdown_lines.append("\n")

    output_path = "docs/accounts/equation_validation_report.md"
    clean_lines = [
        line if line.endswith("\n") else f"{line}\n" for line in markdown_lines
    ]
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(clean_lines)

    print(f"Laporan berhasil dibuat di {output_path} ({len(markdown_lines)} baris).")


if __name__ == "__main__":
    main()
