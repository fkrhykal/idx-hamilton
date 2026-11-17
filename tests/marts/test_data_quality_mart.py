import tempfile
from pathlib import Path

import polars as pl

from idx_hamilton.marts.data_quality import (
    CanonicalDiagnosticRecord,
    DiagnosticIssueType,
    DiagnosticValidationStatus,
    canonical_diagnostics,
    data_quality_report_html,
)
from idx_hamilton.schema.canonical import CanonicalCatalog, CanonicalRegistry
from idx_hamilton.schema.statements import StatementSchemaRegistry
from idx_hamilton.stagings.dei import DeiMetadata
from idx_hamilton.transformations.canonical import CanonicalAccount


def test_canonical_diagnostics_and_html(
    canonical_registry: CanonicalRegistry,
    canonical_catalog: CanonicalCatalog,
    statement_schema_registry: StatementSchemaRegistry,
):
    canonical_registry.catalog = canonical_catalog

    # 1. Create mock canonical accounts: 1 valid, 1 invalid footing
    accounts_data = [
        {
            "emiten_code": "BBCA",
            "year": 2024,
            "period": "TW1",
            "entry_point": "financial_and_sharia",
            "statement": "balance_statement",
            "variant": "liquidity",
            "canonical_scope": "universal",
            "canonical_code": "BS.A",
            "canonical_account": "TotalAssets",
            "reported_value": 1000.0,
            "value": 1000.0,
            "is_usable": True,
            "validation_status": "FOOTING_VERIFIED",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 5,
            "usable_component_count": 5,
            "sector": "Financials",
            "subsector": "Banks",
        },
        {
            "emiten_code": "BBCA",
            "year": 2024,
            "period": "TW1",
            "entry_point": "financial_and_sharia",
            "statement": "balance_statement",
            "variant": "liquidity",
            "canonical_scope": "universal",
            "canonical_code": "BS.L",
            "canonical_account": "TotalLiabilities",
            "reported_value": 850.0,
            "value": 800.0,
            "is_usable": False,
            "validation_status": "UNRECONCILED_DIFFERENCE",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 4,
            "usable_component_count": 3,
            "sector": "Financials",
            "subsector": "Banks",
        },
    ]
    canonical_df = CanonicalAccount.validate(pl.DataFrame(accounts_data))

    # Mock DEI metadata where BBCA also had TW2, but ASII missed TW2
    dei_data = [
        {
            "emiten_code": "BBCA",
            "year": 2024,
            "period": "TW1",
            "EntityName": "PT Bank Central Asia Tbk",
            "EntityCode": "BBCA",
            "DescriptionOfPresentationCurrency": "Rupiah",
            "TypeOfReportOnFinancialStatements": "Audit",
            "CurrentPeriodStartDate": "2024-01-01",
            "CurrentPeriodEndDate": "2024-03-31",
            "Sector": "Financials",
            "Subsector": "Banks",
            "TypeOfAuditorsOpinion": "Unqualified",
            "CurrentYearAuditor": "PwC",
        },
        {
            "emiten_code": "BBCA",
            "year": 2024,
            "period": "TW2",
            "EntityName": "PT Bank Central Asia Tbk",
            "EntityCode": "BBCA",
            "DescriptionOfPresentationCurrency": "Rupiah",
            "TypeOfReportOnFinancialStatements": "Audit",
            "CurrentPeriodStartDate": "2024-01-01",
            "CurrentPeriodEndDate": "2024-06-30",
            "Sector": "Financials",
            "Subsector": "Banks",
            "TypeOfAuditorsOpinion": "Unqualified",
            "CurrentYearAuditor": "PwC",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "TW1",
            "EntityName": "PT Astra International Tbk",
            "EntityCode": "ASII",
            "DescriptionOfPresentationCurrency": "Rupiah",
            "TypeOfReportOnFinancialStatements": "Audit",
            "CurrentPeriodStartDate": "2024-01-01",
            "CurrentPeriodEndDate": "2024-03-31",
            "Sector": "Industrials",
            "Subsector": "Automobiles",
            "TypeOfAuditorsOpinion": "Unqualified",
            "CurrentYearAuditor": "KPMG",
        },
    ]
    dei_df = DeiMetadata.validate(pl.DataFrame(dei_data))

    diagnostics = canonical_diagnostics(
        unified_canonical_accounts=canonical_df,
        canonical_registry=canonical_registry,
        dei_metadata=dei_df,
    )

    assert not diagnostics.is_empty()
    assert isinstance(diagnostics, pl.DataFrame)

    # 1. Check Invalid Footing record
    invalid_rows = diagnostics.filter(
        CanonicalDiagnosticRecord.c.issue_type == DiagnosticIssueType.INVALID_FOOTING
    )
    assert len(invalid_rows) == 1
    row_dict = invalid_rows.to_dicts()[0]
    assert row_dict["canonical_code"] == "BS.L"
    assert row_dict["difference"] == 50.0  # 850.0 - 800.0
    assert row_dict["validation_status"] == DiagnosticValidationStatus.UNRECONCILED_DIFFERENCE
    assert row_dict["target_manual_filename"] == "BBCA_2024_TW1_balance_statement.csv"

    # 2. Check Missing Canonical record (e.g. BS.E is expected for liquidity balance sheet but wasn't provided)
    missing_rows = diagnostics.filter(
        CanonicalDiagnosticRecord.c.issue_type == DiagnosticIssueType.MISSING_CANONICAL
    )
    assert len(missing_rows) > 0
    missing_codes = missing_rows["canonical_code"].to_list()
    assert "BS.E" in missing_codes

    # 3. Check Missing Filing record (ASII 2024 TW2 is missing while BBCA has it)
    missing_filings = diagnostics.filter(
        CanonicalDiagnosticRecord.c.issue_type == DiagnosticIssueType.MISSING_FILING
    )
    assert len(missing_filings) > 0
    asii_missing = missing_filings.filter(
        CanonicalDiagnosticRecord.c.emiten_code == "ASII"
    ).to_dicts()[0]
    assert asii_missing["year"] == 2024
    assert asii_missing["period"] == "TW2"

    # 4. Generate HTML and verify
    with tempfile.TemporaryDirectory() as tmp_dir:
        out_file = Path(tmp_dir) / "data_quality_report.html"
        result_path = data_quality_report_html(
            diagnostics,
            statement_schema_registry=statement_schema_registry,
            output_path=str(out_file),
        )
        assert result_path.exists()
        assert (result_path.parent / "records.json").exists()
        assert (result_path.parent / "records.js").exists()
        assert (result_path.parent / "statement_trees.json").exists()
        assert (result_path.parent / "statement_trees.js").exists()
        content = result_path.read_text(encoding="utf-8")
        assert "Audit Kualitas Data" in content
        assert "statement_trees.js" in content
        assert "INVALID_FOOTING" in content
        assert "yearFilter" in content
        assert "periodFilter" in content
        assert "filingDetailModal" in content
        assert "openFilingDetailModal" in content

        # Verify that records.json contains unique (emiten_code, year, period) filings
        import json
        records_data = json.loads((result_path.parent / "records.json").read_text(encoding="utf-8"))
        assert len(records_data) > 0
        keys = [(r["emiten_code"], r["year"], r["period"]) for r in records_data]
        assert len(keys) == len(set(keys))
        assert "issues" in records_data[0]

        # Also test directory output
        out_dir = Path(tmp_dir) / "subfolder"
        dir_result = data_quality_report_html(
            diagnostics,
            statement_schema_registry=statement_schema_registry,
            output_dir=str(out_dir),
        )
        assert dir_result.exists()
        assert dir_result.name == "index.html"
        assert (out_dir / "records.json").exists()
        assert (out_dir / "statement_trees.json").exists()
