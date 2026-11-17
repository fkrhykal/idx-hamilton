import collections
import json
from enum import StrEnum
from pathlib import Path
from typing import Any

import patito as pt
import polars as pl

from idx_hamilton.models import Model
from idx_hamilton.schema.canonical import CanonicalRegistry
from idx_hamilton.schema.statements import AccountNode, StatementSchemaRegistry
from idx_hamilton.sources import Period
from idx_hamilton.stagings.dei import DeiMetadata
from idx_hamilton.stagings.statement import StatementClassification
from idx_hamilton.transformations.canonical import CanonicalAccount
from idx_hamilton.transformations.validation import ValidationStatus

PERIOD_ORDER: dict[str, int] = {"TW1": 1, "TW2": 2, "TW3": 3, "Audit": 4}


class DiagnosticIssueType(StrEnum):
    INVALID_FOOTING = "INVALID_FOOTING"
    MISSING_CANONICAL = "MISSING_CANONICAL"
    MISSING_FILING = "MISSING_FILING"


class DiagnosticValidationStatus(StrEnum):
    FOOTING_VERIFIED = ValidationStatus.FOOTING_VERIFIED.value
    CONFIRMED_BY_MAJOR_AGGREGATE = ValidationStatus.CONFIRMED_BY_MAJOR_AGGREGATE.value
    RECOMPUTED_SUBTOTAL = ValidationStatus.RECOMPUTED_SUBTOTAL.value
    VERIFIED_COMPONENT = ValidationStatus.VERIFIED_COMPONENT.value
    UNRECONCILED_COMPONENT = ValidationStatus.UNRECONCILED_COMPONENT.value
    ELIMINATED_DISCLOSURE = ValidationStatus.ELIMINATED_DISCLOSURE.value
    STANDALONE_DISCLOSURE = ValidationStatus.STANDALONE_DISCLOSURE.value
    UNRECONCILED_DIFFERENCE = ValidationStatus.UNRECONCILED_DIFFERENCE.value
    MISSING = "MISSING"


class StatementType(StrEnum):
    BALANCE_STATEMENT = "balance_statement"
    INCOME_STATEMENT = "income_statement"
    CASHFLOW_STATEMENT = "cashflow_statement"


class CanonicalDiagnosticRecord(Model):
    emiten_code: str
    year: int
    period: Period
    statement: str
    entry_point: str
    variant: str
    canonical_code: str
    canonical_account: str
    validation_status: DiagnosticValidationStatus
    reported_value: float | None = None
    value: float | None = None
    difference: float | None = None
    issue_type: DiagnosticIssueType
    target_manual_filename: str
    sector: str | None = None
    subsector: str | None = None


def canonical_diagnostics(
    unified_canonical_accounts: pt.DataFrame[CanonicalAccount],
    canonical_registry: CanonicalRegistry,
    dei_metadata: pt.DataFrame[DeiMetadata] | None = None,
) -> pt.DataFrame[CanonicalDiagnosticRecord]:
    """Generates a complete diagnostic worklist of invalid, missing, or unbalanced accounts.

    This mart provides actionable backfill targets with expected file paths and entry-point
    classifications without magic strings.
    """
    if unified_canonical_accounts.is_empty() and (
        dei_metadata is None or dei_metadata.is_empty()
    ):
        return CanonicalDiagnosticRecord.DataFrame()

    frames: list[pl.DataFrame] = []

    # 1. Detect INVALID_FOOTING accounts (unusable due to footing errors)
    if not unified_canonical_accounts.is_empty():
        invalid_footing = (
            unified_canonical_accounts.filter(~CanonicalAccount.c.is_usable)
            .with_columns(
                difference=(
                    CanonicalAccount.c.reported_value - CanonicalAccount.c.value
                ),
                issue_type=pl.lit(DiagnosticIssueType.INVALID_FOOTING.value),
                target_manual_filename=pl.concat_str(
                    [
                        CanonicalAccount.c.emiten_code,
                        pl.lit("_"),
                        CanonicalAccount.c.year.cast(pl.Utf8),
                        pl.lit("_"),
                        CanonicalAccount.c.period,
                        pl.lit("_"),
                        CanonicalAccount.c.statement,
                        pl.lit(".csv"),
                    ]
                ),
            )
            .select(
                CanonicalDiagnosticRecord.n.emiten_code,
                CanonicalDiagnosticRecord.n.year,
                CanonicalDiagnosticRecord.n.period,
                CanonicalDiagnosticRecord.n.statement,
                CanonicalDiagnosticRecord.n.entry_point,
                CanonicalDiagnosticRecord.n.variant,
                CanonicalDiagnosticRecord.n.canonical_code,
                CanonicalDiagnosticRecord.n.canonical_account,
                CanonicalDiagnosticRecord.n.validation_status,
                CanonicalDiagnosticRecord.n.reported_value,
                CanonicalDiagnosticRecord.n.value,
                CanonicalDiagnosticRecord.n.difference,
                CanonicalDiagnosticRecord.n.issue_type,
                CanonicalDiagnosticRecord.n.target_manual_filename,
                CanonicalDiagnosticRecord.n.sector,
                CanonicalDiagnosticRecord.n.subsector,
            )
        )
        if not invalid_footing.is_empty():
            frames.append(invalid_footing)

    # 2. Detect MISSING_CANONICAL accounts (expected by catalog for given classification, but absent)
    if not unified_canonical_accounts.is_empty() and canonical_registry.catalog:
        filings = unified_canonical_accounts.select(
            CanonicalAccount.n.emiten_code,
            CanonicalAccount.n.year,
            CanonicalAccount.n.period,
            CanonicalAccount.n.statement,
            CanonicalAccount.n.entry_point,
            CanonicalAccount.n.variant,
            CanonicalAccount.n.sector,
            CanonicalAccount.n.subsector,
        ).unique()

        # Build expected canonical accounts per classification
        expected_rows: list[dict[str, Any]] = []
        unique_classifications = filings.select(
            CanonicalAccount.n.entry_point,
            CanonicalAccount.n.statement,
            CanonicalAccount.n.variant,
        ).unique().to_dicts()

        for c_dict in unique_classifications:
            classification = StatementClassification(
                entry_point=c_dict[CanonicalAccount.n.entry_point],
                statement=c_dict[CanonicalAccount.n.statement],
                variant=c_dict[CanonicalAccount.n.variant],
            )
            specs = canonical_registry.catalog.expected_for(classification)
            for spec in specs:
                expected_rows.append(
                    {
                        CanonicalAccount.n.entry_point: classification.entry_point,
                        CanonicalAccount.n.statement: classification.statement,
                        CanonicalAccount.n.variant: classification.variant,
                        CanonicalAccount.n.canonical_code: spec.code,
                        CanonicalAccount.n.canonical_account: spec.canonical_account,
                    }
                )

        if expected_rows:
            expected_df = pl.DataFrame(expected_rows)
            # Cross join filings with expected specs matching their classification
            filings_with_expected = filings.join(
                expected_df,
                on=[
                    CanonicalAccount.n.entry_point,
                    CanonicalAccount.n.statement,
                    CanonicalAccount.n.variant,
                ],
                how="inner",
            )

            # Anti-join against observed accounts to find which ones were omitted
            missing_canonicals = filings_with_expected.join(
                unified_canonical_accounts.select(
                    CanonicalAccount.n.emiten_code,
                    CanonicalAccount.n.year,
                    CanonicalAccount.n.period,
                    CanonicalAccount.n.canonical_code,
                ),
                on=[
                    CanonicalAccount.n.emiten_code,
                    CanonicalAccount.n.year,
                    CanonicalAccount.n.period,
                    CanonicalAccount.n.canonical_code,
                ],
                how="anti",
            ).with_columns(
                validation_status=pl.lit(DiagnosticValidationStatus.MISSING.value),
                reported_value=pl.lit(None, dtype=pl.Float64),
                value=pl.lit(None, dtype=pl.Float64),
                difference=pl.lit(None, dtype=pl.Float64),
                issue_type=pl.lit(DiagnosticIssueType.MISSING_CANONICAL.value),
                target_manual_filename=pl.concat_str(
                    [
                        pl.col(CanonicalAccount.n.emiten_code),
                        pl.lit("_"),
                        pl.col(CanonicalAccount.n.year).cast(pl.Utf8),
                        pl.lit("_"),
                        pl.col(CanonicalAccount.n.period),
                        pl.lit("_"),
                        pl.col(CanonicalAccount.n.statement),
                        pl.lit(".csv"),
                    ]
                ),
            ).select(
                CanonicalDiagnosticRecord.n.emiten_code,
                CanonicalDiagnosticRecord.n.year,
                CanonicalDiagnosticRecord.n.period,
                CanonicalDiagnosticRecord.n.statement,
                CanonicalDiagnosticRecord.n.entry_point,
                CanonicalDiagnosticRecord.n.variant,
                CanonicalDiagnosticRecord.n.canonical_code,
                CanonicalDiagnosticRecord.n.canonical_account,
                CanonicalDiagnosticRecord.n.validation_status,
                CanonicalDiagnosticRecord.n.reported_value,
                CanonicalDiagnosticRecord.n.value,
                CanonicalDiagnosticRecord.n.difference,
                CanonicalDiagnosticRecord.n.issue_type,
                CanonicalDiagnosticRecord.n.target_manual_filename,
                CanonicalDiagnosticRecord.n.sector,
                CanonicalDiagnosticRecord.n.subsector,
            )

            if not missing_canonicals.is_empty():
                frames.append(missing_canonicals)

    # 3. Detect MISSING_FILING (where an emiten has no records for an expected period)
    if dei_metadata is not None and not dei_metadata.is_empty():
        observed_periods = dei_metadata.select(
            DeiMetadata.n.year,
            DeiMetadata.n.period,
        ).unique()

        emitens = dei_metadata.select(
            DeiMetadata.n.emiten_code,
            DeiMetadata.n.Sector,
            DeiMetadata.n.Subsector,
        ).unique(subset=[DeiMetadata.n.emiten_code])

        all_expected_filings = emitens.join(observed_periods, how="cross")
        actual_filings = dei_metadata.select(
            DeiMetadata.n.emiten_code,
            DeiMetadata.n.year,
            DeiMetadata.n.period,
        ).unique()

        missing_filings = all_expected_filings.join(
            actual_filings,
            on=[
                DeiMetadata.n.emiten_code,
                DeiMetadata.n.year,
                DeiMetadata.n.period,
            ],
            how="anti",
        )

        if not missing_filings.is_empty():
            # Lookup historical entry point & variant for emiten if available
            historical_profile: pl.DataFrame | None = None
            if not unified_canonical_accounts.is_empty():
                historical_profile = unified_canonical_accounts.select(
                    CanonicalAccount.n.emiten_code,
                    CanonicalAccount.n.entry_point,
                    CanonicalAccount.n.statement,
                    CanonicalAccount.n.variant,
                ).unique(subset=[CanonicalAccount.n.emiten_code, CanonicalAccount.n.statement])

            if historical_profile is not None and not historical_profile.is_empty():
                missing_filing_records = missing_filings.join(
                    historical_profile,
                    on=DeiMetadata.n.emiten_code,
                    how="left",
                ).with_columns(
                    entry_point=pl.col("entry_point").fill_null(pl.lit("general")),
                    statement=pl.col("statement").fill_null(
                        pl.lit(StatementType.BALANCE_STATEMENT.value)
                    ),
                    variant=pl.col("variant").fill_null(pl.lit("current_and_non_current")),
                )
            else:
                missing_filing_records = missing_filings.with_columns(
                    entry_point=pl.lit("general"),
                    statement=pl.lit(StatementType.BALANCE_STATEMENT.value),
                    variant=pl.lit("current_and_non_current"),
                )

            formatted_missing_filings = missing_filing_records.with_columns(
                canonical_code=pl.lit("ALL"),
                canonical_account=pl.lit("FilingMissing"),
                validation_status=pl.lit(DiagnosticValidationStatus.MISSING.value),
                reported_value=pl.lit(None, dtype=pl.Float64),
                value=pl.lit(None, dtype=pl.Float64),
                difference=pl.lit(None, dtype=pl.Float64),
                issue_type=pl.lit(DiagnosticIssueType.MISSING_FILING.value),
                sector=pl.col(DeiMetadata.n.Sector),
                subsector=pl.col(DeiMetadata.n.Subsector),
                target_manual_filename=pl.concat_str(
                    [
                        pl.col(DeiMetadata.n.emiten_code),
                        pl.lit("_"),
                        pl.col(DeiMetadata.n.year).cast(pl.Utf8),
                        pl.lit("_"),
                        pl.col(DeiMetadata.n.period),
                        pl.lit("_"),
                        pl.col("statement"),
                        pl.lit(".csv"),
                    ]
                ),
            ).select(
                CanonicalDiagnosticRecord.n.emiten_code,
                CanonicalDiagnosticRecord.n.year,
                CanonicalDiagnosticRecord.n.period,
                CanonicalDiagnosticRecord.n.statement,
                CanonicalDiagnosticRecord.n.entry_point,
                CanonicalDiagnosticRecord.n.variant,
                CanonicalDiagnosticRecord.n.canonical_code,
                CanonicalDiagnosticRecord.n.canonical_account,
                CanonicalDiagnosticRecord.n.validation_status,
                CanonicalDiagnosticRecord.n.reported_value,
                CanonicalDiagnosticRecord.n.value,
                CanonicalDiagnosticRecord.n.difference,
                CanonicalDiagnosticRecord.n.issue_type,
                CanonicalDiagnosticRecord.n.target_manual_filename,
                CanonicalDiagnosticRecord.n.sector,
                CanonicalDiagnosticRecord.n.subsector,
            )

            if not formatted_missing_filings.is_empty():
                frames.append(formatted_missing_filings)

    if not frames:
        return CanonicalDiagnosticRecord.DataFrame()

    combined = pl.concat(frames, how="vertical").sort(
        CanonicalDiagnosticRecord.n.emiten_code,
        CanonicalDiagnosticRecord.n.year,
        CanonicalDiagnosticRecord.n.period,
        CanonicalDiagnosticRecord.n.statement,
        CanonicalDiagnosticRecord.n.canonical_code,
    )
    return CanonicalDiagnosticRecord.validate(combined)


