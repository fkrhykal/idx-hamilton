from collections import Counter
from enum import StrEnum
from importlib import resources
from pathlib import Path

import yaml
from pydantic import BaseModel, Field

from idx_hamilton.schema.canonical import (
    CanonicalCatalog,
    CanonicalComponentTerm,
    CanonicalScope,
)


class RatioCategory(StrEnum):
    PROFITABILITY = "profitability"
    LIQUIDITY = "liquidity"
    SOLVENCY = "solvency"
    ACTIVITY = "activity"
    CASHFLOW = "cashflow"
    EFFICIENCY = "efficiency"
    ASSET_QUALITY = "asset_quality"
    FUNDING_STRUCTURE = "funding_structure"
    UNDERWRITING = "underwriting"
    INVESTMENT = "investment"
    TAX = "tax"


class TemporalBasis(StrEnum):
    STOCK_TO_STOCK = "stock_to_stock"
    FLOW_TO_FLOW = "flow_to_flow"
    FLOW_TO_STOCK = "flow_to_stock"
    FLOW = "flow"


class RatioPolarity(StrEnum):
    HIGHER_IS_BETTER = "higher_is_better"
    LOWER_IS_BETTER = "lower_is_better"
    NEUTRAL = "neutral"


class RatioUnit(StrEnum):
    PERCENT = "percent"
    MULTIPLIER = "multiplier"
    CURRENCY = "currency"


class RatioSpec(BaseModel):
    ratio: str
    code: str
    label: str = ""
    category: RatioCategory
    scope: CanonicalScope
    temporal_basis: TemporalBasis
    unit: RatioUnit = RatioUnit.PERCENT
    polarity: RatioPolarity = RatioPolarity.HIGHER_IS_BETTER
    description: str = ""
    how_to_read: str = ""
    applicable_entry_points: list[str]
    numerator: list[CanonicalComponentTerm]
    denominator: list[CanonicalComponentTerm] = Field(default_factory=list)

    @property
    def display_name(self) -> str:
        return self.label or self.ratio.replace("_", " ").title()

    @property
    def required_accounts(self) -> list[str]:
        accounts: list[str] = []
        for term in [*self.numerator, *self.denominator]:
            if term.account not in accounts:
                accounts.append(term.account)
        return accounts


class RatioCatalog(BaseModel):
    ratios: list[RatioSpec]

    @property
    def spec_by_ratio(self) -> dict[str, RatioSpec]:
        return {spec.ratio: spec for spec in self.ratios}

    @property
    def spec_by_code(self) -> dict[str, RatioSpec]:
        return {spec.code: spec for spec in self.ratios}

    def get_spec(self, ratio_or_code: str) -> RatioSpec | None:
        for r in self.ratios:
            if r.ratio == ratio_or_code or r.code == ratio_or_code:
                return r
        return None


class RatioRegistry:
    """Manages declarative financial ratio formulas and specifications."""

    def __init__(
        self,
        canonical_catalog: CanonicalCatalog | None = None,
        root_path: Path | None = None,
    ):
        schema_path = root_path or Path(
            str(resources.files("idx_hamilton").joinpath("schema"))
        )
        ratio_catalog_file = schema_path.joinpath("ratios.yaml")
        if not ratio_catalog_file.is_file():
            raise FileNotFoundError(f"Ratio catalog missing: {ratio_catalog_file}")

        raw_ratios = yaml.safe_load(ratio_catalog_file.read_bytes())
        self.catalog = RatioCatalog.model_validate(raw_ratios)
        self._validate_ratio_catalog(self.catalog, canonical_catalog)

    def get(self, ratio_or_code: str) -> RatioSpec | None:
        return self.catalog.get_spec(ratio_or_code)

    def __len__(self) -> int:
        return len(self.catalog.ratios)

    @staticmethod
    def _validate_ratio_catalog(
        ratio_catalog: RatioCatalog,
        canonical_catalog: CanonicalCatalog | None,
    ) -> None:
        names = [spec.ratio for spec in ratio_catalog.ratios]
        codes = [spec.code for spec in ratio_catalog.ratios]
        dup_names = sorted(n for n, c in Counter(names).items() if c > 1)
        dup_codes = sorted(code for code, c in Counter(codes).items() if c > 1)
        issues: list[str] = []
        if dup_names:
            issues.append(f"duplicate ratio names: {', '.join(dup_names)}")
        if dup_codes:
            issues.append(f"duplicate ratio codes: {', '.join(dup_codes)}")

        if canonical_catalog is not None:
            known_accounts = set(canonical_catalog.spec_by_account.keys())
            unknown_reqs: list[str] = []
            for spec in ratio_catalog.ratios:
                for req in spec.required_accounts:
                    if req not in known_accounts:
                        unknown_reqs.append(f"{spec.ratio}->{req}")
            if unknown_reqs:
                issues.append(
                    f"unknown required canonical accounts: {', '.join(unknown_reqs)}"
                )

        if issues:
            raise ValueError(f"ratios.yaml: {'; '.join(issues)}")
