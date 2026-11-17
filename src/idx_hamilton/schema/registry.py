from pathlib import Path

from idx_hamilton.schema.canonical import (
    CanonicalAccountMapping,
    CanonicalAccountSpec,
    CanonicalCatalog,
    CanonicalComponentTerm,
    CanonicalLink,
    CanonicalRegistry,
    CanonicalScope,
    PartitionCanonicalSchema,
)
from idx_hamilton.schema.ratios import (
    RatioCatalog,
    RatioCategory,
    RatioPolarity,
    RatioRegistry,
    RatioSpec,
    RatioUnit,
    TemporalBasis,
)
from idx_hamilton.schema.statements import (
    AccountNode,
    Assertion,
    AssertionTerm,
    ChildLink,
    DeprecatedTag,
    Schema,
    StatementSchemaRegistry,
)
from idx_hamilton.stagings.statement import StatementClassification

__all__ = [
    "AccountNode",
    "Assertion",
    "AssertionTerm",
    "CanonicalAccountMapping",
    "CanonicalAccountSpec",
    "CanonicalCatalog",
    "CanonicalComponentTerm",
    "CanonicalLink",
    "CanonicalRegistry",
    "CanonicalScope",
    "ChildLink",
    "DeprecatedTag",
    "PartitionCanonicalSchema",
    "RatioCatalog",
    "RatioCategory",
    "RatioPolarity",
    "RatioRegistry",
    "RatioSpec",
    "RatioUnit",
    "Schema",
    "SchemaRegistry",
    "StatementSchemaRegistry",
    "TemporalBasis",
]


class SchemaRegistry:
    """Unified composite facade coordinating statement, canonical, and ratio registries.

    Provides backwards compatibility for legacy pipeline calls while delegating
    responsibility to decoupled single-responsibility registries.
    """

    def __init__(self, root_path: Path | None = None):
        self.statement_registry = StatementSchemaRegistry(root_path)
        self.canonical_registry_mgr = CanonicalRegistry(self.statement_registry, root_path)
        self.ratio_registry_mgr = RatioRegistry(self.canonical_registry_mgr.catalog, root_path)

    @property
    def registry(self) -> dict[StatementClassification, Schema]:
        return self.statement_registry.registry

    @property
    def canonical_registry(
        self,
    ) -> dict[StatementClassification, PartitionCanonicalSchema]:
        return self.canonical_registry_mgr.partition_registry

    @property
    def canonical_catalog(self) -> CanonicalCatalog:
        return self.canonical_registry_mgr.catalog

    @property
    def ratio_catalog(self) -> RatioCatalog:
        return self.ratio_registry_mgr.catalog

    def get(self, key: StatementClassification) -> Schema | None:
        return self.statement_registry.get(key)

    def get_canonical(
        self, key: StatementClassification
    ) -> PartitionCanonicalSchema | None:
        return self.canonical_registry_mgr.get_partition(key)