def serialize_account_node(node: AccountNode, depth: int = 0) -> dict[str, Any]:
    return {
        "account": node.account,
        "code": node.code,
        "is_total": node.is_total,
        "weight": node.weight,
        "depth": depth,
        "children": [
            serialize_account_node(child, depth + 1) for child in node.children
        ],
    }


def flatten_tree_accounts(
    node: AccountNode, default_context: str, depth: int = 0
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = [
        {
            "account": node.account,
            "code": node.code,
            "is_total": node.is_total,
            "weight": node.weight,
            "depth": depth,
            "context": default_context,
        }
    ]
    for child in node.children:
        items.extend(flatten_tree_accounts(child, default_context, depth + 1))
    return items


def data_quality_report_html(
    canonical_diagnostics: pt.DataFrame[CanonicalDiagnosticRecord],
    statement_schema_registry: StatementSchemaRegistry,
    output_dir: str = "docs/data_quality",
    output_path: str | None = None,
) -> Path:
    """Generates an interactive, responsive HTML audit dashboard for manual backfilling.

    The data and full statement taxonomy trees are decoupled into separate JSON and JS files
    inside the designated directory (e.g., `docs/data_quality/`), providing instant page loads
    without DOM lag and complete CSV/JSON templates of the full calculation trees.
    """
    destination = Path(output_path or output_dir)
    if destination.suffix == ".html":
        html_path = destination
        folder = destination.parent
    else:
        folder = destination
        html_path = folder / "index.html"

    folder.mkdir(parents=True, exist_ok=True)
    json_path = folder / "records.json"
    js_path = folder / "records.js"
    trees_json_path = folder / "statement_trees.json"
    trees_js_path = folder / "statement_trees.js"

    # Build taxonomy trees catalog for all classifications
    statement_trees: dict[str, Any] = {}
    for classification, schema in statement_schema_registry.registry.items():
        key = f"{classification.entry_point}_{classification.statement}_{classification.variant}"
        default_context = (
            "CurrentYearInstant"
            if classification.statement == StatementType.BALANCE_STATEMENT.value
            else "CurrentYearDuration"
        )
        tree_roots = [
            serialize_account_node(root) for root in schema.chart_of_accounts
        ]
        flat_list: list[dict[str, Any]] = []
        for root in schema.chart_of_accounts:
            flat_list.extend(flatten_tree_accounts(root, default_context))

        csv_rows = ["account,value,context"]
        for item in flat_list:
            if item["account"]:
                csv_rows.append(f"{item['account']},,{item['context']}")
        csv_template = "\n".join(csv_rows)

        statement_trees[key] = {
            "entry_point": classification.entry_point,
            "statement": classification.statement,
            "variant": classification.variant,
            "context": default_context,
            "account_count": len([i for i in flat_list if i["account"]]),
            "tree": tree_roots,
            "flat_accounts": flat_list,
            "csv_template": csv_template,
        }

    trees_json = json.dumps(statement_trees)
    trees_json_path.write_text(json.dumps(statement_trees, indent=2), encoding="utf-8")
    trees_js_path.write_text(f"window.__STATEMENT_TREES__ = {trees_json};", encoding="utf-8")

    records = (
        canonical_diagnostics.to_dicts()
        if not canonical_diagnostics.is_empty()
        else []
    )

    total_records = len(records)
    invalid_footing_count = sum(
        1 for r in records if r["issue_type"] == DiagnosticIssueType.INVALID_FOOTING.value
    )
    missing_canonical_count = sum(
        1 for r in records if r["issue_type"] == DiagnosticIssueType.MISSING_CANONICAL.value
    )
    missing_filing_count = sum(
        1 for r in records if r["issue_type"] == DiagnosticIssueType.MISSING_FILING.value
    )

    # Group granular account issues by unique filing (emiten_code, year, period)
    filings_map: dict[tuple[str, int, str], dict[str, Any]] = collections.defaultdict(
        lambda: {
            "emiten_code": "",
            "year": 0,
            "period": "",
            "sector": "",
            "subsector": "",
            "entry_point": "",
            "variant": "",
            "total_issues": 0,
            "invalid_footing_count": 0,
            "missing_canonical_count": 0,
            "missing_filing_count": 0,
            "statements": set(),
            "target_files": set(),
            "issues": [],
        }
    )

    for r in records:
        key = (r["emiten_code"], r["year"], r["period"])
        item = filings_map[key]
        item["emiten_code"] = r["emiten_code"]
        item["year"] = r["year"]
        item["period"] = r["period"]
        if r.get("sector") and not item["sector"]:
            item["sector"] = r["sector"]
        if r.get("subsector") and not item["subsector"]:
            item["subsector"] = r["subsector"]
        if r.get("entry_point") and not item["entry_point"]:
            item["entry_point"] = r["entry_point"]
        if r.get("variant") and not item["variant"]:
            item["variant"] = r["variant"]

        item["total_issues"] += 1
        if r["issue_type"] == DiagnosticIssueType.INVALID_FOOTING.value:
            item["invalid_footing_count"] += 1
        elif r["issue_type"] == DiagnosticIssueType.MISSING_CANONICAL.value:
            item["missing_canonical_count"] += 1
        elif r["issue_type"] == DiagnosticIssueType.MISSING_FILING.value:
            item["missing_filing_count"] += 1

        if r.get("statement"):
            item["statements"].add(r["statement"])
        if r.get("target_manual_filename"):
            item["target_files"].add(r["target_manual_filename"])

        item["issues"].append({
            "statement": r.get("statement", ""),
            "entry_point": r.get("entry_point", ""),
            "variant": r.get("variant", ""),
            "canonical_code": r.get("canonical_code", ""),
            "canonical_account": r.get("canonical_account", ""),
            "validation_status": r.get("validation_status", ""),
            "reported_value": r.get("reported_value"),
            "value": r.get("value"),
            "difference": r.get("difference"),
            "issue_type": r.get("issue_type", ""),
            "target_manual_filename": r.get("target_manual_filename", ""),
        })

    grouped_filings: list[dict[str, Any]] = []
    for item in filings_map.values():
        item["statements"] = sorted(item["statements"])
        item["target_files"] = sorted(item["target_files"])
        grouped_filings.append(item)

    grouped_filings.sort(
        key=lambda x: (
            -x["year"],
            -PERIOD_ORDER.get(x["period"], 0),
            x["emiten_code"],
        )
    )

    unique_filings_affected = len(grouped_filings)

    records_json = json.dumps(grouped_filings)

    # 1. Write standalone JSON for programmatic access / API consumers
    json_path.write_text(records_json, encoding="utf-8")

    # 2. Write JS wrapper so browsers opening via file:// protocol bypass CORS restrictions
    js_path.write_text(f"window.__DATA_QUALITY_RECORDS__ = {records_json};", encoding="utf-8")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IDX Financial Statement Quality & Backfill Audit</title>
<style>
  :root {{
    --background: #fafafa;
    --foreground: #09090b;
    --card: #ffffff;
    --card-foreground: #09090b;
    --muted: #f4f4f5;
    --muted-foreground: #71717a;
    --border: #e4e4e7;
    --input: #e4e4e7;
    --ring: #18181b;
    --primary: #18181b;
    --primary-foreground: #fafafa;
    --secondary: #f4f4f5;
    --secondary-foreground: #18181b;
    --radius: 0.5rem;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background-color: var(--background);
    color: var(--foreground);
    padding: 32px 24px;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }}

  .header {{
    margin-bottom: 28px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}

  .header h1 {{
    font-size: 24px;
    font-weight: 700;
    letter-spacing: -0.025em;
    color: var(--foreground);
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .header p {{
    color: var(--muted-foreground);
    font-size: 14px;
  }}

  .kpi-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }}

  .card {{
    background-color: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 18px 20px;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);
    transition: box-shadow 0.15s ease, border-color 0.15s ease;
  }}

  .card:hover {{
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    border-color: #d4d4d8;
  }}

  .card-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
  }}

  .card-title {{
    font-size: 13px;
    font-weight: 500;
    color: var(--muted-foreground);
    letter-spacing: -0.01em;
  }}

  .card-icon {{
    color: var(--muted-foreground);
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .card-value {{
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.025em;
    font-variant-numeric: tabular-nums;
    color: var(--foreground);
  }}

  .card-desc {{
    font-size: 12px;
    color: var(--muted-foreground);
    margin-top: 4px;
  }}

  .controls-panel {{
    background-color: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 14px 18px;
    margin-bottom: 24px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: flex-end;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);
  }}

  .control-group {{
    display: flex;
    flex-direction: column;
    gap: 5px;
    min-width: 120px;
  }}

  .control-label {{
    font-size: 11px;
    font-weight: 500;
    color: var(--muted-foreground);
    letter-spacing: 0.01em;
  }}

  .control-input, .control-select {{
    background-color: var(--card);
    border: 1px solid var(--input);
    color: var(--foreground);
    padding: 0 10px;
    border-radius: 6px;
    font-size: 12px;
    height: 32px;
    outline: none;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
    font-family: inherit;
  }}

  .control-input:focus, .control-select:focus {{
    border-color: var(--ring);
    box-shadow: 0 0 0 1px var(--ring);
  }}

  .control-input::placeholder {{
    color: #a1a1aa;
  }}

  .search-input-wrapper {{
    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
  }}

  .search-input-wrapper .search-icon {{
    position: absolute;
    left: 10px;
    color: var(--muted-foreground);
    pointer-events: none;
  }}

  .search-input-wrapper .control-input {{
    padding-left: 30px;
    width: 100%;
  }}

  /* Custom Selection Dropdown (Shadcn-UI Popover/Listbox style) */
  .cselect-wrapper {{
    position: relative;
    user-select: none;
  }}
  .cselect-wrapper[data-for="yearFilter"] {{ min-width: 125px; }}
  .cselect-wrapper[data-for="periodFilter"] {{ min-width: 130px; }}
  .cselect-wrapper[data-for="issueFilter"] {{ min-width: 250px; }}
  .cselect-wrapper[data-for="statementFilter"] {{ min-width: 240px; }}
  .cselect-wrapper[data-for="pageSizeSelect"] {{ min-width: 80px; }}

  .cselect-trigger {{
    display: inline-flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    height: 32px;
    padding: 0 10px;
    font-size: 12px;
    font-weight: 500;
    color: var(--foreground);
    background: var(--card);
    border: 1px solid var(--input);
    border-radius: 6px;
    cursor: pointer;
    outline: none;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
    width: 100%;
    text-align: left;
    font-family: inherit;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.02);
  }}
  .cselect-trigger:focus, .cselect-wrapper.open .cselect-trigger {{
    border-color: var(--ring);
    box-shadow: 0 0 0 1px var(--ring);
  }}
  .cselect-value {{
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    flex: 1;
  }}
  .cselect-chevron {{
    color: var(--muted-foreground);
    flex-shrink: 0;
    transition: transform 0.15s ease;
  }}
  .cselect-wrapper.open .cselect-chevron {{
    transform: rotate(180deg);
  }}
  .cselect-dropdown {{
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    min-width: 100%;
    width: max-content;
    max-width: 380px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 6px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.09), 0 1px 3px rgba(0, 0, 0, 0.04);
    z-index: 100;
    padding: 4px;
    display: none;
  }}
  .cselect-wrapper.open .cselect-dropdown {{
    display: block;
    animation: cselectFadeIn 0.12s ease-out;
  }}
  @keyframes cselectFadeIn {{
    from {{ opacity: 0; transform: translateY(-4px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  .cselect-wrapper[data-for="pageSizeSelect"] .cselect-dropdown {{
    left: auto;
    right: 0;
  }}
  .cselect-search-box {{
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 5px 8px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 4px;
  }}
  .cselect-search-icon {{
    color: var(--muted-foreground);
    flex-shrink: 0;
  }}
  .cselect-filter-input {{
    border: none;
    outline: none;
    background: transparent;
    font-size: 11.5px;
    color: var(--foreground);
    width: 100%;
    font-family: inherit;
  }}
  .cselect-options {{
    max-height: 240px;
    overflow-y: auto;
    scrollbar-width: thin;
  }}
  .cselect-group-header {{
    font-size: 9.5px;
    font-weight: 600;
    color: var(--muted-foreground);
    padding: 6px 8px 3px 8px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}
  .cselect-option {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    padding: 5px 8px;
    font-size: 11.5px;
    color: var(--foreground);
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.1s ease;
    white-space: nowrap;
  }}
  .cselect-option:hover, .cselect-option.focused {{
    background: var(--muted);
  }}
  .cselect-option.selected {{
    font-weight: 600;
    background: #f4f4f5;
  }}
  .cselect-check {{
    color: var(--foreground);
    opacity: 0;
    flex-shrink: 0;
  }}
  .cselect-option.selected .cselect-check {{
    opacity: 1;
  }}
  .cselect-empty {{
    padding: 12px 8px;
    font-size: 11.5px;
    color: var(--muted-foreground);
    text-align: center;
  }}

  .table-container {{
    background-color: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow-x: auto;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    text-align: left;
  }}

  thead th {{
    background-color: #fafafa;
    padding: 12px 16px;
    color: var(--muted-foreground);
    font-weight: 500;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 1px solid var(--border);
    white-space: nowrap;
  }}

  tbody tr {{
    border-bottom: 1px solid var(--border);
    transition: background-color 0.15s ease;
  }}

  tbody tr:hover {{
    background-color: #fafafa;
  }}

  tbody tr:last-child {{
    border-bottom: none;
  }}

  td {{
    padding: 12px 16px;
    vertical-align: middle;
  }}

  .badge {{
    display: inline-flex;
    align-items: center;
    padding: 2px 8px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 500;
    line-height: 1.4;
    border: 1px solid transparent;
    white-space: nowrap;
  }}

  .badge-danger {{
    background-color: #fef2f2;
    color: #ef4444;
    border-color: #fecaca;
  }}

  .badge-warning {{
    background-color: #fffbeb;
    color: #b45309;
    border-color: #fde68a;
  }}

  .badge-purple {{
    background-color: #faf5ff;
    color: #7e22ce;
    border-color: #e9d5ff;
  }}

  .badge-neutral {{
    background-color: #f4f4f5;
    color: #18181b;
    border-color: #e4e4e7;
  }}

  .btn-badge {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    line-height: 1.4;
    cursor: pointer;
    transition: all 0.15s ease;
    text-decoration: none;
    white-space: nowrap;
    font-family: inherit;
    border: 1px solid transparent;
  }}

  .btn-badge-danger {{
    background-color: #fef2f2;
    color: #ef4444;
    border-color: #fecaca;
  }}

  .btn-badge-danger:hover {{
    background-color: #fee2e2;
    border-color: #f87171;
    box-shadow: 0 1px 2px rgba(239, 68, 68, 0.15);
    transform: translateY(-1px);
  }}

  .btn-badge-warning {{
    background-color: #fffbeb;
    color: #b45309;
    border-color: #fde68a;
  }}

  .btn-badge-warning:hover {{
    background-color: #fef3c7;
    border-color: #fbbf24;
    box-shadow: 0 1px 2px rgba(180, 83, 9, 0.15);
    transform: translateY(-1px);
  }}

  .btn-badge-purple {{
    background-color: #faf5ff;
    color: #7e22ce;
    border-color: #e9d5ff;
  }}

  .btn-badge-purple:hover {{
    background-color: #f3e8ff;
    border-color: #c084fc;
    box-shadow: 0 1px 2px rgba(126, 34, 206, 0.15);
    transform: translateY(-1px);
  }}

  .code-cell {{
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 12px;
  }}

  .num-cell {{
    text-align: right;
    font-variant-numeric: tabular-nums;
  }}

  .btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 500;
    height: 32px;
    padding: 0 12px;
    cursor: pointer;
    transition: all 0.15s ease;
    border: 1px solid transparent;
    text-decoration: none;
    white-space: nowrap;
    gap: 6px;
  }}

  .btn-outline {{
    background-color: #ffffff;
    border-color: var(--border);
    color: var(--foreground);
  }}

  .btn-outline:hover:not(:disabled) {{
    background-color: var(--secondary);
    border-color: #d4d4d8;
  }}

  .btn-primary {{
    background-color: var(--primary);
    border-color: var(--primary);
    color: var(--primary-foreground);
  }}

  .btn-primary:hover:not(:disabled) {{
    background-color: #27272a;
  }}

  .btn-sm {{
    height: 28px;
    padding: 0 8px;
    font-size: 11px;
    border-radius: 4px;
  }}

  .btn:disabled {{
    opacity: 0.4;
    cursor: not-allowed;
  }}

  .pagination-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 16px;
    border-top: 1px solid var(--border);
    background-color: var(--card);
    font-size: 13px;
    color: var(--muted-foreground);
  }}

  .pagination-controls {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .toast {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    background-color: var(--primary);
    color: var(--primary-foreground);
    font-size: 13px;
    font-weight: 500;
    padding: 10px 16px;
    border-radius: 6px;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    pointer-events: none;
    z-index: 100;
  }}

  .toast.show {{
    opacity: 1;
    transform: translateY(0);
  }}

  .modal {{
    display: none;
    position: fixed;
    z-index: 50;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(4px);
    justify-content: center;
    align-items: center;
  }}

  .modal.show {{
    display: flex;
  }}

  #filingDetailModal {{
    z-index: 50;
  }}

  #treeModal {{
    z-index: 60;
  }}

  .modal-content {{
    background-color: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    width: 90%;
    max-width: 840px;
    max-height: 85vh;
    display: flex;
    flex-direction: column;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
  }}

  .modal-header {{
    padding: 16px 20px;
    border-bottom: 1px solid var(--border);
    background-color: #fafafa;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .modal-header h2 {{
    font-size: 15px;
    font-weight: 600;
    letter-spacing: -0.015em;
    color: var(--foreground);
  }}

  .modal-close {{
    color: var(--muted-foreground);
    font-size: 18px;
    font-weight: 500;
    cursor: pointer;
    line-height: 1;
    padding: 4px 8px;
    border-radius: 4px;
    transition: all 0.15s ease;
  }}

  .modal-close:hover {{
    color: var(--foreground);
    background-color: var(--secondary);
  }}

  .modal-toolbar {{
    padding: 12px 20px;
    background-color: var(--card);
    border-bottom: 1px solid var(--border);
    display: flex;
    gap: 8px;
    align-items: center;
  }}

  .modal-body {{
    padding: 16px 20px;
    overflow-y: auto;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 12px;
    background-color: #ffffff;
  }}

  .tree-node {{
    margin: 4px 0;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--foreground);
    font-size: 12px;
  }}

  .tree-node.is-total {{
    font-weight: 600;
  }}

  .weight-badge {{
    font-size: 10px;
    padding: 1px 5px;
    border-radius: 4px;
    font-weight: 600;
  }}

  .weight-pos {{
    background-color: #ecfdf5;
    color: #059669;
    border: 1px solid #a7f3d0;
  }}

  .weight-neg {{
    background-color: #fef2f2;
    color: #ef4444;
    border: 1px solid #fecaca;
  }}
