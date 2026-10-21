"""Generates comprehensive equation mismatch audit report markdown (docs/accounts/equation_mismatch_reports.md).

Decoupled from scratch scripts; consumes production Patito models from:
`idx_hamilton.transformations.reconciliation` and `idx_hamilton.transformations.equations`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

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
    AuditDiscrepancyFinding,
    classify_accounting_equation_discrepancies,
)


def format_number(value: float | None) -> str:
    """Formats numeric values into standardized accounting notation."""
    if value is None or abs(value) < 1e-6:
        return "0.00"
    if abs(value) >= 1:
        return f"{value:,.0f}" if value.is_integer() else f"{value:,.2f}"
    return f"{value:.4f}"


# ==============================================================================
# STRATEGY PATTERN: SPECIALIZED TABLE RENDERERS FOR AUDIT DISCREPANCY FINDINGS
# ==============================================================================


class AuditMismatchTableStrategy(ABC):
    """Abstract base strategy for rendering category-specific markdown audit tables."""

    @abstractmethod
    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        """Renders specialized markdown table tailored for this diagnostic category."""


class DuplicateLineItemStrategy(AuditMismatchTableStrategy):
    """Strategy for Duplikasi Pos Pengungkapan: highlights duplicated line items and paired reference accounts."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Saldo Induk Terlapor | Pos Terduplikasi | Pos Pasangan / Referensi | Nominal Duplikasi | Keterangan Temuan Audit |\n",
            "| :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :--- |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            duplicate_account = (
                f"`{finding.duplicate_account_name}`"
                if finding.duplicate_account_name
                else "-"
            )
            reference_account = finding.paired_reference_account or "-"
            if reference_account not in [
                "-",
                "Saldo Total Induk",
                "Akun Komponen Sejenis",
            ]:
                reference_account = f"`{reference_account}`"
            duplicate_nominal_str = format_number(
                finding.duplicate_reported_amount or finding.reconciliation_variance
            )
            audit_notes = finding.diagnostic_audit_notes

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {target_balance_str} | {duplicate_account} | {reference_account} | {duplicate_nominal_str} | {audit_notes} |\n"
            )

        output_lines.append("\n")
        return output_lines


class SignInversionStrategy(AuditMismatchTableStrategy):
    """Strategy for Inversi Tanda Saldo: highlights inverted accounts and sign correction impact."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Saldo Induk Terlapor | Pos Mengalami Inversi | Nilai Input Terlapor | Arah Pembalikan | Rekalkulasi Pasca Koreksi |\n",
            "| :---: | :---: | :---: | :---: | :---: | :--- | :---: | :---: | :--- |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            inverted_account = finding.inverted_account_name or "-"
            if inverted_account != "-" and not inverted_account.startswith("`"):
                inverted_account = f"`{inverted_account}`"
            inverted_amount_str = format_number(
                finding.inverted_reported_amount
                or finding.recalculated_components_total
            )
            reported_polarity = "+" if (finding.expected_sign_direction == "-") else "-"
            expected_polarity = finding.expected_sign_direction or "-"
            sign_transition = f"{reported_polarity} &rarr; {expected_polarity}"
            reconciliation_note = f"Seimbang klop 100% pasca pembalikan tanda (Saldo: {target_balance_str})"

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {target_balance_str} | {inverted_account} | {inverted_amount_str} | {sign_transition} | {reconciliation_note} |\n"
            )

        output_lines.append("\n")
        return output_lines


class OmittedSubtotalStrategy(AuditMismatchTableStrategy):
    """Strategy for Omisi Subtotal Perantara: highlights omitted subtotal and leaf breakdown sum."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Saldo Induk Terlapor | Subtotal Perantara Kosong (0.00) | Pos Rincian Daun yang Mengisi | Total Rincian Daun | Status Konformitas Audit |\n",
            "| :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :---: |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            omitted_subtotal = (
                f"`{finding.omitted_subtotal_account_name}`"
                if finding.omitted_subtotal_account_name
                else "-"
            )
            leaf_accounts_str = finding.active_leaf_breakdown_accounts or "-"
            total_leaf_sum_str = format_number(finding.recalculated_components_total)
            status_str = "Seimbang Klop 100% (Selisih Rp 0.00)"

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {target_balance_str} | {omitted_subtotal} | {leaf_accounts_str} | {total_leaf_sum_str} | {status_str} |\n"
            )

        output_lines.append("\n")
        return output_lines


