"""Hamilton DAG nodes providing fine-grained financial schemas and catalogs."""

from idx_hamilton.schema.canonical import CanonicalCatalog, CanonicalRegistry
from idx_hamilton.schema.ratios import RatioCatalog, RatioRegistry
from idx_hamilton.schema.statements import StatementSchemaRegistry


def statement_schema_registry() -> StatementSchemaRegistry:
    """Loads and validates all 40 IDX taxonomy statement calculation schemas."""
    return StatementSchemaRegistry()


def canonical_registry(
    statement_schema_registry: StatementSchemaRegistry,
) -> CanonicalRegistry:
    """Coordinates canonical mapping across statement partitions."""
    return CanonicalRegistry(statement_schema_registry)


def canonical_catalog(canonical_registry: CanonicalRegistry) -> CanonicalCatalog:
    """Catalog of all 52 unified canonical accounts."""
    return canonical_registry.catalog


def ratio_registry(canonical_catalog: CanonicalCatalog) -> RatioRegistry:
    """Coordinates financial ratio specifications and validations."""
    return RatioRegistry(canonical_catalog)


def ratio_catalog(ratio_registry: RatioRegistry) -> RatioCatalog:
    """Catalog of all 52 standardized financial ratios."""
    return ratio_registry.catalog

