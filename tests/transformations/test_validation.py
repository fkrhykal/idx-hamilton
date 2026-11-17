import patito as pt
import polars as pl

from idx_hamilton.schema.statements import StatementSchemaRegistry
from idx_hamilton.stagings.statement import StatementClassification
from idx_hamilton.transformations.enriched import EnrichedAccount
from idx_hamilton.transformations.validation import (
    ReconciledAccount,
    reconciled_accounts,
)


def test_reconciled_account_patito_model():
    df = pl.DataFrame(
        {
            "emiten_code": ["MKAP", "NASA"],
            "year": [2024, 2024],
            "period": ["TW2", "TW1"],
            "account": [
                "CashGeneratedFromUsedInOperations",
                "PaymentsForAcquisitionOfPropertyPlantAndEquipment",
            ],
            "statement": ["cashflow_statement", "cashflow_statement"],
            "variant": ["direct_method", "direct_method"],
            "value": [100.0, 0.0],
            "reported_value": [0.0, -10368000.0],
            "is_usable": [True, False],
            "validation_status": ["RECOMPUTED_SUBTOTAL", "ELIMINATED_DISCLOSURE"],
            "is_recomputed": [True, False],
            "is_eliminated": [False, True],
            "sector": ["Energy", "Consumer"],
            "subsector": ["Oil & Gas", "Retail"],
        }
    )
    validated = ReconciledAccount.validate(df)
    assert isinstance(validated, pt.DataFrame)
    assert (
        validated.filter(pl.col("emiten_code") == "MKAP").select("is_usable").item()
        is True
    )
    assert (
        validated.filter(pl.col("emiten_code") == "MKAP")
        .select("validation_status")
        .item()
        == "RECOMPUTED_SUBTOTAL"
    )
    assert (
        validated.filter(pl.col("emiten_code") == "NASA").select("is_usable").item()
        is False
    )
    assert (
        validated.filter(pl.col("emiten_code") == "NASA")
        .select("validation_status")
        .item()
        == "ELIMINATED_DISCLOSURE"
    )


