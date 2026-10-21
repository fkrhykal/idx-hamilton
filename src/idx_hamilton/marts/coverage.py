import collections
from enum import StrEnum
from pathlib import Path

import patito as pt
import polars as pl
from hamilton.function_modifiers import group, inject, source

from idx_hamilton.sources import IxbrlFillingUrl
from idx_hamilton.transformations.backfilling import (
    BACKFILLED_ACCOUNT_NODES,
    AccountFact,
    Provenace,
)


class ColorMapEnum(StrEnum):
    color: str

    def __new__(cls, value: str, color: str):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.color = color
        return obj

    @classmethod
    def color_map(cls) -> dict[str, str]:
        return {s.value: s.color for s in cls}


class ReportStatus(ColorMapEnum):
    AVAILABLE = ("AVAILABLE", "#2ecc71")
    CORRUPTED = ("CORRUPTED", "#e74c3c")
    FAILED = ("FAILED", "#f1c40f")
    MISSING = ("MISSING", "#252e38")


class FactStatus(ColorMapEnum):
    ACTUAL = (Provenace.ACTUAL, "#2ecc71")
    COMPARATIVE_BACKFILL = (Provenace.COMPARATIVE_BACKFILL, "#3498db")
    MISSING = (Provenace.MISSING, "#252e38")


PERIOD_ORDER = {"TW1": 1, "TW2": 2, "TW3": 3, "Audit": 4}


def _sort_timeframes(timeframes: list[str]) -> list[str]:
    def key_fn(tf: str) -> tuple[int, int]:
        parts = tf.split("_")
        year = int(parts[0])
        period = parts[1] if len(parts) > 1 else ""
        return year, PERIOD_ORDER.get(period, 99)

    return sorted(timeframes, key=key_fn)


def report_coverage_matrix(
    ixbrl_filling_urls: list[IxbrlFillingUrl],
) -> pl.DataFrame:
    records = []
    unique_tfs = list({f"{u.year}_{u.period}" for u in ixbrl_filling_urls})
    all_timeframes = _sort_timeframes(unique_tfs)

    for item in ixbrl_filling_urls:
        base_path = (
            Path(".data")
            .joinpath("sources")
            .joinpath("ixbrl_financial_report")
            .joinpath(item.emiten_code)
            .joinpath(f"{item.year}_{item.period}")
        )

        if base_path.with_suffix(".zip").is_file():
            status = ReportStatus.AVAILABLE
        elif base_path.with_suffix(".corrupted").is_file():
            status = ReportStatus.CORRUPTED
        elif base_path.with_suffix(".failed").is_file():
            status = ReportStatus.FAILED
        else:
            status = ReportStatus.MISSING

        records.append(
            {
                "emiten_code": item.emiten_code,
                "timeframe": f"{item.year}_{item.period}",
                "status": status,
            }
        )

    df = pl.DataFrame(records)

    pivoted = df.pivot(
        on="timeframe",
        index="emiten_code",
        values="status",
        aggregate_function="first",
    ).fill_null(ReportStatus.MISSING)

    cols = ["emiten_code"] + [c for c in all_timeframes if c in pivoted.columns]
    return pivoted.select(cols).sort("emiten_code")