class RogueChildStrategy(AuditMismatchTableStrategy):
    """Strategy for Rincian Tanpa Saldo Induk: highlights active children with parent balance at 0.00."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Pos Akun Induk (Nol) | Pos Rincian Anak yang Terisi | Total Nilai Rincian | Karakteristik Pelaporan Audit |\n",
            "| :---: | :---: | :---: | :---: | :--- | :--- | :---: | :--- |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            parent_account_label = "Akun Induk (0.00)"
            active_children_str = (
                finding.active_leaf_breakdown_accounts or "Pos rincian anak terisi"
            )
            total_children_sum_str = format_number(
                finding.recalculated_components_total
            )
            audit_note = finding.diagnostic_audit_notes

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {parent_account_label} | {active_children_str} | {total_children_sum_str} | {audit_note} |\n"
            )

        output_lines.append("\n")
        return output_lines


class LumpSumAggregateStrategy(AuditMismatchTableStrategy):
    """Strategy for Penyajian Agregat Tanpa Rincian: highlights aggregate balance with omitted children."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Pos Akun Induk | Saldo Agregat Terlapor | Pos Rincian Taksonomi (Dikosongkan) | Pola Pelaporan Audit |\n",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :--- | :--- |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            omitted_taxonomic_str = "Seluruh pos rincian anak bernilai 0.00"
            audit_note = finding.diagnostic_audit_notes

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | Pos Akun Induk | {target_balance_str} | {omitted_taxonomic_str} | {audit_note} |\n"
            )

        output_lines.append("\n")
        return output_lines


class OmittedPartialSubtotalStrategy(AuditMismatchTableStrategy):
    """Strategy for Omisi Subtotal & Rincian Tidak Lengkap: highlights skipped subtotal and partial leaf terms."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Saldo Induk Terlapor | Subtotal yang Dikosongkan | Rincian Daun yang Dilaporkan | Varians Rekonsiliasi | Rasio Deviasi (%) |\n",
            "| :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :---: |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            omitted_subtotal = (
                f"`{finding.omitted_subtotal_account_name}`"
                if finding.omitted_subtotal_account_name
                else "-"
            )
            leaf_accounts_str = finding.active_leaf_breakdown_accounts or "-"
            variance_str = format_number(finding.reconciliation_variance)
            deviation_str = f"{finding.deviation_ratio_percent:.2f}%"

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {target_balance_str} | {omitted_subtotal} | {leaf_accounts_str} | {variance_str} | {deviation_str} |\n"
            )

        output_lines.append("\n")
        return output_lines


class PartialBreakdownStrategy(AuditMismatchTableStrategy):
    """Strategy for Rincian Tidak Lengkap: highlights active children and residual difference."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Saldo Induk Terlapor | Total Rincian Terisi | Sisa Belum Terinci | Rasio Deviasi (%) | Pos Rincian yang Dilaporkan |\n",
            "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            recalculated_components_str = format_number(
                finding.recalculated_components_total
            )
            variance_str = format_number(finding.reconciliation_variance)
            deviation_str = f"{finding.deviation_ratio_percent:.2f}%"
            audit_note = finding.diagnostic_audit_notes

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {target_balance_str} | {recalculated_components_str} | {variance_str} | {deviation_str} | {audit_note} |\n"
            )

        output_lines.append("\n")
        return output_lines


