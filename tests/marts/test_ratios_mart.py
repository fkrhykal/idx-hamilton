import tempfile

import polars as pl

from idx_hamilton.marts.ratios import financial_ratios_heatmaps_html
from idx_hamilton.schema.canonical import CanonicalCatalog
from idx_hamilton.schema.ratios import RatioCatalog
from idx_hamilton.transformations.canonical import CanonicalAccount
from idx_hamilton.transformations.ratios import (
    RatioEvaluationWindow,
    financial_ratios,
)


def test_financial_ratios_heatmaps_html_generation(
    canonical_catalog: CanonicalCatalog,
    ratio_catalog: RatioCatalog,
):
    rows = [
        {
            "emiten_code": "BBCA",
            "year": 2024,
            "period": "TW1",
            "entry_point": "financial_and_sharia",
            "statement": "income_statement",
            "variant": "by_nature_after_tax",
            "canonical_scope": "universal",
            "canonical_code": "IS.PL",
            "canonical_account": "NetIncome",
            "reported_value": 15.0,
            "value": 15.0,
            "is_usable": True,
            "validation_status": "FOOTING_VERIFIED",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 1,
            "usable_component_count": 1,
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
            "canonical_code": "BS.E",
            "canonical_account": "TotalEquity",
            "reported_value": 275.0,
            "value": 275.0,
            "is_usable": True,
            "validation_status": "FOOTING_VERIFIED",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 1,
            "usable_component_count": 1,
            "sector": "Financials",
            "subsector": "Banks",
        },
    ]

    can_df = CanonicalAccount.validate(pl.DataFrame(rows))
    ratios_df = financial_ratios(
        can_df,
        canonical_catalog,
        ratio_catalog,
        evaluation_window=RatioEvaluationWindow(
            start_year=2024,
            start_period="TW1",
            trailing_months=12,
        ),
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        html_path = financial_ratios_heatmaps_html(
            ratios_df, ratio_catalog, output_path=f"{tmpdir}/heatmaps.html"
        )
        assert html_path.exists()
        content = html_path.read_text(encoding="utf-8")
        assert "RATIOS_DATA" in content
        assert "PERIODS_INFO" in content
        assert "subsectorSelect" in content
        assert "sectorSelect" in content
        assert "emitenSelect" in content
        assert "searchInput" not in content
        assert "emitenDatalist" not in content
        assert "(All)" not in content
        assert "Semua Sektor" in content
        assert "Semua Emiten" in content
        js_path = html_path.parent / "ratios_data.js"
        json_path = html_path.parent / "ratios_data.json"
        assert js_path.exists()
        assert json_path.exists()
        js_content = js_path.read_text(encoding="utf-8")
        assert "Return on Equity (ROE)" in js_content
        assert "UNREC (Footing)" in content
        assert "ISA 520" not in content
        assert "2024 TW1" in content
        assert "badge-nm" in content
        assert "corridorContainer" in content
        assert "corridorSvg" in content
        assert "renderQuantileCorridor" in content
        assert "rankingContainer" in content
        assert "rankingSvg" in content
        assert "renderPeerRanking" in content
        assert "rankingPeriodSelect" in content