def _render_matrix_to_svg(
    matrix: pl.DataFrame,
    output_path: Path,
    color_map: dict[str, str],
) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    timeframe_cols = [c for c in matrix.columns if c != "emiten_code"]
    rows = matrix.to_dicts()

    cell_w = 28
    cell_h = 13
    pad_x = 75
    pad_y = 55
    year_gap = 14

    year_groups: dict[str, list[tuple[int, str]]] = collections.defaultdict(list)
    for idx, tf in enumerate(timeframe_cols):
        year, period = tf.split("_")
        year_groups[year].append((idx, period))

    years = list(year_groups.keys())
    year_to_idx = {y: i for i, y in enumerate(years)}

    def get_col_x(col_idx: int, yr: str) -> float:
        return pad_x + col_idx * cell_w + year_to_idx[yr] * year_gap

    width = (
        pad_x + len(timeframe_cols) * cell_w + max(0, len(years) - 1) * year_gap + 20
    )
    height = pad_y + len(rows) * cell_h + 20

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" style="background:#141414; font-family:Consolas, Monaco, monospace;">'
    ]

    for year, quarters in year_groups.items():
        start_x = get_col_x(quarters[0][0], year)
        end_x = get_col_x(quarters[-1][0], year) + cell_w
        mid_x = (start_x + end_x) / 2

        svg.append(
            f'<text x="{mid_x}" y="20" fill="#ddd" font-weight="600" font-size="11" text-anchor="middle">{year}</text>'
        )
        svg.append(
            f'<line x1="{start_x}" y1="26" x2="{end_x - 2}" y2="26" stroke="#444" stroke-width="1"/>'
        )

    for col_idx, tf in enumerate(timeframe_cols):
        year, period = tf.split("_")
        label = "FY" if period == "Audit" else period
        x = get_col_x(col_idx, year) + (cell_w - 2) / 2
        svg.append(
            f'<text x="{x}" y="42" fill="#888" font-size="9" text-anchor="middle">{label}</text>'
        )

    svg.append(
        f'<line x1="{pad_x - 10}" y1="{pad_y - 5}" x2="{width - 10}" y2="{pad_y - 5}" stroke="#555" stroke-width="1.5"/>'
    )

    for row_idx, r in enumerate(rows):
        y = pad_y + row_idx * cell_h
        emiten = r["emiten_code"]

        svg.append(
            f'<text x="{pad_x - 8}" y="{y + 10}" fill="#aaa" text-anchor="end" font-size="9">{emiten}</text>'
        )

        for col_idx, tf in enumerate(timeframe_cols):
            year, _ = tf.split("_")
            x = get_col_x(col_idx, year)
            status = r.get(tf, ReportStatus.MISSING)
            color = color_map.get(status, "#252e38")

            svg.append(
                f'<rect x="{x}" y="{y}" width="{cell_w - 2}" height="{cell_h - 2}" rx="1" fill="{color}">'
                f"<title>{emiten} [{tf}]: {status}</title></rect>"
            )

    svg.append("</svg>")
    output_path.write_text("\n".join(svg), encoding="utf-8")
    return output_path


def report_coverage_svg(report_coverage_matrix: pl.DataFrame) -> Path:
    return _render_matrix_to_svg(
        report_coverage_matrix,
        Path("docs/coverage_heatmap.svg"),
        ReportStatus.color_map(),
    )


def report_coverage_png(report_coverage_svg: Path) -> Path:
    from resvg_py import svg_to_bytes

    output_path = report_coverage_svg.with_suffix(".png")
    svg_string = report_coverage_svg.read_text(encoding="utf-8")
    png_bytes = svg_to_bytes(svg_string=svg_string)
    output_path.write_bytes(png_bytes)
    return output_path


FACT_NODE_NAMES = list(BACKFILLED_ACCOUNT_NODES.keys())


@inject(facts=group(*[source(name) for name in FACT_NODE_NAMES]))
def backfill_coverage_matrix(
    facts: list[pt.DataFrame[AccountFact]],
) -> pl.DataFrame:
    valid_dfs = [df for df in facts if not df.is_empty()]
    if not valid_dfs:
        return pl.DataFrame()

    df = AccountFact.validate(pl.concat(valid_dfs))

    status_df = (
        df.with_columns(
            timeframe=pl.concat_str(
                [AccountFact.c.year, pl.lit("_"), AccountFact.c.period]
            )
        )
        .group_by(["emiten_code", "timeframe"])
        .agg(
            status=pl.when((AccountFact.c.provenance == FactStatus.ACTUAL).any())
            .then(pl.lit(FactStatus.ACTUAL))
            .otherwise(pl.lit(FactStatus.COMPARATIVE_BACKFILL))
        )
    )

    matrix = status_df.pivot(
        on="timeframe",
        index="emiten_code",
        values="status",
        aggregate_function="first",
    ).fill_null(FactStatus.MISSING)

    all_timeframes = _sort_timeframes([c for c in matrix.columns if c != "emiten_code"])
    cols = ["emiten_code"] + all_timeframes
    return matrix.select(cols).sort("emiten_code")


