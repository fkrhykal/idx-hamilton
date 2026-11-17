from idx_hamilton.schema import StatementSchemaRegistry
from idx_hamilton.stagings.statement import StatementClassification


def test_statement_schema_lookups(statement_registry: StatementSchemaRegistry):
    balance_schema = statement_registry.get(
        StatementClassification(
            entry_point="general",
            statement="balance_statement",
            variant="current_and_non_current",
        )
    )
    assert balance_schema is not None
    assert len(balance_schema.chart_of_accounts) > 0

    income_schema = statement_registry.get(
        StatementClassification(
            entry_point="general",
            statement="income_statement",
            variant="by_function_after_tax",
        )
    )
    assert income_schema is not None
    assert len(income_schema.chart_of_accounts) > 0

    cashflow_schema = statement_registry.get(
        StatementClassification(
            entry_point="general",
            statement="cashflow_statement",
            variant="direct_method",
        )
    )
    assert cashflow_schema is not None
    assert len(cashflow_schema.chart_of_accounts) > 0
    assert len(cashflow_schema.parent_levels) >= 2
    assert "CashGeneratedFromUsedInOperations" in cashflow_schema.intermediate_accounts
    assert (
        "NetIncreaseDecreaseInCashAndCashEquivalents"
        not in cashflow_schema.intermediate_accounts
    )
    assert cashflow_schema.parent_code_of.get("CF.OPS.GEN") == "CF.OPS"

