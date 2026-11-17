from dataclasses import asdict

import patito as pt
import polars as pl

from idx_hamilton.models import Model
from idx_hamilton.schema.canonical import CanonicalRegistry, CanonicalScope
from idx_hamilton.schema.statements import StatementSchemaRegistry
from idx_hamilton.sources import Period
from idx_hamilton.stagings.statement import StatementPartition, Variant
from idx_hamilton.transformations.validation import ReconciledAccount, ValidationStatus


class CanonicalAccount(Model):
    emiten_code: str
    year: int
    period: Period
    entry_point: str
    statement: str
    variant: Variant
    canonical_scope: CanonicalScope
    canonical_code: str
    canonical_account: str
    reported_value: float
    value: float
    is_usable: bool
    validation_status: ValidationStatus
    is_recomputed: bool = False
    is_eliminated: bool = False
    component_count: int
    usable_component_count: int
    sector: str
    subsector: str


def canonical_accounts(
    reconciled_accounts: StatementPartition[pt.DataFrame[ReconciledAccount]],
    canonical_registry: CanonicalRegistry,
    statement_schema_registry: StatementSchemaRegistry,
) -> StatementPartition[pt.DataFrame[CanonicalAccount]]:
    catalog = canonical_registry.catalog
    if catalog is None:
        raise ValueError("CanonicalRegistry catalog is not initialized")

    report_keys = [
        ReconciledAccount.n.emiten_code,
        ReconciledAccount.n.year,
        ReconciledAccount.n.period,
        ReconciledAccount.n.statement,
        ReconciledAccount.n.variant,
        ReconciledAccount.n.sector,
        ReconciledAccount.n.subsector,
    ]
    partitions: StatementPartition[pt.DataFrame[CanonicalAccount]] = {}

    for classification, rec_df in reconciled_accounts.items():
        schema = statement_schema_registry.get(classification)
        partition_canonical = canonical_registry.get_partition(classification)
        if schema is None or partition_canonical is None:
            continue

        links = partition_canonical.canonical_links(schema, catalog)
        if not links:
            continue

        links_df = pl.DataFrame([asdict(link) for link in links])

        agg_df = (
            rec_df.join(
                links_df,
                on=ReconciledAccount.n.account,
                how="inner",
            )
            .group_by(
                *report_keys,
                "canonical_scope",
                "canonical_code",
                "canonical_account",
            )
            .agg(
                reported_value=(
                    ReconciledAccount.c.reported_value * pl.col("weight")
                ).sum(),
                value=(
                    pl.when(ReconciledAccount.c.is_usable)
                    .then(ReconciledAccount.c.value * pl.col("weight"))
                    .otherwise(0.0)
                ).sum(),
                component_count=pl.len().cast(pl.Int64),
                usable_component_count=ReconciledAccount.c.is_usable.sum().cast(
                    pl.Int64
                ),
                has_unreconciled_diff=(
                    ReconciledAccount.c.validation_status == "UNRECONCILED_DIFFERENCE"
                ).any(),
                has_unreconciled_comp=(
                    ReconciledAccount.c.validation_status == "UNRECONCILED_COMPONENT"
                ).any(),
                all_eliminated=(
                    ReconciledAccount.c.validation_status == "ELIMINATED_DISCLOSURE"
                ).all(),
                any_eliminated=ReconciledAccount.c.is_eliminated.any(),
                any_recomputed=(
                    (ReconciledAccount.c.validation_status == "RECOMPUTED_SUBTOTAL")
                    | ReconciledAccount.c.is_recomputed
                ).any(),
                all_footing_verified=(
                    ReconciledAccount.c.validation_status == "FOOTING_VERIFIED"
                ).all(),
                all_confirmed_major=(
                    ReconciledAccount.c.validation_status
                    == "CONFIRMED_BY_MAJOR_AGGREGATE"
                ).all(),
                any_verified_comp=(
                    ReconciledAccount.c.validation_status.is_in(
                        [
                            "VERIFIED_COMPONENT",
                            "FOOTING_VERIFIED",
                            "CONFIRMED_BY_MAJOR_AGGREGATE",
                        ]
                    )
                ).any(),
            )
            .with_columns(
                validation_status=pl.when(pl.col("has_unreconciled_diff"))
                .then(pl.lit("UNRECONCILED_DIFFERENCE"))
                .when(pl.col("has_unreconciled_comp"))
                .then(pl.lit("UNRECONCILED_COMPONENT"))
                .when(
                    pl.col("all_eliminated")
                    | (
                        pl.col("any_eliminated")
                        & (pl.col("usable_component_count") == 0)
                    )
                )
                .then(pl.lit("ELIMINATED_DISCLOSURE"))
                .when(pl.col("any_recomputed"))
                .then(pl.lit("RECOMPUTED_SUBTOTAL"))
                .when(pl.col("all_footing_verified"))
                .then(pl.lit("FOOTING_VERIFIED"))
                .when(pl.col("all_confirmed_major"))
                .then(pl.lit("CONFIRMED_BY_MAJOR_AGGREGATE"))
                .when(pl.col("any_verified_comp"))
                .then(pl.lit("VERIFIED_COMPONENT"))
                .otherwise(pl.lit("STANDALONE_DISCLOSURE")),
            )
            .with_columns(
                is_usable=pl.col("validation_status").is_in(
                    [
                        "FOOTING_VERIFIED",
                        "CONFIRMED_BY_MAJOR_AGGREGATE",
                        "RECOMPUTED_SUBTOTAL",
                        "VERIFIED_COMPONENT",
                        "STANDALONE_DISCLOSURE",
                    ]
                ),
                is_recomputed=pl.col("any_recomputed"),
                is_eliminated=pl.col("validation_status") == "ELIMINATED_DISCLOSURE",
                entry_point=pl.lit(classification.entry_point),
            )
            .select(
                CanonicalAccount.n.emiten_code,
                CanonicalAccount.n.year,
                CanonicalAccount.n.period,
                CanonicalAccount.n.entry_point,
                CanonicalAccount.n.statement,
                CanonicalAccount.n.variant,
                CanonicalAccount.n.canonical_scope,
                CanonicalAccount.n.canonical_code,
                CanonicalAccount.n.canonical_account,
                CanonicalAccount.n.reported_value,
                CanonicalAccount.n.value,
                CanonicalAccount.n.is_usable,
                CanonicalAccount.n.validation_status,
                CanonicalAccount.n.is_recomputed,
                CanonicalAccount.n.is_eliminated,
                CanonicalAccount.n.component_count,
                CanonicalAccount.n.usable_component_count,
                CanonicalAccount.n.sector,
                CanonicalAccount.n.subsector,
            )
            .sort(
                CanonicalAccount.n.emiten_code,
                CanonicalAccount.n.year,
                CanonicalAccount.n.period,
                CanonicalAccount.n.canonical_code,
            )
        )

        partitions[classification] = CanonicalAccount.validate(agg_df)

    return partitions


def unified_canonical_accounts(
    canonical_accounts: StatementPartition[pt.DataFrame[CanonicalAccount]],
) -> pt.DataFrame[CanonicalAccount]:
    if not canonical_accounts:
        return CanonicalAccount.DataFrame()
    combined = pl.concat(list(canonical_accounts.values()), how="vertical").sort(
        CanonicalAccount.n.emiten_code,
        CanonicalAccount.n.year,
        CanonicalAccount.n.period,
        CanonicalAccount.n.canonical_code,
    )
    return CanonicalAccount.validate(combined)