def test_reconciled_accounts_reconciliation_rules(
    statement_schema_registry: StatementSchemaRegistry,
):
    clf = StatementClassification(
        entry_point="general",
        statement="cashflow_statement",
        variant="direct_method",
    )

    # Test report A (Cara 1): CF.OPS.GEN is 0, children sum to 100, CF.OPS = 100
    # Test report B (Cara 2): CF.INV is 0, child is -50, CF.NET = CF.OPS (50) + CF.INV (0) = 50
    # Test report C (Cara 3): CF.OPS.GEN reported 999.0 (typo), children sum to 100.0, and CF.OPS = 100.0
    records = [
        # Report A: Imputation of CashGeneratedFromUsedInOperations
        {
            "emiten_code": "TEST1",
            "year": 2024,
            "period": "Audit",
            "account": "ReceiptsFromCustomers",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 150.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST1",
            "year": 2024,
            "period": "Audit",
            "account": "PaymentsToSuppliersForGoodsAndServices",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 50.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST1",
            "year": 2024,
            "period": "Audit",
            "account": "CashGeneratedFromUsedInOperations",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 0.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST1",
            "year": 2024,
            "period": "Audit",
            "account": "NetCashFlowsReceivedFromUsedInOperatingActivities",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 100.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        # Report B: Child adjustment (Cara 2) where CF.INV is 0 and confirmed by CF.NET
        {
            "emiten_code": "TEST2",
            "year": 2024,
            "period": "Audit",
            "account": "NetCashFlowsReceivedFromUsedInOperatingActivities",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 50.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST2",
            "year": 2024,
            "period": "Audit",
            "account": "NetCashFlowsReceivedFromUsedInInvestingActivities",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 0.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST2",
            "year": 2024,
            "period": "Audit",
            "account": "PaymentsForAcquisitionOfPropertyPlantAndEquipment",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": -20.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST2",
            "year": 2024,
            "period": "Audit",
            "account": "NetCashFlowsReceivedFromUsedInFinancingActivities",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 0.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST2",
            "year": 2024,
            "period": "Audit",
            "account": "NetIncreaseDecreaseInCashAndCashEquivalents",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 50.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        # Report C (Non-zero Parent Mismatch confirmed by GP):
        {
            "emiten_code": "TEST3",
            "year": 2024,
            "period": "Audit",
            "account": "ReceiptsFromCustomers",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 150.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST3",
            "year": 2024,
            "period": "Audit",
            "account": "PaymentsToSuppliersForGoodsAndServices",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 50.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST3",
            "year": 2024,
            "period": "Audit",
            "account": "CashGeneratedFromUsedInOperations",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 999.0,
            "sector": "Tech",
            "subsector": "Software",
        },
        {
            "emiten_code": "TEST3",
            "year": 2024,
            "period": "Audit",
            "account": "NetCashFlowsReceivedFromUsedInOperatingActivities",
            "statement": "cashflow_statement",
            "variant": "direct_method",
            "value": 100.0,
            "sector": "Tech",
            "subsector": "Software",
        },
    ]

    enriched_partition = {clf: EnrichedAccount.validate(pl.DataFrame(records))}
    result_partition = reconciled_accounts(enriched_partition, statement_schema_registry)
    res_df = result_partition[clf]

    # Check TEST1 (Subtotal Re-computation)
    gen_row = res_df.filter(
        (pl.col("emiten_code") == "TEST1")
        & (pl.col("account") == "CashGeneratedFromUsedInOperations")
    )
    assert gen_row.select("value").item() == 100.0
    assert gen_row.select("reported_value").item() == 0.0
    assert gen_row.select("is_recomputed").item() is True
    assert gen_row.select("is_eliminated").item() is False
    assert gen_row.select("is_usable").item() is True
    assert gen_row.select("validation_status").item() == "RECOMPUTED_SUBTOTAL"

    # Check leaf component in TEST1
    receipt_row = res_df.filter(
        (pl.col("emiten_code") == "TEST1")
        & (pl.col("account") == "ReceiptsFromCustomers")
    )
    assert receipt_row.select("is_usable").item() is True
    assert receipt_row.select("validation_status").item() == "VERIFIED_COMPONENT"

    # Check TEST2 (Component Elimination where subtotal is 0 and confirmed by major aggregate)
    inv_parent = res_df.filter(
        (pl.col("emiten_code") == "TEST2")
        & (pl.col("account") == "NetCashFlowsReceivedFromUsedInInvestingActivities")
    )
    assert inv_parent.select("value").item() == 0.0
    assert inv_parent.select("is_recomputed").item() is False
    assert inv_parent.select("is_usable").item() is True
    assert (
        inv_parent.select("validation_status").item() == "CONFIRMED_BY_MAJOR_AGGREGATE"
    )

    inv_child = res_df.filter(
        (pl.col("emiten_code") == "TEST2")
        & (pl.col("account") == "PaymentsForAcquisitionOfPropertyPlantAndEquipment")
    )
    assert inv_child.select("value").item() == 0.0
    assert inv_child.select("reported_value").item() == -20.0
    assert inv_child.select("is_recomputed").item() is False
    assert inv_child.select("is_eliminated").item() is True
    assert inv_child.select("is_usable").item() is False
    assert inv_child.select("validation_status").item() == "ELIMINATED_DISCLOSURE"

    # Check TEST3 (Subtotal Re-computation on non-zero parent confirmed by major aggregate)
    test3_parent = res_df.filter(
        (pl.col("emiten_code") == "TEST3")
        & (pl.col("account") == "CashGeneratedFromUsedInOperations")
    )
    assert test3_parent.select("value").item() == 100.0
    assert test3_parent.select("reported_value").item() == 999.0
    assert test3_parent.select("is_recomputed").item() is True
    assert test3_parent.select("is_usable").item() is True
    assert test3_parent.select("validation_status").item() == "RECOMPUTED_SUBTOTAL"

    test3_child = res_df.filter(
        (pl.col("emiten_code") == "TEST3")
        & (pl.col("account") == "ReceiptsFromCustomers")
    )
    assert test3_child.select("is_usable").item() is True
    assert test3_child.select("validation_status").item() == "VERIFIED_COMPONENT"

