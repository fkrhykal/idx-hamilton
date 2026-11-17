from idx_hamilton.schema import (
    CanonicalRegistry,
    RatioRegistry,
    StatementSchemaRegistry,
)
from idx_hamilton.stagings.statement import StatementClassification


def test_decoupled_schema_registries(
    statement_registry: StatementSchemaRegistry,
    canonical_registry: CanonicalRegistry,
    ratio_registry: RatioRegistry,
):
    # 1. Statement schema registry in isolation
    assert len(statement_registry) == 40
    clf = StatementClassification(
        entry_point="general",
        statement="balance_statement",
        variant="current_and_non_current",
    )
    assert clf in statement_registry
    assert statement_registry.get(clf) is not None

    # 2. Canonical registry in isolation
    assert len(canonical_registry.catalog.canonical_accounts) == 52
    assert len(canonical_registry) == 40
    assert canonical_registry.get_partition(clf) is not None

    # 3. Ratio registry in isolation
    assert len(ratio_registry.catalog.ratios) == 52
    cr_spec = ratio_registry.get("LQ.CR")
    assert cr_spec is not None
    assert cr_spec.ratio == "current_ratio"
    for r in ratio_registry.catalog.ratios:
        assert len(r.description.strip()) > 0, f"Ratio {r.ratio} missing description"
        assert len(r.how_to_read.strip()) > 0, f"Ratio {r.ratio} missing how_to_read"