</style>
<script src="records.js"></script>
<script src="statement_trees.js"></script>
</head>
<body>

<div class="header">
  <h1>
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
    Audit Kualitas Data &amp; Backfill Worklist
  </h1>
  <p>Katalog pengujian kepatuhan pelaporan keuangan: diskrepansi penjumlahan (footing), pengungkapan wajib taksonomi, dan verifikasi ketersediaan laporan.</p>
</div>

<div class="kpi-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-title">Laporan Terdampak</span>
      <span class="card-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>
      </span>
    </div>
    <div class="card-value">{unique_filings_affected}</div>
    <div class="card-desc">Laporan keuangan dengan temuan</div>
  </div>
  <div class="card">
    <div class="card-header">
      <span class="card-title">Total Temuan Audit</span>
      <span class="card-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>
      </span>
    </div>
    <div class="card-value" style="color: #b45309;">{total_records}</div>
    <div class="card-desc">Seluruh pos akun dengan diskrepansi</div>
  </div>
  <div class="card">
    <div class="card-header">
      <span class="card-title">Diskrepansi Penjumlahan</span>
      <span class="card-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg>
      </span>
    </div>
    <div class="card-value" style="color: #ef4444;">{invalid_footing_count}</div>
    <div class="card-desc">Selisih pengujian footing (tie-out)</div>
  </div>
  <div class="card">
    <div class="card-header">
      <span class="card-title">Pengungkapan Wajib Tidak Dilaporkan</span>
      <span class="card-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/></svg>
      </span>
    </div>
    <div class="card-value" style="color: #0284c7;">{missing_canonical_count}</div>
    <div class="card-desc">Pos taksonomi wajib yang dihilangkan</div>
  </div>
  <div class="card">
    <div class="card-header">
      <span class="card-title">Laporan Tidak Tersedia</span>
      <span class="card-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="m14.5 12.5-5 5"/><path d="m9.5 12.5 5 5"/></svg>
      </span>
    </div>
    <div class="card-value" style="color: #7e22ce;">{missing_filing_count}</div>
    <div class="card-desc">Laporan tidak tersedia</div>
  </div>