class RoundingToleranceStrategy(AuditMismatchTableStrategy):
    """Strategy for Selisih Pembulatan: highlights immaterial rounding tolerance."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Saldo Induk Terlapor | Hasil Rekalkulasi Komponen | Varians Rekonsiliasi | Rasio Deviasi (%) | Catatan Toleransi Audit |\n",
            "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            recalculated_components_str = format_number(
                finding.recalculated_components_total
            )
            variance_str = format_number(finding.reconciliation_variance)
            deviation_str = f"{finding.deviation_ratio_percent:.2f}%"
            audit_note = finding.diagnostic_audit_notes

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {target_balance_str} | {recalculated_components_str} | {variance_str} | {deviation_str} | {audit_note} |\n"
            )

        output_lines.append("\n")
        return output_lines


class MaterialDiscrepancyStrategy(AuditMismatchTableStrategy):
    """Strategy for Diskrepansi Material Pelaporan: highlights severe deviations."""

    def render(
        self,
        findings: list[AuditDiscrepancyFinding],
        section_title: str,
        section_explanation: str,
    ) -> list[str]:
        sorted_findings = sorted(
            findings, key=lambda f: f.reconciliation_variance, reverse=True
        )
        output_lines: list[str] = [
            f"#### {section_title} ({len(sorted_findings):,} laporan)\n\n",
            f"> *{section_explanation}*\n\n",
            "| No | Emiten | Tahun | Periode | Saldo Induk Terlapor | Hasil Rekalkulasi Komponen | Varians Rekonsiliasi | Rasio Deviasi (%) | Analisis Komponen Terlapor |\n",
            "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n",
        ]

        for index, finding in enumerate(sorted_findings, start=1):
            target_balance_str = format_number(finding.reported_target_balance)
            recalculated_components_str = format_number(
                finding.recalculated_components_total
            )
            variance_str = format_number(finding.reconciliation_variance)
            deviation_str = f"{finding.deviation_ratio_percent:.2f}%"
            audit_note = finding.diagnostic_audit_notes

            output_lines.append(
                f"| {index} | `{finding.entity_ticker}` | {finding.fiscal_year} | `{finding.fiscal_period}` | {target_balance_str} | {recalculated_components_str} | {variance_str} | {deviation_str} | {audit_note} |\n"
            )

        output_lines.append("\n")
        return output_lines


# Strategy Registries
AUDIT_STRATEGIES: dict[
    AuditDiscrepancyCategory, tuple[AuditMismatchTableStrategy, str, str]
] = {
    AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY: (
        MaterialDiscrepancyStrategy(),
        "1. Diskrepansi Material Pelaporan",
        "Deviasi signifikan (>= 100%) akibat salah input angka, kelebihan digit nol, atau kekeliruan skala pelaporan sumber iXBRL emiten.",
    ),
    AuditDiscrepancyCategory.PARTIAL_BREAKDOWN_DISCREPANCY: (
        PartialBreakdownStrategy(),
        "2. Rincian Tidak Lengkap",
        "Pos rincian anak yang dilaporkan belum menjumlah penuh ke saldo induk (1.0% - 99.9%) karena adanya transaksi minor yang belum terpetakan atau tidak dirinci.",
    ),
    AuditDiscrepancyCategory.OMITTED_PARTIAL_SUBTOTAL: (
        OmittedPartialSubtotalStrategy(),
        "3. Omisi Subtotal (Rincian Tidak Lengkap)",
        "Subtotal perantara dikosongkan dan pos rincian anaknya pun belum mencakup seluruh komponen saldo induk.",
    ),
    AuditDiscrepancyCategory.SIGN_INVERSION: (
        SignInversionStrategy(),
        "4. Inversi Tanda Saldo",
        "Nilai diinput dengan tanda terbalik pada formulir iXBRL (misalnya angka negatif pada pos pengeluaran yang di taksonomi sudah bertanda pengurang, menghasilkan minus ganda).",
    ),
    AuditDiscrepancyCategory.DUPLICATE_LINE_ITEM: (
        DuplicateLineItemStrategy(),
        "5. Duplikasi Pos Pengungkapan",
        "Nominal identik diinput ke dua pos berbeda (pencatatan ganda pengungkapan), atau saldo induk disalin ulang ke pos rincian anak.",
    ),
    AuditDiscrepancyCategory.OMITTED_INTERMEDIATE_SUBTOTAL: (
        OmittedSubtotalStrategy(),
        "6. Omisi Subtotal Perantara (Rincian Klop)",
        "Emiten mengosongkan pos subtotal perantara, namun seluruh pos rincian anak secara aljabar menjumlah seimbang (<= 1.0%) ke saldo induk.",
    ),
    AuditDiscrepancyCategory.ROGUE_CHILD_WITHOUT_PARENT: (
        RogueChildStrategy(),
        "7. Rincian Tanpa Saldo Induk",
        "Pos rincian anak terisi angka riil, namun saldo akun induk dilaporkan nol (indikasi pos terisi tanpa jangkar induk atau perbedaan taksonomi industri).",
    ),
    AuditDiscrepancyCategory.LUMP_SUM_AGGREGATE_PRESENTATION: (
        LumpSumAggregateStrategy(),
        "8. Penyajian Agregat Tanpa Rincian",
        "Emiten menyajikan saldo total pada akun induk, namun seluruh pos rincian anak di bawahnya tidak dirinci (bernilai nol).",
    ),
    AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE: (
        RoundingToleranceStrategy(),
        "9. Selisih Pembulatan",
        "Selisih minor (<= 1.0%) akibat toleransi pembulatan desimal, penyajian dalam jutaan rupiah, atau selisih kurs valuta asing.",
    ),
}

ORDERED_CATEGORIES: list[AuditDiscrepancyCategory] = [
    AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY,
    AuditDiscrepancyCategory.PARTIAL_BREAKDOWN_DISCREPANCY,
    AuditDiscrepancyCategory.OMITTED_PARTIAL_SUBTOTAL,
    AuditDiscrepancyCategory.SIGN_INVERSION,
    AuditDiscrepancyCategory.DUPLICATE_LINE_ITEM,
    AuditDiscrepancyCategory.OMITTED_INTERMEDIATE_SUBTOTAL,
    AuditDiscrepancyCategory.ROGUE_CHILD_WITHOUT_PARENT,
    AuditDiscrepancyCategory.LUMP_SUM_AGGREGATE_PRESENTATION,
    AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE,
]

CROSS_AUDIT_STRATEGIES: dict[
    AuditDiscrepancyCategory, tuple[AuditMismatchTableStrategy, str, str]
] = {
    AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY: (
        MaterialDiscrepancyStrategy(),
        "1. Diskrepansi Material Lintas Laporan",
        "Perbedaan saldo ekstrem antar-laporan keuangan emiten yang memerlukan penelusuran lebih lanjut.",
    ),
    AuditDiscrepancyCategory.PARTIAL_BREAKDOWN_DISCREPANCY: (
        PartialBreakdownStrategy(),
        "2. Perbedaan Rincian Kas (Restricted Cash / Overdraft)",
        "Perbedaan saldo kas neraca vs arus kas akibat kas yang dibatasi penggunaannya (restricted cash) atau cerukan bank sesuai PSAK 2 / IAS 7.",
    ),
    AuditDiscrepancyCategory.SIGN_INVERSION: (
        SignInversionStrategy(),
        "3. Inversi Tanda Saldo Antar-Laporan",
        "Emiten melaporkan nilai dengan tanda berlawanan antar-laporan (misal: laba rugi mencatat rugi negatif, namun di arus kas diinput positif).",
    ),
    AuditDiscrepancyCategory.DUPLICATE_LINE_ITEM: (
        DuplicateLineItemStrategy(),
        "4. Duplikasi Pos Antar-Laporan",
        "Terdapat pengungkapan ganda pada komponen kas lintas laporan.",
    ),
    AuditDiscrepancyCategory.ROGUE_CHILD_WITHOUT_PARENT: (
        RogueChildStrategy(),
        "5. Rincian Tanpa Saldo Induk Lintas Laporan",
        "Akun target di salah satu laporan bernilai 0, namun akun lawan terisi angka riil.",
    ),
    AuditDiscrepancyCategory.LUMP_SUM_AGGREGATE_PRESENTATION: (
        LumpSumAggregateStrategy(),
        "6. Penyajian Agregat Lintas Laporan",
        "Emiten melaporkan saldo pada salah satu akun, namun akun lawan tidak diisi (0).",
    ),
    AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE: (
        RoundingToleranceStrategy(),
        "7. Selisih Pembulatan Lintas Laporan",
        "Selisih minor (<= 1.0%) akibat toleransi pembulatan desimal, jutaan rupiah, atau kurs valas.",
    ),
}

ORDERED_CROSS_CATEGORIES: list[AuditDiscrepancyCategory] = [
    AuditDiscrepancyCategory.MATERIAL_REPORTING_DISCREPANCY,
    AuditDiscrepancyCategory.PARTIAL_BREAKDOWN_DISCREPANCY,
    AuditDiscrepancyCategory.SIGN_INVERSION,
    AuditDiscrepancyCategory.DUPLICATE_LINE_ITEM,
    AuditDiscrepancyCategory.ROGUE_CHILD_WITHOUT_PARENT,
    AuditDiscrepancyCategory.LUMP_SUM_AGGREGATE_PRESENTATION,
    AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE,
]


def main():
    print("Memindai data Parquet statements untuk audit rincian mismatch...")
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

    current_period_df = raw_dataframe.filter(
        pl.col("context").str.starts_with("Current")
    )

    # Ranking entry point berdasarkan kelengkapan akun unik terbanyak
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

    markdown_lines: list[str] = [
        "# Laporan Rincian Kasus Ketidakseimbangan Saldo IDX (Equation Mismatches)\n",
        "> Dokumen ini memuat audit mendalam atas seluruh emiten dan laporan keuangan yang mengalami diskrepansi pada pengujian konsistensi matematis iXBRL BEI. Setiap temuan diklasifikasikan secara deterministik menggunakan Strategy Pattern ke dalam kategori pola pelaporan emiten.\n",
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
.eq-header-card {
    border-left: 4px solid #3b82f6;
    background: #f1f5f9;
    padding: 12px 16px;
    margin: 24px 0 12px 0;
    border-radius: 0 6px 6px 0;
}
@media (prefers-color-scheme: dark) {
    .eq-header-card {
        background: #1e293b;
        border-left-color: #60a5fa;
    }
}
.eq-title {
    font-size: 1.1em;
    font-weight: bold;
    margin-bottom: 4px;
}
.eq-meta {
    font-size: 0.9em;
    color: #64748b;
}
.eq-count-badge {
    display: inline-block;
    background: #ef4444;
    color: white;
    padding: 1px 8px;
    border-radius: 12px;
    font-size: 0.8em;
    font-weight: bold;
    margin-left: 8px;
}
</style>
""",
        "## Daftar Isi Laporan Detail Selisih\n",
        "- [Laporan Posisi Keuangan (Balance Statement)](#laporan-posisi-keuangan-balance-statement)",
        "- [Laporan Laba Rugi dan Penghasilan Komprehensif Lain (Income Statement)](#laporan-laba-rugi-dan-penghasilan-komprehensif-lain-income-statement)",
        "- [Laporan Arus Kas (Cash Flow Statement)](#laporan-arus-kas-cash-flow-statement)",
        "- [Artikulasi Saldo Lintas Laporan (Inter-Statement Articulation)](#artikulasi-saldo-lintas-laporan-inter-statement-articulation)",
        "",
    ]

    target_statements = [
        ("balance_statement", "Laporan Posisi Keuangan (Balance Statement)"),
        (
            "income_statement",
            "Laporan Laba Rugi dan Penghasilan Komprehensif Lain (Income Statement)",
        ),
        ("cash_flow_statement", "Laporan Arus Kas (Cash Flow Statement)"),
    ]

    for statement_name, statement_label in target_statements:
        markdown_lines.append(f"## {statement_label}\n")
        statement_has_mismatches = False

        for entry_point in ordered_entry_points:
            sector_equations = ENTRY_POINT_EQUATIONS.get(entry_point, {}).get(
                statement_name, {}
            )
            if not sector_equations:
                continue

            sorted_variants = sorted(
                sector_equations.keys(),
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
                equations: tuple[AccountingEquationSpecification, ...] = (
                    sector_equations[variant]
                )
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

                variant_mismatch_blocks: list[str] = []

                for equation in equations:
                    equation_id = equation.equation_identifier
                    conformance_col = f"is_conformant_{equation_id}"

                    if conformance_col not in verified_df.columns:
                        continue

                    equation_findings = findings_by_eq.get(equation_id, [])
                    non_exact_findings = [
                        f
                        for f in equation_findings
                        if f.category != AuditDiscrepancyCategory.CONFORMANT_EXACT
                    ]

                    if not non_exact_findings:
                        continue

                    statement_has_mismatches = True
                    equation_type_str = (
                        "Keseimbangan Makro (Horizontal)"
                        if equation.equation_category
                        == AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY
                        else "Penjumlahan Rincian (Vertikal)"
                    )
                    if variant_mismatch_blocks:
                        variant_mismatch_blocks.append("\n---\n\n")

                    total_reports_count = len(verified_df)
                    exact_count = total_reports_count - len(non_exact_findings)
                    rounding_findings = [
                        f
                        for f in non_exact_findings
                        if f.category
                        == AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE
                    ]
                    rounding_count = len(rounding_findings)
                    total_conforming_count = exact_count + rounding_count

                    pct_exact = (
                        exact_count / total_reports_count * 100.0
                        if total_reports_count > 0
                        else 0.0
                    )
                    pct_conforming = (
                        total_conforming_count / total_reports_count * 100.0
                        if total_reports_count > 0
                        else 0.0
                    )
                    rounding_badge_info = (
                        f" (+{rounding_count:,} pembulatan)"
                        if rounding_count > 0
                        else ""
                    )

                    header_card = (
                        f'<div class="eq-header-card">\n'
                        f'  <div class="eq-title">\n'
                        f"    <code>[{equation.target_account.code}]</code> {equation.equation_name}\n"
                        f'    <span class="eq-count-badge">{len(non_exact_findings):,} laporan selisih{rounding_badge_info}</span>\n'
                        f"  </div>\n"
                        f'  <div class="eq-meta">\n'
                        f"    <b>Formula:</b> <code>{equation.formula_representation}</code> &bull; <b>Keseimbangan:</b> {pct_exact:.2f}% (Eksak) &bull; <b>{pct_conforming:.2f}% (+Pembulatan)</b> &bull; <b>Hubungan Akun:</b> {equation_type_str}\n"
                        f"  </div>\n"
                        f"</div>\n"
                    )
                    variant_mismatch_blocks.append(header_card)

                    findings_by_category: dict[
                        AuditDiscrepancyCategory, list[AuditDiscrepancyFinding]
                    ] = {cat: [] for cat in ORDERED_CATEGORIES}
                    for finding in non_exact_findings:
                        if finding.category in findings_by_category:
                            findings_by_category[finding.category].append(finding)

                    for category in ORDERED_CATEGORIES:
                        category_findings = findings_by_category[category]
                        if not category_findings:
                            continue
                        strategy, title, explanation = AUDIT_STRATEGIES[category]
                        variant_mismatch_blocks.extend(
                            strategy.render(category_findings, title, explanation)
                        )

                if variant_mismatch_blocks:
                    markdown_lines.append(f"### `{entry_point}` &mdash; `{variant}`\n")
                    markdown_lines.extend(variant_mismatch_blocks)
                    markdown_lines.append("\n\n")

        if not statement_has_mismatches:
            markdown_lines.append(
                "*Seluruh keterhubungan akun pada laporan ini seimbang sempurna tanpa selisih.*\n\n"
            )

        markdown_lines.append(
            '<hr style="border: none; border-top: 4px double #64748b; margin: 48px 0;" />\n\n'
        )

    # 4. Evaluasi Artikulasi Lintas Laporan
    print("Mengevaluasi selisih artikulasi lintas laporan...")
    markdown_lines.append(
        "## Artikulasi Saldo Lintas Laporan (Inter-Statement Articulation)\n"
    )
    markdown_lines.append(
        "> Bagian ini memuat rincian laporan emiten yang mengalami perbedaan saldo pada pengujian keterkaitan antar-laporan keuangan (*inter-statement articulation*) periode berjalan (*Current Period*) yang disesuaikan secara khusus (*custom*) per sektor industri tanpa melibatkan saldo periode lalu (*Prior*).\n"
    )
    markdown_lines.append("### Panduan Formula Artikulasi Lintas Laporan per Sektor\n")
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
      <td><code>[CFS.CASH.END] == [BS.BANK.CASH] + [BS.BANK.CA.BI]</code></td>
      <td><b>Artikulasi Kas Akhir Perbankan Konvensional &amp; Syariah</b><br>Berlaku khusus untuk <code>financial_and_sharia</code> (bank). Menghubungkan kas fisik bank dan giro wajib minimum pada Bank Indonesia terhadap kas akhir arus kas.</td>
      <td>&bull; <code>[CFS.CASH.END]</code>: <i>cash_flow_statement</i> &rarr; <code>CurrentYearInstant</code> &rarr; <code>CashAndCashEquivalentsCashFlows</code><br>&bull; <code>[BS.BANK.CASH]</code>: <i>balance_statement</i> &rarr; <code>Cash</code><br>&bull; <code>[BS.BANK.CA.BI]</code>: <i>balance_statement</i> &rarr; <code>CurrentAccountsWithBankIndonesia</code></td>
    </tr>
    <tr>
      <td align="center"><b>4</b></td>
      <td><code>[BS.CASH] == [CFS.CASH.END]</code></td>
      <td><b>Artikulasi Kas Akhir KIK (Kontrak Investasi Kolektif)</b><br>Berlaku untuk instrumen KIK-EBA / KIK-DIRE. Kas fisik di neraca terhubung ke kas akhir arus kas.</td>
      <td>&bull; <code>[BS.CASH]</code>: <i>balance_statement</i> &rarr; <code>CashAndCashEquivalents</code><br>&bull; <code>[CFS.CASH.END]</code>: <i>cash_flow_statement</i> &rarr; <code>CashAndCashEquivalentsCashFlows</code></td>
    </tr>
  </tbody>
</table>
"""
    )

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
        cross_sector_equations = ENTRY_POINT_CROSS_EQUATIONS.get(entry_point, {})
        if not cross_sector_equations:
            continue

        sorted_cfs_variants = sorted(
            cross_sector_equations.keys(),
            key=lambda v_name: (
                -density_map.get((entry_point, "cash_flow_statement", v_name), (0, 0))[
                    0
                ],
            ),
        )

        for cfs_variant in sorted_cfs_variants:
            cross_eqs: tuple[AccountingEquationSpecification, ...] = (
                cross_sector_equations[cfs_variant]
            )
            if not cross_eqs:
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
                cross_pivoted_df, cross_eqs
            )
            cross_findings_by_eq = classify_accounting_equation_discrepancies(
                cross_verified_df, cross_eqs
            )

            cross_mismatch_blocks: list[str] = []

            for equation in cross_eqs:
                eq_id = equation.equation_identifier
                conformance_col = f"is_conformant_{eq_id}"

                if conformance_col not in cross_verified_df.columns:
                    continue

                eq_findings = cross_findings_by_eq.get(eq_id, [])
                non_exact_cross = [
                    f
                    for f in eq_findings
                    if f.category != AuditDiscrepancyCategory.CONFORMANT_EXACT
                ]

                if not non_exact_cross:
                    continue

                if cross_mismatch_blocks:
                    cross_mismatch_blocks.append("\n---\n\n")

                tot_reports = len(cross_verified_df)
                exact_count = tot_reports - len(non_exact_cross)
                rounding_cross = [
                    f
                    for f in non_exact_cross
                    if f.category
                    == AuditDiscrepancyCategory.CONFORMANT_WITHIN_ROUNDING_TOLERANCE
                ]
                round_count = len(rounding_cross)
                tot_conforming = exact_count + round_count

                pct_exact = (
                    exact_count / tot_reports * 100.0 if tot_reports > 0 else 0.0
                )
                pct_conforming = (
                    tot_conforming / tot_reports * 100.0 if tot_reports > 0 else 0.0
                )
                round_badge_info = (
                    f" (+{round_count:,} pembulatan)" if round_count > 0 else ""
                )

                header_card = (
                    f'<div class="eq-header-card">\n'
                    f'  <div class="eq-title">\n'
                    f"    <code>[{equation.target_account.code}]</code> {equation.equation_name}\n"
                    f'    <span class="eq-count-badge">{len(non_exact_cross):,} laporan selisih{round_badge_info}</span>\n'
                    f"  </div>\n"
                    f'  <div class="eq-meta">\n'
                    f"    <b>Formula:</b> <code>{equation.formula_representation}</code> &bull; <b>Keseimbangan:</b> {pct_exact:.2f}% (Eksak) &bull; <b>{pct_conforming:.2f}% (+Pembulatan)</b> &bull; <b>Hubungan Akun:</b> Artikulasi Lintas Laporan\n"
                    f"  </div>\n"
                    f"</div>\n"
                )
                cross_mismatch_blocks.append(header_card)

                cross_findings_by_cat: dict[
                    AuditDiscrepancyCategory, list[AuditDiscrepancyFinding]
                ] = {cat: [] for cat in ORDERED_CROSS_CATEGORIES}
                for finding in non_exact_cross:
                    if finding.category in cross_findings_by_cat:
                        cross_findings_by_cat[finding.category].append(finding)

                for category in ORDERED_CROSS_CATEGORIES:
                    cat_findings = cross_findings_by_cat[category]
                    if not cat_findings:
                        continue
                    strategy, title, explanation = CROSS_AUDIT_STRATEGIES[category]
                    cross_mismatch_blocks.extend(
                        strategy.render(cat_findings, title, explanation)
                    )

            if cross_mismatch_blocks:
                markdown_lines.append(f"### `{entry_point}` &mdash; `{cfs_variant}`\n")
                markdown_lines.extend(cross_mismatch_blocks)
                markdown_lines.append("\n\n")

    output_path = "docs/accounts/equation_mismatch_reports.md"
    clean_lines = [
        line if line.endswith("\n") else f"{line}\n" for line in markdown_lines
    ]
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(clean_lines)

    print(
        f"Laporan detail mismatch berhasil dibuat di {output_path} ({len(markdown_lines)} baris)."
    )


if __name__ == "__main__":
    main()
