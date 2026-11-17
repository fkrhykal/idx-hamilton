import json
from collections import Counter
from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

import yaml
from pydantic import BaseModel, Field

from idx_hamilton.stagings.statement import StatementClassification


class DeprecatedTag(BaseModel):
    tag: str


class AccountNode(BaseModel):
    account: str
    code: str
    is_total: bool = False
    weight: int = 1
    deprecated_tags: list[DeprecatedTag] = Field(default_factory=list)
    children: list[AccountNode] = Field(default_factory=list)

    def iter_nodes(self) -> Iterator[AccountNode]:
        yield self
        for child in self.children:
            yield from child.iter_nodes()

    def all_mapped_tags(self) -> list[str]:
        tags: list[str] = []
        if self.account:
            tags.append(self.account)
        for dep in self.deprecated_tags:
            tags.append(dep.tag)
        return tags

    def child_links(self) -> list[tuple[str, str, str, int]]:
        if not self.is_total or not self.children:
            return []
        links: list[tuple[str, str, str, int]] = []
        for child in self.children:
            weight = child.weight
            for tag in child.all_mapped_tags():
                links.append((self.code, self.account, tag, weight))
        return links

    @property
    def height(self) -> int:
        sub_parents = [c for c in self.children if c.is_total and c.children]
        if not sub_parents:
            return 1
        return 1 + max(c.height for c in sub_parents)


@dataclass
class ChildLink:
    parent_code: str
    parent: str
    child: str
    weight: int


class AssertionTerm(BaseModel):
    account: str
    weight: int


class Assertion(BaseModel):
    assertion_id: str
    description: str | None = None
    terms: list[AssertionTerm]
    target: float = 0.0
    tolerance: float = 1.0


class Schema(BaseModel):
    entry_point: str
    statement: str
    variant: str
    chart_of_accounts: list[AccountNode]
    assertions: list[Assertion] = Field(default_factory=list)

    def iter_nodes(self) -> Iterator[AccountNode]:
        for root in self.chart_of_accounts:
            yield from root.iter_nodes()

    @property
    def parent_nodes(self) -> list[AccountNode]:
        """Nodes where is_total is True and has child nodes."""
        return [
            node
            for node in self.iter_nodes()
            if node.is_total and node.children and node.account
        ]

    @property
    def parent_names(self) -> list[str]:
        return [node.account for node in self.parent_nodes if node.account]

    @property
    def all_codes(self) -> list[str]:
        return [node.code for node in self.iter_nodes()]

    def child_links(self) -> list[ChildLink]:
        return [
            ChildLink(
                parent_code=link[0],
                parent=link[1],
                child=link[2],
                weight=link[3],
            )
            for parent in self.parent_nodes
            for link in parent.child_links()
        ]

    @property
    def canonical_accounts(self) -> list[str]:
        return [node.account for node in self.iter_nodes() if node.account]

    @property
    def intermediate_accounts(self) -> set[str]:
        return {
            child.account
            for parent in self.parent_nodes
            for child in parent.children
            if child.account
        }

    @property
    def parent_levels(self) -> list[list[AccountNode]]:
        """Returns parent nodes grouped by height in ascending order (bottom-up)."""
        height_map: dict[int, list[AccountNode]] = {}
        for node in self.parent_nodes:
            height_map.setdefault(node.height, []).append(node)
        return [height_map[h] for h in sorted(height_map.keys())]

    @property
    def parent_code_of(self) -> dict[str, str]:
        """Mapping from child parent code to its immediate enclosing parent code."""
        mapping: dict[str, str] = {}
        for parent in self.parent_nodes:
            for child in parent.children:
                if child.is_total and child.children and child.code:
                    mapping[child.code] = parent.code
        return mapping

    @property
    def deprecated_tags(self) -> list[str]:
        return [tag.tag for node in self.iter_nodes() for tag in node.deprecated_tags]

    def mapped_tags_for(self, account_name: str) -> list[str]:
        tags: list[str] = []
        for node in self.iter_nodes():
            if node.account == account_name:
                for tag in node.all_mapped_tags():
                    if tag not in tags:
                        tags.append(tag)
        return tags