</div>

<div class="controls-panel">
  <div class="control-group" style="flex: 2; min-width: 240px;">
    <label class="control-label" for="searchFilter">Cari Emiten / Kode Akun</label>
    <div class="search-input-wrapper">
      <svg class="search-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <input type="text" id="searchFilter" class="control-input" placeholder="Ketik kode saham (misal: BBCA) atau kode akun...">
    </div>
  </div>
  <div class="control-group" style="min-width: 125px;">
    <label class="control-label" for="yearFilter">Tahun Buku</label>
    <select id="yearFilter" class="control-select">
      <option value="ALL">Semua Tahun</option>
    </select>
  </div>
  <div class="control-group" style="min-width: 130px;">
    <label class="control-label" for="periodFilter">Periode Pelaporan</label>
    <select id="periodFilter" class="control-select">
      <option value="ALL">Semua Periode</option>
    </select>
  </div>
  <div class="control-group" style="min-width: 250px;">
    <label class="control-label" for="issueFilter">Kategori Temuan Audit</label>
    <select id="issueFilter" class="control-select">
      <option value="ALL">Semua Kategori Temuan</option>
      <option value="{DiagnosticIssueType.INVALID_FOOTING.value}">Diskrepansi Penjumlahan (Footing)</option>
      <option value="{DiagnosticIssueType.MISSING_CANONICAL.value}">Pengungkapan Wajib Tidak Dilaporkan</option>
      <option value="{DiagnosticIssueType.MISSING_FILING.value}">Laporan Tidak Tersedia</option>
    </select>
  </div>
  <div class="control-group" style="min-width: 240px;">
    <label class="control-label" for="statementFilter">Jenis Laporan Keuangan</label>
    <select id="statementFilter" class="control-select">
      <option value="ALL">Semua Laporan Keuangan</option>
      <option value="balance_statement">Laporan Posisi Keuangan (Neraca)</option>
      <option value="income_statement">Laporan Laba Rugi</option>
      <option value="cashflow_statement">Laporan Arus Kas</option>
    </select>
  </div>
  <div class="control-group" style="min-width: 80px;">
    <label class="control-label" for="pageSizeSelect">Baris / Hal</label>
    <select id="pageSizeSelect" class="control-select">
      <option value="25">25</option>
      <option value="50" selected>50</option>
      <option value="100">100</option>
      <option value="250">250</option>
    </select>
  </div>
