from collections import Counter
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel

from idx_hamilton.schema.statements import Schema, StatementSchemaRegistry
from idx_hamilton.stagings.statement import StatementClassification

type CanonicalScope = Literal[
    "universal",
    "real_sector",
    "financial_sector",
    "financial_banking_and_financing",
    "financial_insurance",
]


class CanonicalComponentTerm(BaseModel):
    account: str
    weight: Literal[1, -1] = 1


class CanonicalAccountSpec(BaseModel):
    canonical_account: str
    code: str
    scope: CanonicalScope
    statement: Literal["balance_statement", "income_statement", "cashflow_statement"]
    description: str
    applicable_entry_points: list[str]
    applicable_variants: list[str]


class CanonicalCatalog(BaseModel):
    canonical_accounts: list[CanonicalAccountSpec]

    def expected_for(
        self, classification: StatementClassification
    ) -> list[CanonicalAccountSpec]:
        return [
            spec
            for spec in self.canonical_accounts
            if spec.statement == classification.statement
            and classification.entry_point in spec.applicable_entry_points
            and classification.variant in spec.applicable_variants
        ]

    @property
    def spec_by_account(self) -> dict[str, CanonicalAccountSpec]:
        return {
            spec.canonical_account: spec for spec in self.canonical_accounts
        }

    @property
    def code_by_account(self) -> dict[str, str]:
        return {
            spec.canonical_account: spec.code for spec in self.canonical_accounts
        }


class CanonicalAccountMapping(BaseModel):
    canonical_account: str
    components: list[CanonicalComponentTerm]


@dataclass(frozen=True)
class CanonicalLink:
    canonical_code: str
    canonical_account: str
    canonical_scope: CanonicalScope
    account: str
    weight: int


class PartitionCanonicalSchema(BaseModel):
    entry_point: str
    statement: str
    variant: str
    mappings: list[CanonicalAccountMapping]

    def canonical_links(
        self, schema: Schema, catalog: CanonicalCatalog
    ) -> list[CanonicalLink]:
        spec_map = catalog.spec_by_account
        links: list[CanonicalLink] = []
        for mapping in self.mappings:
            spec = spec_map[mapping.canonical_account]
            for comp in mapping.components:
                for tag in schema.mapped_tags_for(comp.account):
                    links.append(
                        CanonicalLink(
                            canonical_code=spec.code,
                            canonical_account=mapping.canonical_account,
                            canonical_scope=spec.scope,
                            account=tag,
                            weight=comp.weight,
                        )
                    )
        return links


