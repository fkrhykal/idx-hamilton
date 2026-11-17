import polars as pl

from idx_hamilton.schema.canonical import CanonicalCatalog
from idx_hamilton.schema.ratios import RatioCatalog
from idx_hamilton.transformations.canonical import CanonicalAccount
from idx_hamilton.transformations.ratios import (
    RatioEvaluationWindow,
    financial_ratios,
)


def test_financial_ratios_ttm_and_status(
    canonical_catalog: CanonicalCatalog,
    ratio_catalog: RatioCatalog,
):
    # Construct 3 periods for BBCA:
    # 2023 TW1 (NII=20, NI=10)
    # 2023 Audit (NII=100, NI=50)
    # 2024 TW1 (NII=25, NI=15)
    # TTM at 2024 TW1: NI_TTM = 15 + 50 - 10 = 55
    rows = [
        # 2023 TW1
        {
            "emiten_code": "BBCA",
            "year": 2023,
            "period": "TW1",
            "entry_point": "financial_and_sharia",
            "statement": "income_statement",
            "variant": "by_nature_after_tax",
            "canonical_scope": "universal",
            "canonical_code": "IS.PL",
            "canonical_account": "NetIncome",
            "reported_value": 10.0,
            "value": 10.0,
            "is_usable": True,
            "validation_status": "FOOTING_VERIFIED",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 1,
            "usable_component_count": 1,
            "sector": "Financials",
            "subsector": "Banks",
        },
        # 2023 Audit
        {
            "emiten_code": "BBCA",
            "year": 2023,
            "period": "Audit",
            "entry_point": "financial_and_sharia",
            "statement": "income_statement",
            "variant": "by_nature_after_tax",
            "canonical_scope": "universal",
            "canonical_code": "IS.PL",
            "canonical_account": "NetIncome",
            "reported_value": 50.0,
            "value": 50.0,
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
            "year": 2023,
            "period": "Audit",
            "entry_point": "financial_and_sharia",
            "statement": "balance_statement",
            "variant": "liquidity",
            "canonical_scope": "universal",
            "canonical_code": "BS.E",
            "canonical_account": "TotalEquity",
            "reported_value": 250.0,
            "value": 250.0,
            "is_usable": True,
            "validation_status": "FOOTING_VERIFIED",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 1,
            "usable_component_count": 1,
            "sector": "Financials",
            "subsector": "Banks",
        },
        # 2024 TW1
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
        # Deficient equity company at 2024 TW1 (TotalEquity = -100)
        {
            "emiten_code": "SRIL",
            "year": 2024,
            "period": "TW1",
            "entry_point": "general",
            "statement": "balance_statement",
            "variant": "current_and_non_current",
            "canonical_scope": "universal",
            "canonical_code": "BS.L",
            "canonical_account": "TotalLiabilities",
            "reported_value": 300.0,
            "value": 300.0,
            "is_usable": True,
            "validation_status": "FOOTING_VERIFIED",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 1,
            "usable_component_count": 1,
            "sector": "Consumer",
            "subsector": "Textiles",
        },
        {
            "emiten_code": "SRIL",
            "year": 2024,
            "period": "TW1",
            "entry_point": "general",
            "statement": "balance_statement",
            "variant": "current_and_non_current",
            "canonical_scope": "universal",
            "canonical_code": "BS.E",
            "canonical_account": "TotalEquity",
            "reported_value": -100.0,
            "value": -100.0,
            "is_usable": True,
            "validation_status": "FOOTING_VERIFIED",
            "is_recomputed": False,
            "is_eliminated": False,
            "component_count": 1,
            "usable_component_count": 1,
            "sector": "Consumer",
            "subsector": "Textiles",
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

    # 2023 TW1 must be excluded from evaluation window (it was lookback buffer)
    assert ratios_df.filter(
        (pl.col("year") == 2023) & (pl.col("period") == "TW1")
    ).is_empty()

    roe_2024_tw1 = ratios_df.filter(
        (pl.col("emiten_code") == "BBCA")
        & (pl.col("year") == 2024)
        & (pl.col("period") == "TW1")
        & (pl.col("ratio") == "roe_total")
    )
    # TTM NetIncome = 15 + 50 - 10 = 55; TotalEquity = 275 -> ROE = 55 / 275 = 0.2
    assert roe_2024_tw1.select("value").item() == 0.2
    assert abs(roe_2024_tw1.select("ytd_value").item() - (15.0 / 275.0)) < 1e-9
    assert roe_2024_tw1.select("is_usable").item() is True
    assert roe_2024_tw1.select("status").item() == "VALID"

    # Negative equity on SRIL liabilities_to_equity -> NOT_MEANINGFUL
    sril_ler = ratios_df.filter(
        (pl.col("emiten_code") == "SRIL")
        & (pl.col("ratio") == "liabilities_to_equity")
    )
    assert sril_ler.select("value").item() is None
    assert sril_ler.select("is_usable").item() is False
    assert sril_ler.select("status").item() == "NOT_MEANINGFUL"