</div>

<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>Emiten</th>
        <th>Tahun</th>
        <th>Periode</th>
        <th>Sektor / Subsektor</th>
        <th>Entry Point</th>
        <th>Ringkasan Temuan Audit</th>
      </tr>
    </thead>
    <tbody id="tableBody">
    </tbody>
  </table>

  <div class="pagination-bar">
    <div id="paginationInfo">Menampilkan 0 dari 0 laporan</div>
    <div class="pagination-controls">
      <button id="btnFirstPage" class="btn btn-outline btn-sm">&laquo; Awal</button>
      <button id="btnPrevPage" class="btn btn-outline btn-sm">&lsaquo; Sebelumnya</button>
      <span id="pageCurrentInfo" style="margin: 0 8px; font-weight: 500; font-size: 12px; color: var(--foreground);">Halaman 1</span>
      <button id="btnNextPage" class="btn btn-outline btn-sm">Berikutnya &rsaquo;</button>
      <button id="btnLastPage" class="btn btn-outline btn-sm">Akhir &raquo;</button>
    </div>
  </div>
</div>

<div id="filingDetailModal" class="modal">
  <div class="modal-content" style="max-width: 1150px; width: 95%;">
    <div class="modal-header">
      <div>
        <h2 id="detailModalTitle">Rincian Temuan Audit</h2>
        <div id="detailModalSubtitle" style="font-size: 12px; color: var(--muted-foreground); margin-top: 4px;"></div>
      </div>
      <span class="modal-close" onclick="closeFilingDetailModal()">&times;</span>
    </div>
    <div id="detailModalToolbar" class="modal-toolbar" style="flex-direction: column; align-items: stretch; gap: 8px; background: #fafafa; padding: 14px 20px;"></div>
    <div class="modal-body" style="padding: 0; max-height: 55vh; overflow-y: auto;">
      <table style="width: 100%; font-size: 12px;">
        <thead>
          <tr>
            <th>Statement</th>
            <th>Variant</th>
            <th>Canonical Code</th>
            <th>Akun Canonical</th>
            <th>Kategori Temuan</th>
            <th>Status Validasi</th>
            <th class="num-cell">Nilai Dilaporkan</th>
            <th class="num-cell">Hasil Rekomputasi</th>
            <th class="num-cell">Selisih (&Delta;)</th>
          </tr>
        </thead>
        <tbody id="detailTableBody"></tbody>
      </table>
    </div>
  </div>
</div>

<div id="treeModal" class="modal">
  <div class="modal-content">
    <div class="modal-header">
      <h2 id="modalTitle">Hierarki Taksonomi Statement</h2>
      <span class="modal-close" onclick="closeTreeModal()">&times;</span>
    </div>
    <div class="modal-toolbar">
      <button class="btn btn-outline btn-sm" id="modalBtnCopyCsv">Copy Entire CSV Tree</button>
      <button class="btn btn-outline btn-sm" id="modalBtnCopyJson">Copy JSON Tree</button>
      <button class="btn btn-primary btn-sm" id="modalBtnDownload">Download CSV</button>
      <span id="modalAccountCount" style="margin-left: auto; color: var(--muted-foreground); font-size: 12px;"></span>
    </div>
    <div id="treeViewContainer" class="modal-body"></div>
  </div>
</div>

<div id="toast" class="toast">CSV Template Disalin ke Clipboard!</div>

<script>
let allRecords = window.__DATA_QUALITY_RECORDS__ || [];
let statementTrees = window.__STATEMENT_TREES__ || {{}};
let currentPage = 1;
let pageSize = 50;
let filteredRecords = [];
let searchDebounceTimer = null;

function formatNumber(val) {{
  if (val === null || val === undefined) return "-";
  return new Intl.NumberFormat('en-US', {{ maximumFractionDigits: 2 }}).format(val);
}}

function getIssueBadge(issue) {{
  if (issue === "{DiagnosticIssueType.INVALID_FOOTING.value}") {{
    return `<span class="badge badge-danger">DISKREPANSI FOOTING</span>`;
  }} else if (issue === "{DiagnosticIssueType.MISSING_CANONICAL.value}") {{
    return `<span class="badge badge-warning">PENGUNGKAPAN HILANG</span>`;
  }} else if (issue === "{DiagnosticIssueType.MISSING_FILING.value}") {{
    return `<span class="badge badge-purple">LAPORAN TIDAK TERSEDIA</span>`;
  }}
  return `<span class="badge badge-neutral">${{issue}}</span>`;
}}

function getTreeKey(ep, stmt, varnt) {{
  return `${{ep}}_${{stmt}}_${{varnt}}`;
}}

function getTreeInfo(ep, stmt, varnt) {{
  const key = getTreeKey(ep, stmt, varnt);
  return statementTrees[key] || null;
}}

function showToast(msg) {{
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2500);
}}

function copyCsvTree(ep, stmt, varnt) {{
  const info = getTreeInfo(ep, stmt, varnt);
  if (!info) {{
    showToast("Pohon taksonomi belum tersedia untuk varian ini.");
    return;
  }}
  navigator.clipboard.writeText(info.csv_template).then(() => {{
    showToast(`Pohon CSV Disalin! (${{info.account_count}} akun taksonomi)`);
  }});
}}

function copyJsonTree(ep, stmt, varnt) {{
  const info = getTreeInfo(ep, stmt, varnt);
  if (!info) {{
    showToast("Pohon taksonomi belum tersedia.");
    return;
  }}
  const jsonStr = JSON.stringify(info.tree, null, 2);
  navigator.clipboard.writeText(jsonStr).then(() => {{
    showToast(`Pohon JSON Disalin! (${{info.account_count}} akun taksonomi)`);
  }});
}}

