from enum import StrEnum
from typing import Any

import patito as pt
import polars as pl

from idx_hamilton.schema.statements import StatementSchemaRegistry
from idx_hamilton.stagings.statement import StatementPartition
from idx_hamilton.transformations.enriched import EnrichedAccount

REPORT_KEY_COLUMNS: list[str] = ["emiten_code", "year", "period"]


class ValidationStatus(StrEnum):
    FOOTING_VERIFIED = "FOOTING_VERIFIED"
    CONFIRMED_BY_MAJOR_AGGREGATE = "CONFIRMED_BY_MAJOR_AGGREGATE"
    RECOMPUTED_SUBTOTAL = "RECOMPUTED_SUBTOTAL"
    VERIFIED_COMPONENT = "VERIFIED_COMPONENT"
    UNRECONCILED_COMPONENT = "UNRECONCILED_COMPONENT"
    ELIMINATED_DISCLOSURE = "ELIMINATED_DISCLOSURE"
    STANDALONE_DISCLOSURE = "STANDALONE_DISCLOSURE"
    UNRECONCILED_DIFFERENCE = "UNRECONCILED_DIFFERENCE"


USABLE_VALIDATION_STATUSES: set[str] = {
    ValidationStatus.FOOTING_VERIFIED,
    ValidationStatus.CONFIRMED_BY_MAJOR_AGGREGATE,
    ValidationStatus.RECOMPUTED_SUBTOTAL,
    ValidationStatus.VERIFIED_COMPONENT,
    ValidationStatus.STANDALONE_DISCLOSURE,
}


class ReconciledAccount(EnrichedAccount):
    reported_value: float
    value: float
    is_usable: bool
    validation_status: ValidationStatus
    is_recomputed: bool = False
    is_eliminated: bool = False


def _evaluate_all_hierarchy_levels(
    account_dataframe: pl.DataFrame,
    parent_levels: list[list[Any]],
    report_keys: list[str],
    tolerance_pct: float,
    propagate_recomputed: bool,
) -> list[pl.DataFrame]:
    """Evaluates hierarchical footing level by level.

    When propagate_recomputed is True, children sums are propagated upward for failed
    subtotals so their parent aggregates can test whether the recomputed sum reconciles.
    When propagate_recomputed is False, reported values are kept strictly.
    """
    working_values = account_dataframe.select(
        *report_keys,
        pl.col("account"),
        pl.col("value").alias("effective_value"),
    )
    level_evaluations: list[pl.DataFrame] = []

    for level_parents in parent_levels:
        level_links: list[dict[str, Any]] = [
            {
                "parent_code": link[0],
                "parent": link[1],
                "child": link[2],
                "weight": link[3],
            }
            for parent in level_parents
            for link in parent.child_links()
        ]
        if not level_links:
            continue

        links_dataframe = pl.DataFrame(level_links)
        children_aggregations = (
            working_values.join(links_dataframe, left_on="account", right_on="child")
            .group_by(*report_keys, "parent_code", "parent")
            .agg(
                children_sum=(pl.col("effective_value") * pl.col("weight")).sum(),
                children_zero=(pl.col("effective_value") == 0).all(),
            )
        )

        parent_names = [parent.account for parent in level_parents]
        parent_reported = account_dataframe.filter(
            pl.col("account").is_in(parent_names)
        ).select(
            *report_keys,
            pl.col("account").alias("parent"),
            pl.col("value").alias("reported"),
        )

        level_checks = (
            parent_reported.join(
                children_aggregations, on=[*report_keys, "parent"], how="right"
            )
            .with_columns(
                pl.col("reported").fill_null(0.0),
                pl.col("children_sum").fill_null(0.0),
            )
            .with_columns(
                variance=pl.col("reported") - pl.col("children_sum"),
            )
            .with_columns(
                percentage_difference=pl.when(pl.col("children_sum") != 0)
                .then((pl.col("variance").abs() / pl.col("children_sum").abs()) * 100)
                .when(pl.col("reported") == 0)
                .then(0.0)
                .otherwise(float("inf")),
            )
            .with_columns(
                is_balanced=pl.col("percentage_difference") <= tolerance_pct,
            )
        )
        level_evaluations.append(level_checks)

        if propagate_recomputed:
            parent_updates = level_checks.select(
                *report_keys,
                pl.col("parent").alias("account"),
                pl.when(pl.col("is_balanced"))
                .then(pl.col("reported"))
                .otherwise(pl.col("children_sum"))
                .alias("effective_value"),
            )
        else:
            parent_updates = level_checks.select(
                *report_keys,
                pl.col("parent").alias("account"),
                pl.col("reported").alias("effective_value"),
            )

        working_values = working_values.join(
            parent_updates.select(*report_keys, "account"),
            on=[*report_keys, "account"],
            how="anti",
        ).vstack(parent_updates)

    return level_evaluations


