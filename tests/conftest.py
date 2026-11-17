import pytest

from idx_hamilton.schema import (
    CanonicalCatalog,
    CanonicalRegistry,
    RatioCatalog,
    RatioRegistry,
    StatementSchemaRegistry,
)
from idx_hamilton.schema.registry import SchemaRegistry


@pytest.fixture(scope="session")
def schema_registry() -> SchemaRegistry:
    return SchemaRegistry()


@pytest.fixture(scope="session")
def statement_schema_registry() -> StatementSchemaRegistry:
    return StatementSchemaRegistry()


@pytest.fixture(scope="session")
def statement_registry(statement_schema_registry: StatementSchemaRegistry) -> StatementSchemaRegistry:
    return statement_schema_registry


@pytest.fixture(scope="session")
def canonical_registry(
    statement_schema_registry: StatementSchemaRegistry,
) -> CanonicalRegistry:
    return CanonicalRegistry(statement_schema_registry)


@pytest.fixture(scope="session")
def canonical_catalog(canonical_registry: CanonicalRegistry) -> CanonicalCatalog:
    return canonical_registry.catalog


@pytest.fixture(scope="session")
def ratio_registry(canonical_catalog: CanonicalCatalog) -> RatioRegistry:
    return RatioRegistry(canonical_catalog)


@pytest.fixture(scope="session")
def ratio_catalog(ratio_registry: RatioRegistry) -> RatioCatalog:
    return ratio_registry.catalog