function downloadCsv(filename, ep, stmt, varnt) {{
  const info = getTreeInfo(ep, stmt, varnt);
  if (!info) {{
    showToast("Pohon taksonomi belum tersedia.");
    return;
  }}
  const blob = new Blob([info.csv_template], {{ type: "text/csv;charset=utf-8;" }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  showToast(`Mengunduh ${{filename}}...`);
}}

function openTreeModal(ep, stmt, varnt) {{
  const info = getTreeInfo(ep, stmt, varnt);
  if (!info) {{
    showToast("Pohon taksonomi belum tersedia.");
    return;
  }}
  document.getElementById("modalTitle").textContent = `${{ep}} \u203a ${{stmt}} \u203a ${{varnt}}`;
  document.getElementById("modalAccountCount").textContent = `${{info.account_count}} akun terdaftar`;

  document.getElementById("modalBtnCopyCsv").onclick = () => copyCsvTree(ep, stmt, varnt);
  document.getElementById("modalBtnCopyJson").onclick = () => copyJsonTree(ep, stmt, varnt);
  document.getElementById("modalBtnDownload").onclick = () => downloadCsv(`${{ep}}_${{stmt}}_${{varnt}}.csv`, ep, stmt, varnt);

  const container = document.getElementById("treeViewContainer");
  container.innerHTML = renderTreeNodesHtml(info.tree);
  document.getElementById("treeModal").classList.add("show");
}}

function closeTreeModal() {{
  document.getElementById("treeModal").classList.remove("show");
}}

function renderTreeNodesHtml(nodes) {{
  if (!nodes || nodes.length === 0) return "";
  return nodes.map(node => {{
    const indent = (node.depth || 0) * 20;
    const isTotal = node.is_total;
    const weightClass = node.weight < 0 ? "weight-neg" : "weight-pos";
    const weightSign = node.weight < 0 ? "-1" : "+1";
    const childrenHtml = renderTreeNodesHtml(node.children);

    return `
      <div style="padding-left: ${{indent}}px;">
        <div class="tree-node ${{isTotal ? 'is-total' : ''}}">
          <span class="weight-badge ${{weightClass}}">${{weightSign}}</span>
          <span>${{node.account}}</span>
          <span style="color: var(--muted-foreground); font-size: 11px;">(${{node.code}})</span>
        </div>
        ${{childrenHtml}}
      </div>
    `;
  }}).join("");
}}

function closeAllCustomSelects(exceptWrapper) {{
  document.querySelectorAll(".cselect-wrapper.open").forEach(w => {{
    if (w !== exceptWrapper) {{
      w.classList.remove("open");
      const btn = w.querySelector(".cselect-trigger");
      if (btn) btn.setAttribute("aria-expanded", "false");
    }}
  }});
}}

document.addEventListener("click", (e) => {{
  if (!e.target.closest(".cselect-wrapper")) {{
    closeAllCustomSelects();
  }}
}});

document.addEventListener("keydown", (e) => {{
  if (e.key === "Escape") {{
    closeAllCustomSelects();
  }}
}});

function filterCustomSelect(wrapper, query) {{
  const q = query.trim().toLowerCase();
  const options = wrapper.querySelectorAll(".cselect-option");
  let visibleCount = 0;

  options.forEach(opt => {{
    const txt = (opt.textContent || "").toLowerCase();
    const match = !q || txt.includes(q);
    opt.style.display = match ? "flex" : "none";
    if (match) visibleCount++;
  }});

  let emptyEl = wrapper.querySelector(".cselect-empty");
  if (visibleCount === 0) {{
    if (!emptyEl) {{
      emptyEl = document.createElement("div");
      emptyEl.className = "cselect-empty";
      emptyEl.textContent = "Tidak ada hasil ditemukan";
      const optsList = wrapper.querySelector(".cselect-options");
      if (optsList) optsList.appendChild(emptyEl);
    }}
    emptyEl.style.display = "block";
  }} else if (emptyEl) {{
    emptyEl.style.display = "none";
  }}
}}

function buildCustomSelectOptions(wrapper, selectEl) {{
  const optsContainer = wrapper.querySelector(".cselect-options");
  if (!optsContainer) return;
  optsContainer.innerHTML = "";

  const currentVal = selectEl.value;

  function createOptionItem(opt) {{
    const item = document.createElement("div");
    item.className = "cselect-option" + (opt.value === currentVal ? " selected" : "");
    item.setAttribute("data-value", opt.value);
    item.setAttribute("role", "option");
    item.setAttribute("aria-selected", opt.value === currentVal ? "true" : "false");

    const textSpan = document.createElement("span");
    textSpan.style.overflow = "hidden";
    textSpan.style.textOverflow = "ellipsis";
    textSpan.style.whiteSpace = "nowrap";
    textSpan.textContent = opt.textContent;
    item.appendChild(textSpan);

    const checkSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    checkSvg.setAttribute("class", "cselect-check");
    checkSvg.setAttribute("width", "13");
    checkSvg.setAttribute("height", "13");
    checkSvg.setAttribute("viewBox", "0 0 24 24");
    checkSvg.setAttribute("fill", "none");
    checkSvg.setAttribute("stroke", "currentColor");
    checkSvg.setAttribute("stroke-width", "2.5");
    checkSvg.setAttribute("stroke-linecap", "round");
    checkSvg.setAttribute("stroke-linejoin", "round");
    const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    polyline.setAttribute("points", "20 6 9 17 4 12");
    checkSvg.appendChild(polyline);
    item.appendChild(checkSvg);

    item.addEventListener("click", (e) => {{
      e.stopPropagation();
      selectEl.value = opt.value;
      wrapper.classList.remove("open");
      selectEl.dispatchEvent(new Event("change", {{ bubbles: true }}));
      syncCustomSelect(selectEl);
    }});

    return item;
  }}

  Array.from(selectEl.children).forEach(child => {{
    if (child.tagName === "OPTION") {{
      optsContainer.appendChild(createOptionItem(child));
    }}
  }});

  const valEl = wrapper.querySelector(".cselect-value");
  if (valEl) {{
    const selOpt = selectEl.options[selectEl.selectedIndex];
    valEl.textContent = selOpt ? selOpt.textContent : (selectEl.value || "Pilih...");
  }}
}}

function initCustomSelect(selectEl, opts = {{}}) {{
  if (!selectEl) return;
  const searchable = !!opts.searchable;

  let wrapper = selectEl.nextElementSibling;
  if (!wrapper || !wrapper.classList.contains("cselect-wrapper") || wrapper.getAttribute("data-for") !== selectEl.id) {{
    wrapper = document.createElement("div");
    wrapper.className = "cselect-wrapper";
    wrapper.setAttribute("data-for", selectEl.id);

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "cselect-trigger";
    trigger.setAttribute("aria-haspopup", "listbox");
    trigger.setAttribute("aria-expanded", "false");

    const valSpan = document.createElement("span");
    valSpan.className = "cselect-value";
    trigger.appendChild(valSpan);

    const chevronSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    chevronSvg.setAttribute("class", "cselect-chevron");
    chevronSvg.setAttribute("width", "13");
    chevronSvg.setAttribute("height", "13");
    chevronSvg.setAttribute("viewBox", "0 0 24 24");
    chevronSvg.setAttribute("fill", "none");
    chevronSvg.setAttribute("stroke", "currentColor");
    chevronSvg.setAttribute("stroke-width", "2");
    chevronSvg.setAttribute("stroke-linecap", "round");
    chevronSvg.setAttribute("stroke-linejoin", "round");
    const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    polyline.setAttribute("points", "6 9 12 15 18 9");
    chevronSvg.appendChild(polyline);
    trigger.appendChild(chevronSvg);

    const dropdown = document.createElement("div");
    dropdown.className = "cselect-dropdown";

    if (searchable) {{
      const sBox = document.createElement("div");
      sBox.className = "cselect-search-box";

      const sIcon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      sIcon.setAttribute("class", "cselect-search-icon");
      sIcon.setAttribute("width", "12");
      sIcon.setAttribute("height", "12");
      sIcon.setAttribute("viewBox", "0 0 24 24");
      sIcon.setAttribute("fill", "none");
      sIcon.setAttribute("stroke", "currentColor");
      sIcon.setAttribute("stroke-width", "2");
      sIcon.setAttribute("stroke-linecap", "round");
      sIcon.setAttribute("stroke-linejoin", "round");
      const sCircle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      sCircle.setAttribute("cx", "11");
      sCircle.setAttribute("cy", "11");
      sCircle.setAttribute("r", "8");
      const sLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
      sLine.setAttribute("x1", "21");
      sLine.setAttribute("y1", "21");
      sLine.setAttribute("x2", "16.65");
      sLine.setAttribute("y2", "16.65");
      sIcon.appendChild(sCircle);
      sIcon.appendChild(sLine);
      sBox.appendChild(sIcon);

      const fInput = document.createElement("input");
      fInput.type = "text";
      fInput.className = "cselect-filter-input";
      fInput.placeholder = "Cari...";
      fInput.autocomplete = "off";
      fInput.addEventListener("input", (e) => {{
        filterCustomSelect(wrapper, e.target.value);
      }});
      fInput.addEventListener("click", (e) => e.stopPropagation());
      sBox.appendChild(fInput);

      dropdown.appendChild(sBox);
    }}

    const optsDiv = document.createElement("div");
    optsDiv.className = "cselect-options";
    optsDiv.setAttribute("role", "listbox");
    dropdown.appendChild(optsDiv);

    wrapper.appendChild(trigger);
    wrapper.appendChild(dropdown);

    selectEl.style.display = "none";
    selectEl.parentNode.insertBefore(wrapper, selectEl.nextSibling);

    trigger.addEventListener("click", (e) => {{
      e.stopPropagation();
      const isOpen = wrapper.classList.contains("open");
      closeAllCustomSelects(wrapper);
      if (!isOpen) {{
        wrapper.classList.add("open");
        trigger.setAttribute("aria-expanded", "true");
        if (searchable) {{
          const fi = wrapper.querySelector(".cselect-filter-input");
          if (fi) {{
            fi.value = "";
            filterCustomSelect(wrapper, "");
            setTimeout(() => fi.focus(), 30);
          }}
        }}
        const selOpt = wrapper.querySelector(".cselect-option.selected");
        if (selOpt) {{
          selOpt.scrollIntoView({{ block: "nearest" }});
        }}
      }} else {{
        wrapper.classList.remove("open");
        trigger.setAttribute("aria-expanded", "false");
      }}
    }});

    wrapper.addEventListener("keydown", (e) => {{
      if (!wrapper.classList.contains("open")) return;
      const visibleOpts = Array.from(wrapper.querySelectorAll(".cselect-option")).filter(
        o => o.style.display !== "none"
      );
      if (visibleOpts.length === 0) return;

      let focusedIdx = visibleOpts.findIndex(o => o.classList.contains("focused"));
      if (e.key === "ArrowDown") {{
        e.preventDefault();
        if (focusedIdx >= 0) visibleOpts[focusedIdx].classList.remove("focused");
        focusedIdx = (focusedIdx + 1) % visibleOpts.length;
        visibleOpts[focusedIdx].classList.add("focused");
        visibleOpts[focusedIdx].scrollIntoView({{ block: "nearest" }});
      }} else if (e.key === "ArrowUp") {{
        e.preventDefault();
        if (focusedIdx >= 0) visibleOpts[focusedIdx].classList.remove("focused");
        focusedIdx = (focusedIdx - 1 + visibleOpts.length) % visibleOpts.length;
        visibleOpts[focusedIdx].classList.add("focused");
        visibleOpts[focusedIdx].scrollIntoView({{ block: "nearest" }});
      }} else if (e.key === "Enter") {{
        e.preventDefault();
        if (focusedIdx >= 0 && visibleOpts[focusedIdx]) {{
          visibleOpts[focusedIdx].click();
        }} else {{
          const sel = wrapper.querySelector(".cselect-option.selected");
          if (sel && sel.style.display !== "none") sel.click();
        }}
      }}
    }});
  }}

  buildCustomSelectOptions(wrapper, selectEl);
}}

function syncCustomSelect(selectEl) {{
  if (!selectEl) return;
  const wrapper = selectEl.nextElementSibling;
  if (!wrapper || !wrapper.classList.contains("cselect-wrapper")) return;
  buildCustomSelectOptions(wrapper, selectEl);
}}

function populateYearFilter() {{
  const yearSelect = document.getElementById('yearFilter');
  if (!yearSelect) return;
  const currentVal = yearSelect.value;
  const years = Array.from(new Set(allRecords.map(r => r.year).filter(y => y != null))).sort((a, b) => b - a);
  yearSelect.innerHTML = '<option value="ALL">Semua Tahun</option>';
  years.forEach(y => {{
    const opt = document.createElement('option');
    opt.value = String(y);
    opt.textContent = String(y);
    yearSelect.appendChild(opt);
  }});
  if (years.map(String).includes(currentVal)) {{
    yearSelect.value = currentVal;
  }} else {{
    yearSelect.value = 'ALL';
  }}
  syncCustomSelect(yearSelect);
}}

function populatePeriodFilter() {{
  const periodSelect = document.getElementById('periodFilter');
  if (!periodSelect) return;
  const currentVal = periodSelect.value;
  const order = {{ "TW1": 1, "TW2": 2, "TW3": 3, "Audit": 4 }};
  const periods = Array.from(new Set(allRecords.map(r => r.period).filter(Boolean)))
    .sort((a, b) => (order[a] || 99) - (order[b] || 99));
  periodSelect.innerHTML = '<option value="ALL">Semua Periode</option>';
  periods.forEach(p => {{
    const opt = document.createElement('option');
    opt.value = p;
    opt.textContent = p;
    periodSelect.appendChild(opt);
  }});
  if (periods.includes(currentVal)) {{
    periodSelect.value = currentVal;
  }} else {{
    periodSelect.value = 'ALL';
  }}
  syncCustomSelect(periodSelect);
}}

function applyFilter() {{
  const search = document.getElementById('searchFilter').value.toLowerCase().trim();
  const yearFilter = document.getElementById('yearFilter').value;
  const periodFilter = document.getElementById('periodFilter').value;
  const issueFilter = document.getElementById('issueFilter').value;
  const stmtFilter = document.getElementById('statementFilter').value;

  filteredRecords = allRecords.filter(f => {{
    if (yearFilter !== 'ALL' && String(f.year) !== yearFilter) return false;
    if (periodFilter !== 'ALL' && f.period !== periodFilter) return false;
    if (issueFilter === '{DiagnosticIssueType.INVALID_FOOTING.value}' && f.invalid_footing_count === 0) return false;
    if (issueFilter === '{DiagnosticIssueType.MISSING_CANONICAL.value}' && f.missing_canonical_count === 0) return false;
    if (issueFilter === '{DiagnosticIssueType.MISSING_FILING.value}' && f.missing_filing_count === 0) return false;
    if (stmtFilter !== 'ALL' && (!f.statements || !f.statements.includes(stmtFilter))) return false;
    if (search) {{
      const matchKode = f.emiten_code.toLowerCase().includes(search);
      const matchAccount = f.issues && f.issues.some(i =>
        (i.canonical_account || '').toLowerCase().includes(search) ||
        (i.canonical_code || '').toLowerCase().includes(search)
      );
      if (!matchKode && !matchAccount) return false;
    }}
    return true;
  }});

  currentPage = 1;
  renderTable();
}}

function renderTable() {{
  const tbody = document.getElementById('tableBody');
  const totalFiltered = filteredRecords.length;
  const totalPages = Math.max(1, Math.ceil(totalFiltered / pageSize));

  if (currentPage > totalPages) currentPage = totalPages;
  if (currentPage < 1) currentPage = 1;

  const startIdx = (currentPage - 1) * pageSize;
  const endIdx = Math.min(startIdx + pageSize, totalFiltered);
  const pageSlice = filteredRecords.slice(startIdx, endIdx);

  if (totalFiltered === 0) {{
    tbody.innerHTML = `<tr><td colspan="6" style="text-align:center; padding: 40px; color: var(--muted-foreground);">Tidak ada laporan yang cocok dengan kriteria filter audit.</td></tr>`;
    document.getElementById('paginationInfo').textContent = 'Menampilkan 0 dari 0 laporan';
    document.getElementById('pageCurrentInfo').textContent = 'Halaman 1 / 1';
    document.getElementById('btnFirstPage').disabled = true;
    document.getElementById('btnPrevPage').disabled = true;
    document.getElementById('btnNextPage').disabled = true;
    document.getElementById('btnLastPage').disabled = true;
    return;
  }}

  tbody.innerHTML = pageSlice.map(f => {{
    const issueButtons = [];
    if (f.invalid_footing_count > 0) {{
      issueButtons.push(`<button class="btn-badge btn-badge-danger" onclick="openFilingDetailModal('${{f.emiten_code}}', ${{f.year}}, '${{f.period}}')">${{f.invalid_footing_count}} Footing &rarr;</button>`);
    }}
    if (f.missing_canonical_count > 0) {{
      issueButtons.push(`<button class="btn-badge btn-badge-warning" onclick="openFilingDetailModal('${{f.emiten_code}}', ${{f.year}}, '${{f.period}}')">${{f.missing_canonical_count}} Pos Wajib &rarr;</button>`);
    }}
    if (f.missing_filing_count > 0) {{
      issueButtons.push(`<button class="btn-badge btn-badge-purple" onclick="openFilingDetailModal('${{f.emiten_code}}', ${{f.year}}, '${{f.period}}')">Laporan Tidak Tersedia &rarr;</button>`);
    }}

    return `
      <tr>
        <td style="font-weight: 600; font-size: 13px;">${{f.emiten_code}}</td>
        <td style="font-weight: 500; font-variant-numeric: tabular-nums;">${{f.year}}</td>
        <td><span class="badge badge-neutral">${{f.period}}</span></td>
        <td>
          <div style="font-weight: 500;">${{f.sector || '—'}}</div>
          <div style="color: var(--muted-foreground); font-size: 11px;">${{f.subsector || ''}}</div>
        </td>
        <td class="code-cell" style="color: var(--muted-foreground);">${{f.entry_point || '—'}}</td>
        <td>
          <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;">
            ${{issueButtons.join('')}}
          </div>
        </td>
      </tr>
    `;
  }}).join('');

  document.getElementById('paginationInfo').textContent = `Menampilkan ${{startIdx + 1}}\u2013${{endIdx}} dari ${{totalFiltered.toLocaleString()}} laporan`;
  document.getElementById('pageCurrentInfo').textContent = `Halaman ${{currentPage}} / ${{totalPages}}`;

  document.getElementById('btnFirstPage').disabled = currentPage === 1;
  document.getElementById('btnPrevPage').disabled = currentPage === 1;
  document.getElementById('btnNextPage').disabled = currentPage === totalPages;
  document.getElementById('btnLastPage').disabled = currentPage === totalPages;
}}

function openFilingDetailModal(emiten, year, period) {{
  const filing = allRecords.find(r => r.emiten_code === emiten && r.year === year && r.period === period);
  if (!filing) return;

  document.getElementById('detailModalTitle').textContent = `Audit Detail: ${{filing.emiten_code}} (${{filing.year}} ${{filing.period}})`;
  document.getElementById('detailModalSubtitle').textContent = `Sektor: ${{filing.sector || '—'}} | Subsektor: ${{filing.subsector || '—'}} | Entry Point: ${{filing.entry_point || '—'}} | Total Temuan: ${{filing.total_issues}} pos akun`;

  const toolbar = document.getElementById('detailModalToolbar');

  // Extract unique statements/variants/target files for this filing
  const stmtMap = new Map();
  (filing.issues || []).forEach(i => {{
    const s = i.statement || "balance_statement";
    const ep = i.entry_point || filing.entry_point;
    const v = i.variant || filing.variant;
    const fn = i.target_manual_filename || (s ? `${{filing.emiten_code}}_${{filing.year}}_${{filing.period}}_${{s}}.csv` : "");
    const key = `${{s}}|${{ep}}|${{v}}`;
    if (!stmtMap.has(key)) {{
      stmtMap.set(key, {{ statement: s, entry_point: ep, variant: v, target_manual_filename: fn }});
    }}
  }});

  if (stmtMap.size === 0 && filing.target_files && filing.target_files.length) {{
    filing.target_files.forEach(fn => {{
      let stmt = "balance_statement";
      if (fn.includes("income_statement")) stmt = "income_statement";
      else if (fn.includes("cashflow_statement")) stmt = "cashflow_statement";
      stmtMap.set(fn, {{
        statement: stmt,
        entry_point: filing.entry_point,
        variant: filing.variant,
        target_manual_filename: fn
      }});
    }});
  }}

  let toolbarHtml = `
    <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted-foreground);">
      Berkas Template Override &amp; Pohon Taksonomi Per Statement
    </div>
    <div style="display: flex; flex-direction: column; gap: 8px;">
  `;

  stmtMap.forEach(item => {{
    toolbarHtml += `
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; background: var(--card); border: 1px solid var(--border); border-radius: 6px; padding: 10px 14px; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
          <span class="badge badge-neutral" style="font-weight: 600;">${{item.statement}}</span>
          <span class="code-cell" style="color: var(--muted-foreground); font-size: 11px;">(${{item.variant || 'default'}})</span>
          <span class="code-cell" style="font-size: 12px; font-weight: 500; color: var(--foreground);">${{item.target_manual_filename}}</span>
        </div>
        <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;">
          <button class="btn btn-outline btn-sm" onclick="downloadCsv('${{item.target_manual_filename}}', '${{item.entry_point}}', '${{item.statement}}', '${{item.variant}}')">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Unduh CSV
          </button>
          <button class="btn btn-outline btn-sm" title="Salin seluruh pohon CSV ke clipboard" onclick="copyCsvTree('${{item.entry_point}}', '${{item.statement}}', '${{item.variant}}')">
            Copy CSV Tree
          </button>
          <button class="btn btn-outline btn-sm" title="Salin pohon JSON ke clipboard" onclick="copyJsonTree('${{item.entry_point}}', '${{item.statement}}', '${{item.variant}}')">
            Copy JSON Tree
          </button>
          <button class="btn btn-outline btn-sm" title="Lihat hierarki pohon taksonomi" onclick="openTreeModal('${{item.entry_point}}', '${{item.statement}}', '${{item.variant}}')">
            Lihat Pohon &rarr;
          </button>
        </div>
      </div>
    `;
  }});

  toolbarHtml += `</div>`;
  toolbar.innerHTML = toolbarHtml;

  const tbody = document.getElementById('detailTableBody');
  tbody.innerHTML = (filing.issues || []).map(i => `
    <tr>
      <td><span class="badge badge-neutral">${{i.statement}}</span></td>
      <td class="code-cell">${{i.variant}}</td>
      <td class="code-cell" style="font-weight: 600;">${{i.canonical_code}}</td>
      <td>${{i.canonical_account}}</td>
      <td>${{getIssueBadge(i.issue_type)}}</td>
      <td class="code-cell" style="font-size: 11px; color: var(--muted-foreground);">${{i.validation_status}}</td>
      <td class="num-cell code-cell">${{formatNumber(i.reported_value)}}</td>
      <td class="num-cell code-cell">${{formatNumber(i.value)}}</td>
      <td class="num-cell code-cell" style="color: ${{i.difference ? '#ef4444' : 'inherit'}}; font-weight: ${{i.difference ? '600' : 'normal'}};">${{formatNumber(i.difference)}}</td>
    </tr>
  `).join('');

  document.getElementById('filingDetailModal').classList.add('show');
}}

function closeFilingDetailModal() {{
  document.getElementById('filingDetailModal').classList.remove('show');
}}

window.addEventListener('click', (e) => {{
  const treeModal = document.getElementById('treeModal');
  const detailModal = document.getElementById('filingDetailModal');
  if (e.target === treeModal) closeTreeModal();
  else if (e.target === detailModal) closeFilingDetailModal();
}});

window.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape') {{
    const treeModal = document.getElementById('treeModal');
    if (treeModal && treeModal.classList.contains('show')) {{
      closeTreeModal();
    }} else {{
      closeFilingDetailModal();
    }}
  }}
}});