def _identify_recomputed_subtotals(
    recomputed_evaluations: pl.DataFrame,
    as_reported_evaluations: pl.DataFrame,
    parent_code_of: dict[str, str],
    report_keys: list[str],
) -> pl.DataFrame:
    """Finds subtotals whose reported footing fails but whose children sum balances the parent aggregate."""
    recomputed_parent_balance = recomputed_evaluations.select(
        *report_keys,
        pl.col("parent_code").alias("direct_parent_code"),
        pl.col("is_balanced").alias("parent_recomputed_balanced"),
    )
    as_reported_parent_balance = as_reported_evaluations.select(
        *report_keys,
        pl.col("parent_code").alias("direct_parent_code"),
        pl.col("is_balanced").alias("parent_as_reported_balanced"),
    )

    return (
        recomputed_evaluations.filter(
            pl.col("parent_code").is_in(list(parent_code_of.keys()))
            & pl.col("is_balanced").eq(False)
            & (pl.col("children_zero").eq(False))
        )
        .with_columns(
            direct_parent_code=pl.col("parent_code").replace_strict(parent_code_of)
        )
        .join(
            as_reported_parent_balance,
            on=[*report_keys, "direct_parent_code"],
            how="left",
        )
        .join(
            recomputed_parent_balance,
            on=[*report_keys, "direct_parent_code"],
            how="left",
        )
        .filter(
            pl.col("parent_as_reported_balanced").fill_null(False).eq(False)
            & pl.col("parent_recomputed_balanced").eq(True)
        )
        .select(
            *report_keys,
            pl.col("parent").alias("account"),
            pl.col("children_sum").alias("recomputed_value"),
        )
    )


def _identify_eliminated_disclosures(
    as_reported_evaluations: pl.DataFrame,
    recomputed_candidates: pl.DataFrame,
    parent_code_of: dict[str, str],
    all_child_links: pl.DataFrame,
    report_keys: list[str],
) -> tuple[pl.DataFrame, pl.DataFrame]:
    """Identifies spurious disclosures under a confirmed-zero subtotal and lists children to zero out."""
    as_reported_parent_balance = as_reported_evaluations.select(
        *report_keys,
        pl.col("parent_code").alias("direct_parent_code"),
        pl.col("is_balanced").alias("parent_as_reported_balanced"),
    )

    eliminated_subtotals = (
        as_reported_evaluations.filter(
            pl.col("parent_code").is_in(list(parent_code_of.keys()))
            & (pl.col("reported") == 0)
            & (pl.col("children_zero").eq(False))
        )
        .with_columns(
            direct_parent_code=pl.col("parent_code").replace_strict(parent_code_of)
        )
        .join(
            as_reported_parent_balance,
            on=[*report_keys, "direct_parent_code"],
            how="left",
        )
        .filter(pl.col("parent_as_reported_balanced").eq(True))
        .select(*report_keys, "parent_code", pl.col("parent").alias("account"))
        .join(
            recomputed_candidates.select(*report_keys, "account"),
            on=[*report_keys, "account"],
            how="anti",
        )
    )

    eliminated_children = (
        eliminated_subtotals.join(all_child_links, on="parent_code")
        .select(*report_keys, pl.col("child").alias("account"))
        .with_columns(is_to_eliminate=pl.lit(True))
        .unique()
    )

    return eliminated_subtotals, eliminated_children