class StatementSchemaRegistry:
    """Manages statement-level XBRL taxonomy hierarchy schemas for all entry point variants."""

    def __init__(self, root_path: Path | None = None):
        self.registry: dict[StatementClassification, Schema] = {}
        schema_path = root_path or Path(str(resources.files("idx_hamilton").joinpath("schema")))

        for entry_point in schema_path.iterdir():
            if not entry_point.is_dir() or entry_point.name.startswith((".", "_")):
                continue

            for statement in entry_point.iterdir():
                if not statement.is_dir() or statement.name.startswith((".", "_")):
                    continue

                for variant in statement.iterdir():
                    if not variant.is_dir() or variant.name.startswith((".", "_")):
                        continue

                    schema_yaml = variant.joinpath("schema.yaml")
                    account_json = variant.joinpath("account.schema.json")

                    if not account_json.is_file() or not schema_yaml.is_file():
                        continue

                    account_schema = json.loads(account_json.read_bytes())
                    raw_schema = yaml.safe_load(schema_yaml.read_bytes())
                    label = f"{entry_point.name}/{statement.name}/{variant.name}"

                    schema = Schema.model_validate(raw_schema)

                    if (
                        schema.entry_point != entry_point.name
                        or schema.statement != statement.name
                        or schema.variant != variant.name
                    ):
                        raise ValueError(
                            f"{label}: schema header mismatch ({schema.entry_point}/{schema.statement}/{schema.variant})"
                        )

                    self._validate_schema_consistency(schema, account_schema, label)

                    classification = StatementClassification(
                        entry_point=entry_point.name,
                        statement=statement.name,
                        variant=variant.name,
                    )
                    self.registry[classification] = schema

    def get(self, key: StatementClassification) -> Schema | None:
        return self.registry.get(key)

    def __contains__(self, key: StatementClassification) -> bool:
        return key in self.registry

    def __len__(self) -> int:
        return len(self.registry)

    @staticmethod
    def _validate_schema_consistency(
        schema: Schema, account_schema: object, label: str
    ) -> None:
        if not isinstance(account_schema, Mapping):
            raise TypeError(f"{label}: account schema must be an object")
        allowed_accounts = account_schema.get("enum")
        if not isinstance(allowed_accounts, list) or not all(
            isinstance(account, str) for account in allowed_accounts
        ):
            raise TypeError(
                f"{label}: account.schema.json enum must be a list of strings"
            )

        code_duplicates = sorted(
            code for code, count in Counter(schema.all_codes).items() if count > 1
        )
        deprecated_duplicates = sorted(
            tag for tag, count in Counter(schema.deprecated_tags).items() if count > 1
        )
        collision = sorted(set(schema.canonical_accounts) & set(schema.deprecated_tags))
        all_mapped_tags = set(schema.canonical_accounts) | set(schema.deprecated_tags)
        allowed_set = set(allowed_accounts)
        unknown = sorted(all_mapped_tags - allowed_set)
        unmapped = sorted(allowed_set - all_mapped_tags)

        issues = []
        if code_duplicates:
            issues.append(f"duplicate account codes: {', '.join(code_duplicates)}")
        if deprecated_duplicates:
            issues.append(
                f"duplicate deprecated tags: {', '.join(deprecated_duplicates)}"
            )
        if collision:
            issues.append(
                f"tags appearing as both canonical and deprecated: {', '.join(collision)}"
            )
        if unknown:
            issues.append(
                f"chart of accounts contains unknown accounts/tags: {', '.join(unknown)}"
            )
        if unmapped:
            issues.append(
                f"official taxonomy accounts not yet mapped in schema.yaml: {', '.join(unmapped)}"
            )
        if issues:
            raise ValueError(f"{label}: {'; '.join(issues)}")