def backfill_coverage_svg(backfill_coverage_matrix: pl.DataFrame) -> Path:

    return _render_matrix_to_svg(
        backfill_coverage_matrix,
        Path("docs/backfill_coverage_heatmap.svg"),
        FactStatus.color_map(),
    )


def backfill_coverage_png(backfill_coverage_svg: Path) -> Path:
    from resvg_py import svg_to_bytes

    output_path = backfill_coverage_svg.with_suffix(".png")
    svg_string = backfill_coverage_svg.read_text(encoding="utf-8")
    png_bytes = svg_to_bytes(svg_string=svg_string)
    output_path.write_bytes(png_bytes)
    return output_path


def coverage_summary_svg(
    report_coverage_matrix: pl.DataFrame,
    backfill_coverage_matrix: pl.DataFrame,
) -> Path:
    output_path = Path("docs/coverage_summary.svg")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    tf_cols_src = [c for c in report_coverage_matrix.columns if c != "emiten_code"]
    tf_cols_fact = [c for c in backfill_coverage_matrix.columns if c != "emiten_code"]

    num_emitens = len(report_coverage_matrix)
    num_fact_emitens = len(backfill_coverage_matrix)

    years = sorted({int(c.split("_")[0]) for c in tf_cols_src if "_" in c})

    year_rows = []
    for y in years:
        y_tf_src = [c for c in tf_cols_src if c.startswith(f"{y}_")]
        y_tf_fact = [c for c in tf_cols_fact if c.startswith(f"{y}_")]

        src_cells = num_emitens * len(y_tf_src) if y_tf_src else 1
        fact_cells = num_fact_emitens * len(y_tf_fact) if y_tf_fact else 1

        y_avail = sum(
            int((report_coverage_matrix[c] == ReportStatus.AVAILABLE).sum())
            for c in y_tf_src
        )
        y_failed = sum(
            int((report_coverage_matrix[c] == ReportStatus.FAILED).sum())
            for c in y_tf_src
        )
        y_corrupt = sum(
            int((report_coverage_matrix[c] == ReportStatus.CORRUPTED).sum())
            for c in y_tf_src
        )
        y_missing_src = sum(
            int((report_coverage_matrix[c] == ReportStatus.MISSING).sum())
            for c in y_tf_src
        )

        y_actual = sum(
            int((backfill_coverage_matrix[c] == FactStatus.ACTUAL).sum())
            for c in y_tf_fact
        )
        y_backfill = sum(
            int((backfill_coverage_matrix[c] == FactStatus.COMPARATIVE_BACKFILL).sum())
            for c in y_tf_fact
        )
        y_missing_fact = sum(
            int((backfill_coverage_matrix[c] == FactStatus.MISSING).sum())
            for c in y_tf_fact
        )

        src_cov = (y_avail / src_cells) * 100
        fact_cov = ((y_actual + y_backfill) / fact_cells) * 100
        gain = fact_cov - src_cov

        year_rows.append(
            {
                "year": y,
                "periods": len(y_tf_src),
                "src_cells": src_cells,
                "avail": y_avail,
                "failed": y_failed,
                "corrupt": y_corrupt,
                "missing_src": y_missing_src,
                "src_cov": src_cov,
                "fact_cells": fact_cells,
                "actual": y_actual,
                "backfill": y_backfill,
                "missing_fact": y_missing_fact,
                "fact_cov": fact_cov,
                "gain": gain,
            }
        )

    tot_src_cells = sum(r["src_cells"] for r in year_rows) or 1
    tot_avail = sum(r["avail"] for r in year_rows)
    tot_failed = sum(r["failed"] for r in year_rows)
    tot_corrupt = sum(r["corrupt"] for r in year_rows)
    tot_missing_src = sum(r["missing_src"] for r in year_rows)
    tot_src_cov = (tot_avail / tot_src_cells) * 100

    tot_fact_cells = sum(r["fact_cells"] for r in year_rows) or 1
    tot_actual = sum(r["actual"] for r in year_rows)
    tot_backfill = sum(r["backfill"] for r in year_rows)
    tot_missing_fact = sum(r["missing_fact"] for r in year_rows)
    tot_fact_cov = ((tot_actual + tot_backfill) / tot_fact_cells) * 100
    tot_gain = tot_fact_cov - tot_src_cov

    row_h = 32
    table_top = 150
    table_h = 75 + len(year_rows) * row_h + 45
    total_svg_h = table_top + table_h + 50

    span_start = (
        f"{years[0]}_{tf_cols_src[0].split('_')[1]}" if years and tf_cols_src else "N/A"
    )
    span_end = (
        f"{years[-1]}_{tf_cols_src[-1].split('_')[1]}"
        if years and tf_cols_src
        else "N/A"
    )

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="940" height="{total_svg_h}" viewBox="0 0 940 {total_svg_h}" style="background:#141414; font-family:Consolas, Monaco, -apple-system, sans-serif;">',
        f'  <rect width="940" height="{total_svg_h}" fill="#141414"/>',
        "",
        "  <!-- Header -->",
        '  <text x="40" y="42" fill="#ffffff" font-size="20" font-weight="700">IDX iXBRL Coverage &amp; Backfill Comparison</text>',
        f'  <text x="40" y="64" fill="#888888" font-size="12">Universe: {num_emitens:,} Emiten | {len(tf_cols_src)} Total Periods ({span_start} to {span_end})</text>',
        "",
        "  <!-- Top Stat Cards -->",
        '  <rect x="40" y="82" width="270" height="52" rx="6" fill="#1b1f24" stroke="#2d333b" stroke-width="1"/>',
        '  <text x="55" y="102" fill="#8b949e" font-size="10" font-weight="600">SOURCE AVAILABLE FILINGS</text>',
        f'  <text x="55" y="122" fill="#3fb950" font-size="16" font-weight="700">{tot_avail:,} <tspan fill="#8b949e" font-size="11" font-weight="400">({tot_src_cov:.1f}% cov)</tspan></text>',
        "",
        '  <rect x="330" y="82" width="270" height="52" rx="6" fill="#1b1f24" stroke="#2d333b" stroke-width="1"/>',
        '  <text x="345" y="102" fill="#8b949e" font-size="10" font-weight="600">RESCUED VIA BACKFILL</text>',
        f'  <text x="345" y="122" fill="#58a6ff" font-size="16" font-weight="700">+{tot_backfill:,} facts <tspan fill="#8b949e" font-size="11" font-weight="400">(+{tot_gain:.1f}% boost)</tspan></text>',
        "",
        '  <rect x="620" y="82" width="280" height="52" rx="6" fill="#1b1f24" stroke="#2d333b" stroke-width="1"/>',
        '  <text x="635" y="102" fill="#8b949e" font-size="10" font-weight="600">FINAL FACT COVERAGE</text>',
        f'  <text x="635" y="122" fill="#3fb950" font-size="16" font-weight="700">{tot_fact_cov:.1f}% <tspan fill="#8b949e" font-size="11" font-weight="400">({tot_actual + tot_backfill:,} / {tot_fact_cells:,})</tspan></text>',
        "",
        "  <!-- Main Comparison Table Card -->",
        f'  <rect x="40" y="{table_top}" width="860" height="{table_h}" rx="8" fill="#181c22" stroke="#2d333b" stroke-width="1"/>',
        "",
        "  <!-- Section Header Groups (Row 1) -->",
        '  <text x="60" y="176" fill="#8b949e" font-size="11" font-weight="700">PERIOD</text>',
        '  <text x="315" y="176" fill="#8b949e" font-size="11" font-weight="700" text-anchor="middle">SOURCE INGESTION (BEI FILINGS)</text>',
        '  <line x1="140" y1="184" x2="495" y2="184" stroke="#30363d" stroke-width="1"/>',
        '  <text x="650" y="176" fill="#8b949e" font-size="11" font-weight="700" text-anchor="middle">RECONCILED FACTS (POST-BACKFILL)</text>',
        '  <line x1="515" y1="184" x2="795" y2="184" stroke="#30363d" stroke-width="1"/>',
        '  <text x="850" y="176" fill="#8b949e" font-size="11" font-weight="700" text-anchor="middle">BOOST</text>',
        '  <line x1="815" y1="184" x2="885" y2="184" stroke="#30363d" stroke-width="1"/>',
        "",
        "  <!-- Column Subheaders (Row 2) -->",
        '  <text x="60" y="204" fill="#6e7681" font-size="10" font-weight="600">YEAR</text>',
        '  <text x="195" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">AVAILABLE</text>',
        '  <text x="270" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">FAILED</text>',
        '  <text x="345" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">CORRUPT</text>',
        '  <text x="420" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">MISSING</text>',
        '  <text x="495" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">SRC COV</text>',
        '  <text x="580" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">ACTUAL</text>',
        '  <text x="660" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">BACKFILL</text>',
        '  <text x="735" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">MISSING</text>',
        '  <text x="795" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">FACT COV</text>',
        '  <text x="880" y="204" fill="#6e7681" font-size="10" font-weight="600" text-anchor="end">NET GAIN</text>',
        '  <line x1="40" y1="214" x2="900" y2="214" stroke="#30363d" stroke-width="1"/>',
    ]

    curr_y = 238
    for r in year_rows:
        failed_fill = ReportStatus.FAILED.color if r["failed"] > 0 else "#484f58"
        corrupt_fill = ReportStatus.CORRUPTED.color if r["corrupt"] > 0 else "#484f58"
        backfill_fill = (
            FactStatus.COMPARATIVE_BACKFILL.color if r["backfill"] > 0 else "#484f58"
        )
        gain_fill = "#3fb950" if r["gain"] > 0 else "#8b949e"

        svg.append(
            f'  <text x="60" y="{curr_y}" fill="#ffffff" font-size="11" font-weight="600">{r["year"]}</text>'
        )
        svg.append(
            f'  <text x="195" y="{curr_y}" fill="{ReportStatus.AVAILABLE.color}" font-size="11" text-anchor="end">{r["avail"]:,}</text>'
        )
        svg.append(
            f'  <text x="270" y="{curr_y}" fill="{failed_fill}" font-size="11" text-anchor="end">{r["failed"]:,}</text>'
        )
        svg.append(
            f'  <text x="345" y="{curr_y}" fill="{corrupt_fill}" font-size="11" text-anchor="end">{r["corrupt"]:,}</text>'
        )
        svg.append(
            f'  <text x="420" y="{curr_y}" fill="#8b949e" font-size="11" text-anchor="end">{r["missing_src"]:,}</text>'
        )
        svg.append(
            f'  <text x="495" y="{curr_y}" fill="#c9d1d9" font-size="11" text-anchor="end">{r["src_cov"]:.1f}%</text>'
        )
        svg.append(
            f'  <text x="580" y="{curr_y}" fill="{FactStatus.ACTUAL.color}" font-size="11" text-anchor="end">{r["actual"]:,}</text>'
        )
        svg.append(
            f'  <text x="660" y="{curr_y}" fill="{backfill_fill}" font-size="11" text-anchor="end">+{r["backfill"]:,}</text>'
        )
        svg.append(
            f'  <text x="735" y="{curr_y}" fill="#8b949e" font-size="11" text-anchor="end">{r["missing_fact"]:,}</text>'
        )
        svg.append(
            f'  <text x="795" y="{curr_y}" fill="{FactStatus.ACTUAL.color}" font-size="11" font-weight="600" text-anchor="end">{r["fact_cov"]:.1f}%</text>'
        )
        svg.append(
            f'  <text x="880" y="{curr_y}" fill="{gain_fill}" font-size="11" font-weight="700" text-anchor="end">+{r["gain"]:.1f}%</text>'
        )
        svg.append(
            f'  <line x1="40" y1="{curr_y + 9}" x2="900" y2="{curr_y + 9}" stroke="#21262d" stroke-width="1"/>'
        )
        curr_y += row_h

    # Total Row
    tot_y = curr_y + 6
    failed_tot_fill = ReportStatus.FAILED.color if tot_failed > 0 else "#8b949e"
    corrupt_tot_fill = ReportStatus.CORRUPTED.color if tot_corrupt > 0 else "#8b949e"
    svg.append(
        f'  <rect x="41" y="{tot_y - 17}" width="858" height="30" rx="4" fill="#21262d"/>'
    )
    svg.append(
        f'  <text x="60" y="{tot_y + 3}" fill="#ffffff" font-size="11" font-weight="700">TOTAL</text>'
    )
    svg.append(
        f'  <text x="195" y="{tot_y + 3}" fill="{ReportStatus.AVAILABLE.color}" font-size="11" font-weight="700" text-anchor="end">{tot_avail:,}</text>'
    )
    svg.append(
        f'  <text x="270" y="{tot_y + 3}" fill="{failed_tot_fill}" font-size="11" font-weight="700" text-anchor="end">{tot_failed:,}</text>'
    )
    svg.append(
        f'  <text x="345" y="{tot_y + 3}" fill="{corrupt_tot_fill}" font-size="11" font-weight="700" text-anchor="end">{tot_corrupt:,}</text>'
    )
    svg.append(
        f'  <text x="420" y="{tot_y + 3}" fill="#8b949e" font-size="11" font-weight="700" text-anchor="end">{tot_missing_src:,}</text>'
    )
    svg.append(
        f'  <text x="495" y="{tot_y + 3}" fill="#ffffff" font-size="11" font-weight="700" text-anchor="end">{tot_src_cov:.1f}%</text>'
    )
    svg.append(
        f'  <text x="580" y="{tot_y + 3}" fill="{FactStatus.ACTUAL.color}" font-size="11" font-weight="700" text-anchor="end">{tot_actual:,}</text>'
    )
    svg.append(
        f'  <text x="660" y="{tot_y + 3}" fill="{FactStatus.COMPARATIVE_BACKFILL.color}" font-size="11" font-weight="700" text-anchor="end">+{tot_backfill:,}</text>'
    )
    svg.append(
        f'  <text x="735" y="{tot_y + 3}" fill="#8b949e" font-size="11" font-weight="700" text-anchor="end">{tot_missing_fact:,}</text>'
    )
    svg.append(
        f'  <text x="795" y="{tot_y + 3}" fill="{FactStatus.ACTUAL.color}" font-size="11" font-weight="700" text-anchor="end">{tot_fact_cov:.1f}%</text>'
    )
    svg.append(
        f'  <text x="880" y="{tot_y + 3}" fill="#3fb950" font-size="11" font-weight="800" text-anchor="end">+{tot_gain:.1f}%</text>'
    )

    # Legend at bottom
    leg_y = table_top + table_h + 24
    svg.extend(
        [
            f'  <circle cx="60" cy="{leg_y}" r="4" fill="{ReportStatus.AVAILABLE.color}"/> <text x="70" y="{leg_y + 3}" fill="#8b949e" font-size="10">Available / Actual</text>',
            f'  <circle cx="210" cy="{leg_y}" r="4" fill="{ReportStatus.FAILED.color}"/> <text x="220" y="{leg_y + 3}" fill="#8b949e" font-size="10">Failed (HTTP 404)</text>',
            f'  <circle cx="350" cy="{leg_y}" r="4" fill="{ReportStatus.CORRUPTED.color}"/> <text x="360" y="{leg_y + 3}" fill="#8b949e" font-size="10">Corrupted Zip</text>',
            f'  <circle cx="470" cy="{leg_y}" r="4" fill="{FactStatus.COMPARATIVE_BACKFILL.color}"/> <text x="480" y="{leg_y + 3}" fill="#8b949e" font-size="10">Comparative Backfill</text>',
            f'  <circle cx="630" cy="{leg_y}" r="4" fill="{ReportStatus.MISSING.color}"/> <text x="640" y="{leg_y + 3}" fill="#8b949e" font-size="10">Missing</text>',
            "</svg>",
        ]
    )

    output_path.write_text("\n".join(svg), encoding="utf-8")
    return output_path


def coverage_summary_png(coverage_summary_svg: Path) -> Path:
    from resvg_py import svg_to_bytes

    output_path = coverage_summary_svg.with_suffix(".png")
    svg_string = coverage_summary_svg.read_text(encoding="utf-8")
    png_bytes = svg_to_bytes(svg_string=svg_string)
    output_path.write_bytes(png_bytes)
    return output_path