class CanonicalRegistry:
    """Manages the canonical account catalog and partition mappings across all statement variants."""

    def __init__(
        self,
        statement_registry: StatementSchemaRegistry | None = None,
        root_path: Path | None = None,
    ):
        schema_path = root_path or Path(str(resources.files("idx_hamilton").joinpath("schema")))
        self.partition_registry: dict[StatementClassification, PartitionCanonicalSchema] = {}

        canonical_catalog_file = schema_path.joinpath("canonical.yaml")
        if not canonical_catalog_file.is_file():
            raise FileNotFoundError(f"Canonical catalog missing: {canonical_catalog_file}")

        raw_catalog = yaml.safe_load(canonical_catalog_file.read_bytes())
        self.catalog = CanonicalCatalog.model_validate(raw_catalog)
        self._validate_canonical_catalog(self.catalog)

        # Load partition canonical mappings
        for entry_point in schema_path.iterdir():
            if not entry_point.is_dir() or entry_point.name.startswith((".", "_")):
                continue

            for statement in entry_point.iterdir():
                if not statement.is_dir() or statement.name.startswith((".", "_")):
                    continue

                for variant in statement.iterdir():
                    if not variant.is_dir() or variant.name.startswith((".", "_")):
                        continue

                    canonical_yaml = variant.joinpath("canonical.yaml")
                    if not canonical_yaml.is_file():
                        continue

                    raw_canonical = yaml.safe_load(canonical_yaml.read_bytes())
                    partition_canonical = PartitionCanonicalSchema.model_validate(raw_canonical)
                    label = f"{entry_point.name}/{statement.name}/{variant.name}"

                    if (
                        partition_canonical.entry_point != entry_point.name
                        or partition_canonical.statement != statement.name
                        or partition_canonical.variant != variant.name
                    ):
                        raise ValueError(f"{label}: canonical.yaml header mismatch")

                    classification = StatementClassification(
                        entry_point=entry_point.name,
                        statement=statement.name,
                        variant=variant.name,
                    )

                    if statement_registry is not None:
                        schema = statement_registry.get(classification)
                        if schema is not None:
                            self._validate_partition_canonical(
                                partition_canonical,
                                schema,
                                self.catalog,
                                classification,
                                label,
                            )

                    self.partition_registry[classification] = partition_canonical

    def get_partition(
        self, classification: StatementClassification
    ) -> PartitionCanonicalSchema | None:
        return self.partition_registry.get(classification)

    def __contains__(self, key: StatementClassification) -> bool:
        return key in self.partition_registry

    def __len__(self) -> int:
        return len(self.partition_registry)

    @staticmethod
    def _validate_canonical_catalog(catalog: CanonicalCatalog) -> None:
        names = [spec.canonical_account for spec in catalog.canonical_accounts]
        codes = [spec.code for spec in catalog.canonical_accounts]
        dup_names = sorted(n for n, c in Counter(names).items() if c > 1)
        dup_codes = sorted(code for code, c in Counter(codes).items() if c > 1)
        issues: list[str] = []
        if dup_names:
            issues.append(f"duplicate canonical_account names: {', '.join(dup_names)}")
        if dup_codes:
            issues.append(f"duplicate canonical_account codes: {', '.join(dup_codes)}")
        if issues:
            raise ValueError(f"canonical.yaml: {'; '.join(issues)}")

    @staticmethod
    def _validate_partition_canonical(
        partition_canonical: PartitionCanonicalSchema,
        schema: Schema,
        catalog: CanonicalCatalog,
        classification: StatementClassification,
        label: str,
    ) -> None:
        expected_specs = catalog.expected_for(classification)
        expected_names = {spec.canonical_account for spec in expected_specs}
        mapped_names = [m.canonical_account for m in partition_canonical.mappings]
        dup_mapped = sorted(n for n, c in Counter(mapped_names).items() if c > 1)
        mapped_set = set(mapped_names)

        missing = sorted(expected_names - mapped_set)
        unexpected = sorted(mapped_set - expected_names)

        allowed_taxonomy_accounts = set(schema.canonical_accounts)
        unknown_components: list[str] = []
        dup_components: list[str] = []
        empty_mappings: list[str] = []

        for mapping in partition_canonical.mappings:
            if not mapping.components:
                empty_mappings.append(mapping.canonical_account)
            comp_accounts = [c.account for c in mapping.components]
            for acc, count in Counter(comp_accounts).items():
                if count > 1:
                    dup_components.append(f"{mapping.canonical_account}:{acc}")
            for acc in comp_accounts:
                if acc not in allowed_taxonomy_accounts:
                    unknown_components.append(f"{mapping.canonical_account}->{acc}")

        issues: list[str] = []
        if dup_mapped:
            issues.append(
                f"duplicate canonical_account mappings: {', '.join(dup_mapped)}"
            )
        if missing:
            issues.append(
                f"missing applicable canonical accounts: {', '.join(missing)}"
            )
        if unexpected:
            issues.append(
                f"unexpected canonical accounts for this partition: {', '.join(unexpected)}"
            )
        if empty_mappings:
            issues.append(
                f"canonical accounts with empty components: {', '.join(empty_mappings)}"
            )
        if dup_components:
            issues.append(
                f"duplicate component accounts: {', '.join(dup_components)}"
            )
        if unknown_components:
            issues.append(
                f"unknown taxonomy accounts in components: {', '.join(unknown_components)}"
            )
        if issues:
            raise ValueError(f"{label}/canonical.yaml: {'; '.join(issues)}")