def _classify_validation_status(
    reconciled_values_dataframe: pl.DataFrame,
    eliminated_subtotals: pl.DataFrame,
    all_child_links: pl.DataFrame,
    parent_names: list[str],
    parent_code_of: dict[str, str],
    report_keys: list[str],
    tolerance_pct: float,
) -> pl.DataFrame:
    """Classifies each line item into its standardized validation status and usable flag."""
    aggregated_children_sums = (
        reconciled_values_dataframe.join(
            all_child_links, left_on="account", right_on="child"
        )
        .group_by(*report_keys, "parent_code", "parent")
        .agg(
            children_sum=(pl.col("value") * pl.col("weight")).sum(),
            children_zero=(pl.col("value") == 0).all(),
        )
    )

    reported_parent_values = reconciled_values_dataframe.filter(
        pl.col("account").is_in(parent_names)
    ).select(
        *report_keys,
        pl.col("account").alias("parent"),
        pl.col("value").alias("reported"),
        pl.col("is_recomputed"),
    )

    final_footing_evaluations = (
        reported_parent_values.join(
            aggregated_children_sums, on=[*report_keys, "parent"], how="right"
        )
        .with_columns(
            pl.col("reported").fill_null(0.0),
            pl.col("children_sum").fill_null(0.0),
        )
        .with_columns(
            variance=pl.col("reported") - pl.col("children_sum"),
        )
        .with_columns(
            percentage_difference=pl.when(pl.col("children_sum") != 0)
            .then((pl.col("variance").abs() / pl.col("children_sum").abs()) * 100)
            .when(pl.col("reported") == 0)
            .then(0.0)
            .otherwise(float("inf")),
        )
        .with_columns(
            is_footing_balanced=pl.col("percentage_difference") <= tolerance_pct,
        )
    )

    final_footing_with_parent = (
        final_footing_evaluations.with_columns(
            direct_parent_code=pl.col("parent_code").replace_strict(
                parent_code_of, default=None
            )
        )
        .join(
            final_footing_evaluations.select(
                *report_keys,
                pl.col("parent_code").alias("direct_parent_code"),
                pl.col("is_footing_balanced").alias("ancestor_is_balanced"),
            ),
            on=[*report_keys, "direct_parent_code"],
            how="left",
        )
        .with_columns(
            ancestor_is_balanced=pl.col("ancestor_is_balanced").fill_null(False),
        )
    )

    eliminated_subtotal_keys = eliminated_subtotals.select(
        *report_keys, pl.col("account"), is_eliminated_subtotal=pl.lit(True)
    )

    parent_status_dataframe = (
        final_footing_with_parent.join(
            eliminated_subtotal_keys,
            left_on=[*report_keys, "parent"],
            right_on=[*report_keys, "account"],
            how="left",
        )
        .select(
            *report_keys,
            pl.col("parent").alias("account"),
            parent_validation_status=pl.when(pl.col("is_recomputed"))
            .then(pl.lit(ValidationStatus.RECOMPUTED_SUBTOTAL))
            .when(pl.col("is_eliminated_subtotal").is_not_null())
            .then(pl.lit(ValidationStatus.CONFIRMED_BY_MAJOR_AGGREGATE))
            .when(pl.col("is_footing_balanced"))
            .then(pl.lit(ValidationStatus.FOOTING_VERIFIED))
            .when(pl.col("ancestor_is_balanced"))
            .then(pl.lit(ValidationStatus.CONFIRMED_BY_MAJOR_AGGREGATE))
            .otherwise(pl.lit(ValidationStatus.UNRECONCILED_DIFFERENCE)),
        )
        .unique(subset=[*report_keys, "account"])
    )

    child_parent_status = (
        all_child_links.select("parent", pl.col("child").alias("account"))
        .join(
            final_footing_evaluations.select(
                *report_keys, "parent", "is_footing_balanced"
            ),
            on="parent",
        )
        .group_by(*report_keys, "account")
        .agg(child_parent_is_balanced=pl.col("is_footing_balanced").all())
    )

    return (
        reconciled_values_dataframe.join(
            parent_status_dataframe, on=[*report_keys, "account"], how="left"
        )
        .join(child_parent_status, on=[*report_keys, "account"], how="left")
        .with_columns(
            validation_status=pl.when(pl.col("parent_validation_status").is_not_null())
            .then(pl.col("parent_validation_status"))
            .when(pl.col("is_eliminated"))
            .then(pl.lit(ValidationStatus.ELIMINATED_DISCLOSURE))
            .when(pl.col("child_parent_is_balanced").is_not_null())
            .then(
                pl.when(pl.col("child_parent_is_balanced"))
                .then(pl.lit(ValidationStatus.VERIFIED_COMPONENT))
                .otherwise(pl.lit(ValidationStatus.UNRECONCILED_COMPONENT))
            )
            .otherwise(pl.lit(ValidationStatus.STANDALONE_DISCLOSURE)),
        )
        .with_columns(
            is_usable=pl.col("validation_status").is_in(
                list(USABLE_VALIDATION_STATUSES)
            )
        )
        .drop("parent_validation_status", "child_parent_is_balanced")
    )