document.getElementById('searchFilter').addEventListener('input', () => {{
  clearTimeout(searchDebounceTimer);
  searchDebounceTimer = setTimeout(applyFilter, 150);
}});

document.getElementById('yearFilter').addEventListener('change', applyFilter);
document.getElementById('periodFilter').addEventListener('change', applyFilter);
document.getElementById('issueFilter').addEventListener('change', applyFilter);
document.getElementById('statementFilter').addEventListener('change', applyFilter);
document.getElementById('pageSizeSelect').addEventListener('change', (e) => {{
  pageSize = parseInt(e.target.value, 10);
  currentPage = 1;
  renderTable();
}});

document.getElementById('btnFirstPage').addEventListener('click', () => {{ currentPage = 1; renderTable(); }});
document.getElementById('btnPrevPage').addEventListener('click', () => {{ if (currentPage > 1) {{ currentPage--; renderTable(); }} }});
document.getElementById('btnNextPage').addEventListener('click', () => {{ currentPage++; renderTable(); }});
document.getElementById('btnLastPage').addEventListener('click', () => {{
  currentPage = Math.ceil(filteredRecords.length / pageSize);
  renderTable();
}});

function initAllControls() {{
  populateYearFilter();
  populatePeriodFilter();

  initCustomSelect(document.getElementById('yearFilter'), {{ searchable: false }});
  initCustomSelect(document.getElementById('periodFilter'), {{ searchable: false }});
  initCustomSelect(document.getElementById('issueFilter'), {{ searchable: false }});
  initCustomSelect(document.getElementById('statementFilter'), {{ searchable: false }});
  initCustomSelect(document.getElementById('pageSizeSelect'), {{ searchable: false }});

  applyFilter();
}}

// Initialize
if (!allRecords.length) {{
  fetch('records.json')
    .then(res => res.json())
    .then(data => {{
      allRecords = data;
      initAllControls();
    }})
    .catch(() => {{
      initAllControls();
    }});
}} else {{
  initAllControls();
}}

if (!Object.keys(statementTrees).length) {{
  fetch('statement_trees.json')
    .then(res => res.json())
    .then(data => {{ statementTrees = data; }})
    .catch(() => {{}});
}}
</script>
</body>
</html>
"""

    html_path.write_text(html_content, encoding="utf-8")
    return html_path

