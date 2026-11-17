import polars as pl

from idx_hamilton.schema.canonical import CanonicalRegistry
from idx_hamilton.schema.registry import SchemaRegistry
from idx_hamilton.schema.statements import StatementSchemaRegistry
from idx_hamilton.stagings.statement import StatementClassification
from idx_hamilton.transformations.canonical import (
    canonical_accounts,
    unified_canonical_accounts,
)
from idx_hamilton.transformations.enriched import EnrichedAccount
from idx_hamilton.transformations.validation import reconciled_accounts


def test_canonical_catalog_and_links(schema_registry: SchemaRegistry):
    assert schema_registry.canonical_catalog is not None
    assert len(schema_registry.canonical_catalog.canonical_accounts) == 52
    assert schema_registry.ratio_catalog is not None
    assert len(schema_registry.ratio_catalog.ratios) == 52
    assert len(schema_registry.canonical_registry) == 40

    for clf, schema in schema_registry.registry.items():
        part_can = schema_registry.get_canonical(clf)
        assert part_can is not None
        links = part_can.canonical_links(schema, schema_registry.canonical_catalog)
        assert len(links) >= len(part_can.mappings)


def test_canonical_transformation_and_unification(
    canonical_registry: CanonicalRegistry,
    statement_schema_registry: StatementSchemaRegistry,
):
    clf = StatementClassification(
        entry_point="general",
        statement="income_statement",
        variant="by_function_after_tax",
    )
    records = [
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "SalesAndRevenue",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 1000.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "CostOfSalesAndRevenue",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 600.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "GrossProfit",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 400.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "SellingExpenses",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 50.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "GeneralAndAdministrativeExpenses",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 100.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "FinanceCosts",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 30.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "ProfitLossBeforeIncomeTax",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 220.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "ProfitLossFromContinuingOperations",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 220.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "ProfitLoss",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 220.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "ProfitLossAttributableToParentEntity",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 220.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "ComprehensiveIncome",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 220.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
        {
            "emiten_code": "ASII",
            "year": 2024,
            "period": "Audit",
            "account": "ComprehensiveIncomeAttributableToParentEntity",
            "statement": "income_statement",
            "variant": "by_function_after_tax",
            "value": 220.0,
            "sector": "Industrials",
            "subsector": "Multi-sector",
        },
    ]
    rec_part = reconciled_accounts(
        {clf: EnrichedAccount.validate(pl.DataFrame(records))},
        statement_schema_registry,
    )
    can_part = canonical_accounts(
        rec_part, canonical_registry, statement_schema_registry
    )
    can_df = can_part[clf]

    ebit_row = can_df.filter(pl.col("canonical_account") == "OperatingProfit")
    assert ebit_row.select("value").item() == 250.0
    assert ebit_row.select("is_usable").item() is True
    assert ebit_row.select("validation_status").item() == "VERIFIED_COMPONENT"
    assert ebit_row.select("canonical_scope").item() == "real_sector"

    gp_row = can_df.filter(pl.col("canonical_account") == "GrossProfit")
    assert gp_row.select("value").item() == 400.0
    assert gp_row.select("is_usable").item() is True
    assert gp_row.select("validation_status").item() == "FOOTING_VERIFIED"
    assert gp_row.select("canonical_scope").item() == "real_sector"

    unified_df = unified_canonical_accounts(can_part)
    assert unified_df.height == can_df.height

    fin_cost = (
        can_df.filter(pl.col("canonical_account") == "FinanceCosts")
        .select("value")
        .item()
    )
    assert fin_cost == 30.0  # Resolved via deprecated_tags on InterestAndFinanceCosts