def reconciled_accounts(
    enriched_accounts: StatementPartition[pt.DataFrame[EnrichedAccount]],
    statement_schema_registry: StatementSchemaRegistry,
    tolerance_pct: float = 0.05,
) -> StatementPartition[pt.DataFrame[ReconciledAccount]]:
    """Reconciles reporting hierarchies and verifies mathematical footing across accounts."""
    report_keys = REPORT_KEY_COLUMNS
    partitions: StatementPartition[pt.DataFrame[ReconciledAccount]] = {}

    for classification, account_dataframe in enriched_accounts.items():
        base_account_dataframe = account_dataframe.with_columns(
            reported_value=pl.col("value"),
            is_recomputed=pl.lit(False),
            is_eliminated=pl.lit(False),
        )

        schema = statement_schema_registry.get(classification)
        if schema is None or not schema.parent_nodes or not schema.parent_levels:
            unreconciled_dataframe = base_account_dataframe.with_columns(
                validation_status=pl.lit(ValidationStatus.STANDALONE_DISCLOSURE),
                is_usable=pl.lit(True),
            )
            partitions[classification] = ReconciledAccount.validate(
                unreconciled_dataframe
            )
            continue

        parent_code_of = schema.parent_code_of
        parent_levels = schema.parent_levels
        if not parent_code_of:
            unreconciled_dataframe = base_account_dataframe.with_columns(
                validation_status=pl.lit(ValidationStatus.STANDALONE_DISCLOSURE),
                is_usable=pl.lit(True),
            )
            partitions[classification] = ReconciledAccount.validate(
                unreconciled_dataframe
            )
            continue

        # 1. Evaluate hierarchy footing under recomputation track and as-reported track
        recomputed_level_evaluations = _evaluate_all_hierarchy_levels(
            account_dataframe=account_dataframe,
            parent_levels=parent_levels,
            report_keys=report_keys,
            tolerance_pct=tolerance_pct,
            propagate_recomputed=True,
        )
        as_reported_level_evaluations = _evaluate_all_hierarchy_levels(
            account_dataframe=account_dataframe,
            parent_levels=parent_levels,
            report_keys=report_keys,
            tolerance_pct=tolerance_pct,
            propagate_recomputed=False,
        )

        if not recomputed_level_evaluations or not as_reported_level_evaluations:
            unreconciled_dataframe = base_account_dataframe.with_columns(
                validation_status=pl.lit(ValidationStatus.STANDALONE_DISCLOSURE),
                is_usable=pl.lit(True),
            )
            partitions[classification] = ReconciledAccount.validate(
                unreconciled_dataframe
            )
            continue

        recomputed_evaluations_dataframe = pl.concat(recomputed_level_evaluations)
        as_reported_evaluations_dataframe = pl.concat(as_reported_level_evaluations)

        # 2. Identify recomputed subtotal candidates
        recomputed_candidates = _identify_recomputed_subtotals(
            recomputed_evaluations=recomputed_evaluations_dataframe,
            as_reported_evaluations=as_reported_evaluations_dataframe,
            parent_code_of=parent_code_of,
            report_keys=report_keys,
        )

        # 3. Identify eliminated spurious disclosures
        all_child_links = pl.DataFrame(
            [
                {
                    "parent_code": link.parent_code,
                    "parent": link.parent,
                    "child": link.child,
                    "weight": link.weight,
                }
                for link in schema.child_links()
            ]
        )
        eliminated_subtotals, eliminated_children = _identify_eliminated_disclosures(
            as_reported_evaluations=as_reported_evaluations_dataframe,
            recomputed_candidates=recomputed_candidates,
            parent_code_of=parent_code_of,
            all_child_links=all_child_links,
            report_keys=report_keys,
        )

        # 4. Construct reconciled values table
        reconciled_values_dataframe = (
            base_account_dataframe.join(
                recomputed_candidates, on=[*report_keys, "account"], how="left"
            )
            .join(eliminated_children, on=[*report_keys, "account"], how="left")
            .with_columns(
                value=pl.when(pl.col("recomputed_value").is_not_null())
                .then(pl.col("recomputed_value"))
                .when(pl.col("is_to_eliminate").is_not_null() & (pl.col("value") != 0))
                .then(0.0)
                .otherwise(pl.col("value")),
                is_recomputed=pl.when(pl.col("recomputed_value").is_not_null())
                .then(True)
                .otherwise(False),
                is_eliminated=pl.when(
                    pl.col("is_to_eliminate").is_not_null() & (pl.col("value") != 0)
                )
                .then(True)
                .otherwise(False),
            )
            .drop("recomputed_value", "is_to_eliminate")
        )

        # 5. Classify line item validation status and usability
        final_reconciled_dataframe = _classify_validation_status(
            reconciled_values_dataframe=reconciled_values_dataframe,
            eliminated_subtotals=eliminated_subtotals,
            all_child_links=all_child_links,
            parent_names=schema.parent_names,
            parent_code_of=parent_code_of,
            report_keys=report_keys,
            tolerance_pct=tolerance_pct,
        )

        partitions[classification] = ReconciledAccount.validate(
            final_reconciled_dataframe
        )

    return partitions
