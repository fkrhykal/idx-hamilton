from enum import StrEnum
from typing import Literal

import patito as pt
import polars as pl

from idx_hamilton.models import Model
from idx_hamilton.schema.canonical import (
    CanonicalCatalog,
    CanonicalComponentTerm,
    CanonicalScope,
)
from idx_hamilton.schema.ratios import (
    RatioCatalog,
    RatioCategory,
    RatioSpec,
    TemporalBasis,
)
from idx_hamilton.sources import Period
from idx_hamilton.transformations.canonical import CanonicalAccount


class RatioStatus(StrEnum):
    VALID = "VALID"
    NOT_MEANINGFUL = "NOT_MEANINGFUL"
    INCOMPLETE_HISTORY = "INCOMPLETE_HISTORY"
    UNRECONCILED_COMPONENT = "UNRECONCILED_COMPONENT"


PERIOD_ORDER: dict[Period, int] = {
    "TW1": 1,
    "TW2": 2,
    "TW3": 3,
    "Audit": 4,
}

ORDER_TO_PERIOD: dict[int, Period] = {
    1: "TW1",
    2: "TW2",
    3: "TW3",
    4: "Audit",
}

# Column prefix constants for wide aggregation table
PREFIX_ACCOUNT_PRESENT: str = "account_present_"
PREFIX_TTM_VALUE: str = "account_ttm_value_"
PREFIX_AVERAGE_STOCK_VALUE: str = "account_average_stock_value_"
PREFIX_REPORTED_PERIOD_VALUE: str = "account_reported_period_value_"
PREFIX_IS_USABLE: str = "account_is_usable_"
PREFIX_TTM_PRESENT: str = "account_ttm_present_"
PREFIX_TTM_USABLE: str = "account_ttm_usable_"
PREFIX_AVERAGE_STOCK_USABLE: str = "account_average_stock_usable_"


class FinancialRatio(Model):
    emiten_code: str
    year: int
    period: Period
    entry_point: str
    sector: str
    subsector: str
    ratio_scope: CanonicalScope
    ratio_category: RatioCategory
    ratio_code: str
    ratio: str
    temporal_basis: TemporalBasis
    value: float | None
    ytd_value: float | None
    is_usable: bool
    status: RatioStatus


class RatioEvaluationWindow(Model):
    start_year: int = 2026
    start_period: Period = "TW3"
    trailing_months: int = 12


def _build_trailing_twelve_months_flow_terms(
    start_year: int,
    start_period: Period,
    trailing_months: int = 12,
) -> list[tuple[int, Period, float]]:
    """Calculates linear combination terms for reconstructing 12M Trailing Twelve Months (TTM).

    For flow statements (Income Statement, Cash Flow):
      - Annual Audit period: directly represents FY 12-month accumulated flow.
      - Interim periods (e.g. TW1 2026): TTM = YTD(2026 TW1) + FY(2025 Audit) - YTD(2025 TW1).
    """
    trailing_quarters = max(1, trailing_months // 3)
    quarter_end_index = start_year * 4 + (PERIOD_ORDER[start_period] - 1)
    quarter_before_index = quarter_end_index - trailing_quarters
    year_before = quarter_before_index // 4
    period_before_order = (quarter_before_index % 4) + 1

    raw_terms: dict[tuple[int, Period], float] = {
        (start_year, start_period): 1.0,
    }

    if period_before_order == 4:
        for year in range(year_before + 1, start_year):
            audit_key = (year, "Audit")
            raw_terms[audit_key] = raw_terms.get(audit_key, 0.0) + 1.0
    else:
        for year in range(year_before, start_year):
            audit_key = (year, "Audit")
            raw_terms[audit_key] = raw_terms.get(audit_key, 0.0) + 1.0
        subtraction_key = (year_before, ORDER_TO_PERIOD[period_before_order])
        raw_terms[subtraction_key] = raw_terms.get(subtraction_key, 0.0) - 1.0

    return [
        (year, period, weight)
        for (year, period), weight in raw_terms.items()
        if abs(weight) > 1e-9
    ]


def _compile_linear_terms(
    terms: list[CanonicalComponentTerm],
    column_prefix: str,
) -> pl.Expr:
    """Compiles a weighted sum expression of canonical account terms."""
    expressions = [
        pl.col(f"{column_prefix}{term.account}") * float(term.weight) for term in terms
    ]
    return pl.sum_horizontal(expressions)


def _compile_ratio_expression(
    ratio_specification: RatioSpec,
    numerator_prefix: str,
    denominator_prefix: str | None = None,
) -> tuple[pl.Expr, pl.Expr]:
    """Compiles numerator and denominator expressions alongside denominator positivity guard."""
    numerator_expression = _compile_linear_terms(
        ratio_specification.numerator, numerator_prefix
    )
    if not ratio_specification.denominator:
        return numerator_expression, pl.lit(True)

    actual_denominator_prefix = (
        denominator_prefix if denominator_prefix is not None else numerator_prefix
    )
    denominator_expression = _compile_linear_terms(
        ratio_specification.denominator, actual_denominator_prefix
    )
    return numerator_expression / denominator_expression, denominator_expression > 0.0


def _calculate_evaluation_quarters(
    evaluation_window: RatioEvaluationWindow,
) -> list[tuple[int, Period]]:
    """Generates the ordered list of evaluation quarters within the evaluation window."""
    anchor_quarter_index = evaluation_window.start_year * 4 + (
        PERIOD_ORDER[evaluation_window.start_period] - 1
    )
    trailing_quarters = max(1, evaluation_window.trailing_months // 3)
    evaluation_quarters: list[tuple[int, Period]] = []
    for quarter_index in range(
        anchor_quarter_index - trailing_quarters + 1, anchor_quarter_index + 1
    ):
        year = quarter_index // 4
        period = ORDER_TO_PERIOD[(quarter_index % 4) + 1]
        evaluation_quarters.append((year, period))
    return evaluation_quarters


def _compute_trailing_and_average_stock_values(
    filtered_accounts_dataframe: pl.DataFrame,
    evaluation_quarters: list[tuple[int, Period]],
    quarters_flow_terms: dict[tuple[int, Period], list[tuple[int, Period, float]]],
) -> pl.DataFrame:
    """Computes TTM flow reconstructions and 12-month average stock values across evaluation quarters."""
    is_flow_statement = pl.col("statement").is_in(
        ["income_statement", "cashflow_statement"]
    )
    evaluation_partitions: list[pl.DataFrame] = []

    for evaluation_year, evaluation_period in evaluation_quarters:
        terms = quarters_flow_terms[(evaluation_year, evaluation_period)]
        anchor_dataframe = filtered_accounts_dataframe.filter(
            (pl.col("year") == evaluation_year)
            & (pl.col("period") == evaluation_period)
        )
        if anchor_dataframe.is_empty():
            continue

        lookback_terms = [
            (year, period, weight)
            for (year, period, weight) in terms
            if (year, period) != (evaluation_year, evaluation_period)
        ]
        anchor_weight = next(
            (
                weight
                for (year, period, weight) in terms
                if (year, period) == (evaluation_year, evaluation_period)
            ),
            1.0,
        )

        if not lookback_terms:
            period_partition = anchor_dataframe.with_columns(
                ttm_present=pl.lit(True),
                ttm_usable=pl.col("is_usable"),
                ttm_value=pl.when(is_flow_statement)
                .then(pl.col("value") * anchor_weight)
                .otherwise(pl.col("value")),
            )
        else:
            period_partition = anchor_dataframe
            accumulated_value_expression = pl.col("value") * anchor_weight
            all_terms_present_expression = pl.lit(True)
            all_terms_usable_expression = pl.col("is_usable")

            for index, (
                lookback_year,
                lookback_period,
                lookback_weight,
            ) in enumerate(lookback_terms):
                lookback_dataframe = (
                    filtered_accounts_dataframe.filter(
                        (pl.col("year") == lookback_year)
                        & (pl.col("period") == lookback_period)
                    )
                    .select(
                        "emiten_code",
                        "canonical_account",
                        pl.col("value").alias(f"_lookback_value_{index}"),
                        pl.col("is_usable").alias(f"_lookback_usable_{index}"),
                    )
                    .unique(
                        subset=["emiten_code", "canonical_account"],
                        maintain_order=True,
                    )
                )
                period_partition = period_partition.join(
                    lookback_dataframe,
                    on=["emiten_code", "canonical_account"],
                    how="left",
                )
                accumulated_value_expression = (
                    accumulated_value_expression
                    + pl.col(f"_lookback_value_{index}") * lookback_weight
                )
                all_terms_present_expression = (
                    all_terms_present_expression
                    & pl.col(f"_lookback_value_{index}").is_not_null()
                )
                all_terms_usable_expression = all_terms_usable_expression & pl.col(
                    f"_lookback_usable_{index}"
                ).fill_null(False)

            period_partition = period_partition.with_columns(
                ttm_present=pl.when(is_flow_statement)
                .then(all_terms_present_expression)
                .otherwise(pl.lit(True)),
                ttm_usable=pl.when(is_flow_statement)
                .then(all_terms_usable_expression)
                .otherwise(pl.col("is_usable")),
                ttm_value=pl.when(is_flow_statement)
                .then(accumulated_value_expression)
                .otherwise(pl.col("value")),
            )

        # Lookback 12 months prior for stock balance (evaluation_year - 1, evaluation_period)
        prior_year_stock_dataframe = (
            filtered_accounts_dataframe.filter(
                (pl.col("year") == evaluation_year - 1)
                & (pl.col("period") == evaluation_period)
            )
            .select(
                "emiten_code",
                "canonical_account",
                pl.col("value").alias("_prior_year_stock_value"),
                pl.col("is_usable").alias("_prior_year_stock_usable"),
            )
            .unique(
                subset=["emiten_code", "canonical_account"],
                maintain_order=True,
            )
        )

        period_partition = (
            period_partition.join(
                prior_year_stock_dataframe,
                on=["emiten_code", "canonical_account"],
                how="left",
            )
            .with_columns(
                avg_stock_val=pl.when(is_flow_statement)
                .then(pl.col("ttm_value"))
                .when(pl.col("_prior_year_stock_value").is_not_null())
                .then((pl.col("value") + pl.col("_prior_year_stock_value")) / 2.0)
                .otherwise(pl.col("value")),
                avg_stock_usable=pl.when(is_flow_statement)
                .then(pl.col("ttm_usable"))
                .when(pl.col("_prior_year_stock_value").is_not_null())
                .then(
                    pl.col("is_usable")
                    & pl.col("_prior_year_stock_usable").fill_null(False)
                )
                .otherwise(pl.col("is_usable")),
            )
            .select(
                anchor_dataframe.columns
                + [
                    "ttm_present",
                    "ttm_usable",
                    "ttm_value",
                    "avg_stock_val",
                    "avg_stock_usable",
                ]
            )
        )

        evaluation_partitions.append(period_partition)

    if not evaluation_partitions:
        return pl.DataFrame()

    return pl.concat(evaluation_partitions)


def _build_wide_metrics_dataframe(
    trailing_dataframe: pl.DataFrame,
    all_canonical_names: list[str],
) -> pl.DataFrame:
    """Builds a wide metrics table with columns keyed by clean, explicit prefixes."""
    aggregation_expressions: list[pl.Expr] = [
        pl.col("entry_point").first().alias("entry_point"),
        pl.col("sector").first().alias("sector"),
        pl.col("subsector").first().alias("subsector"),
    ]
    for account_name in all_canonical_names:
        account_condition = pl.col("canonical_account") == account_name
        aggregation_expressions.extend(
            [
                account_condition.any().alias(
                    f"{PREFIX_ACCOUNT_PRESENT}{account_name}"
                ),
                pl.col("ttm_value")
                .filter(account_condition)
                .first()
                .alias(f"{PREFIX_TTM_VALUE}{account_name}"),
                pl.col("avg_stock_val")
                .filter(account_condition)
                .first()
                .alias(f"{PREFIX_AVERAGE_STOCK_VALUE}{account_name}"),
                pl.col("value")
                .filter(account_condition)
                .first()
                .alias(f"{PREFIX_REPORTED_PERIOD_VALUE}{account_name}"),
                pl.col("is_usable")
                .filter(account_condition)
                .first()
                .fill_null(False)
                .alias(f"{PREFIX_IS_USABLE}{account_name}"),
                pl.col("ttm_present")
                .filter(account_condition)
                .first()
                .fill_null(False)
                .alias(f"{PREFIX_TTM_PRESENT}{account_name}"),
                pl.col("ttm_usable")
                .filter(account_condition)
                .first()
                .fill_null(False)
                .alias(f"{PREFIX_TTM_USABLE}{account_name}"),
                pl.col("avg_stock_usable")
                .filter(account_condition)
                .first()
                .fill_null(False)
                .alias(f"{PREFIX_AVERAGE_STOCK_USABLE}{account_name}"),
            ]
        )

    return trailing_dataframe.group_by("emiten_code", "year", "period").agg(
        aggregation_expressions
    )


def _evaluate_single_ratio(
    wide_metrics_dataframe: pl.DataFrame,
    ratio_specification: RatioSpec,
    account_statement_map: dict[
        str, Literal["balance_statement", "income_statement", "cashflow_statement"]
    ],
) -> pl.DataFrame | None:
    """Evaluates a single financial ratio formula across applicable emitens."""
    required_accounts = ratio_specification.required_accounts
    accounts_present_condition = pl.all_horizontal(
        [pl.col(f"{PREFIX_ACCOUNT_PRESENT}{acc}") for acc in required_accounts]
    )

    applicable_dataframe = wide_metrics_dataframe.filter(
        pl.col("entry_point").is_in(ratio_specification.applicable_entry_points)
        & accounts_present_condition
    )
    if applicable_dataframe.is_empty():
        return None

    basis = ratio_specification.temporal_basis
    current_usable_expression = pl.all_horizontal(
        [pl.col(f"{PREFIX_IS_USABLE}{acc}") for acc in required_accounts]
    )

    if basis == TemporalBasis.STOCK_TO_STOCK:
        # Point-in-time balance sheet ratio: evaluated strictly as-of report date
        ttm_value_expression, ttm_denominator_is_positive = _compile_ratio_expression(
            ratio_specification,
            numerator_prefix=PREFIX_REPORTED_PERIOD_VALUE,
            denominator_prefix=PREFIX_REPORTED_PERIOD_VALUE,
        )
        ytd_value_expression = ttm_value_expression
        ytd_denominator_is_positive = ttm_denominator_is_positive

        unusable_condition = ~current_usable_expression
        missing_history_condition = pl.lit(False)
        non_positive_denominator_condition = (~unusable_condition) & (
            ~ttm_denominator_is_positive
        )
        valid_condition = (~unusable_condition) & ttm_denominator_is_positive

    elif basis == TemporalBasis.FLOW_TO_STOCK:
        # Flow-to-stock ratio: 12M TTM flow over 12M Average Stock
        ttm_value_expression, ttm_denominator_is_positive = _compile_ratio_expression(
            ratio_specification,
            numerator_prefix=PREFIX_TTM_VALUE,
            denominator_prefix=PREFIX_AVERAGE_STOCK_VALUE,
        )
        ytd_value_expression, ytd_denominator_is_positive = _compile_ratio_expression(
            ratio_specification,
            numerator_prefix=PREFIX_REPORTED_PERIOD_VALUE,
            denominator_prefix=PREFIX_REPORTED_PERIOD_VALUE,
        )

        flow_required_accounts = [
            acc
            for acc in required_accounts
            if account_statement_map.get(acc)
            in ("income_statement", "cashflow_statement")
        ]
        stock_required_accounts = [
            acc
            for acc in required_accounts
            if account_statement_map.get(acc) == "balance_statement"
        ]

        ttm_present_expression = (
            pl.all_horizontal(
                [pl.col(f"{PREFIX_TTM_PRESENT}{acc}") for acc in flow_required_accounts]
            )
            if flow_required_accounts
            else pl.lit(True)
        )
        ttm_usable_expression = (
            pl.all_horizontal(
                [pl.col(f"{PREFIX_TTM_USABLE}{acc}") for acc in flow_required_accounts]
            )
            if flow_required_accounts
            else pl.lit(True)
        )
        average_stock_usable_expression = (
            pl.all_horizontal(
                [
                    pl.col(f"{PREFIX_AVERAGE_STOCK_USABLE}{acc}")
                    for acc in stock_required_accounts
                ]
            )
            if stock_required_accounts
            else pl.lit(True)
        )

        unusable_condition = (
            (~current_usable_expression)
            | (ttm_present_expression & (~ttm_usable_expression))
            | (~average_stock_usable_expression)
        )
        missing_history_condition = (~unusable_condition) & (~ttm_present_expression)
        non_positive_denominator_condition = (
            (~unusable_condition)
            & (~missing_history_condition)
            & (~ttm_denominator_is_positive)
        )
        valid_condition = (
            (~unusable_condition)
            & (~missing_history_condition)
            & ttm_denominator_is_positive
        )

    else:
        # Flow-to-flow ratio: 12M TTM duration flows
        ttm_value_expression, ttm_denominator_is_positive = _compile_ratio_expression(
            ratio_specification,
            numerator_prefix=PREFIX_TTM_VALUE,
            denominator_prefix=PREFIX_TTM_VALUE,
        )
        ytd_value_expression, ytd_denominator_is_positive = _compile_ratio_expression(
            ratio_specification,
            numerator_prefix=PREFIX_REPORTED_PERIOD_VALUE,
            denominator_prefix=PREFIX_REPORTED_PERIOD_VALUE,
        )

        flow_required_accounts = [
            acc
            for acc in required_accounts
            if account_statement_map.get(acc)
            in ("income_statement", "cashflow_statement")
        ]

        ttm_present_expression = (
            pl.all_horizontal(
                [pl.col(f"{PREFIX_TTM_PRESENT}{acc}") for acc in flow_required_accounts]
            )
            if flow_required_accounts
            else pl.lit(True)
        )
        ttm_usable_expression = (
            pl.all_horizontal(
                [pl.col(f"{PREFIX_TTM_USABLE}{acc}") for acc in flow_required_accounts]
            )
            if flow_required_accounts
            else pl.lit(True)
        )

        unusable_condition = (~current_usable_expression) | (
            ttm_present_expression & (~ttm_usable_expression)
        )
        missing_history_condition = (~unusable_condition) & (~ttm_present_expression)
        non_positive_denominator_condition = (
            (~unusable_condition)
            & (~missing_history_condition)
            & (~ttm_denominator_is_positive)
        )
        valid_condition = (
            (~unusable_condition)
            & (~missing_history_condition)
            & ttm_denominator_is_positive
        )

    return applicable_dataframe.select(
        pl.col("emiten_code"),
        pl.col("year"),
        pl.col("period"),
        pl.col("entry_point"),
        pl.col("sector"),
        pl.col("subsector"),
        pl.lit(ratio_specification.scope).alias("ratio_scope"),
        pl.lit(ratio_specification.category).alias("ratio_category"),
        pl.lit(ratio_specification.code).alias("ratio_code"),
        pl.lit(ratio_specification.ratio).alias("ratio"),
        pl.lit(ratio_specification.temporal_basis).alias("temporal_basis"),
        pl.when(valid_condition)
        .then(ttm_value_expression)
        .otherwise(pl.lit(None, dtype=pl.Float64))
        .alias("value"),
        pl.when(current_usable_expression & ytd_denominator_is_positive)
        .then(ytd_value_expression)
        .otherwise(pl.lit(None, dtype=pl.Float64))
        .alias("ytd_value"),
        valid_condition.alias("is_usable"),
        pl.when(unusable_condition)
        .then(pl.lit(RatioStatus.UNRECONCILED_COMPONENT))
        .when(missing_history_condition)
        .then(pl.lit(RatioStatus.INCOMPLETE_HISTORY))
        .when(non_positive_denominator_condition)
        .then(pl.lit(RatioStatus.NOT_MEANINGFUL))
        .otherwise(pl.lit(RatioStatus.VALID))
        .alias("status"),
    )


DEFAULT_EVALUATION_WINDOW: RatioEvaluationWindow = RatioEvaluationWindow()


def financial_ratios(
    unified_canonical_accounts: pt.DataFrame[CanonicalAccount],
    canonical_catalog: CanonicalCatalog,
    ratio_catalog: RatioCatalog,
    evaluation_window: RatioEvaluationWindow = DEFAULT_EVALUATION_WINDOW,
) -> pt.DataFrame[FinancialRatio]:
    """Calculates 52 standardized financial ratios with 12M TTM lookback and usability auditing."""
    if (
        unified_canonical_accounts.is_empty()
        or ratio_catalog is None
        or canonical_catalog is None
    ):
        return FinancialRatio.DataFrame()

    evaluation_quarters = _calculate_evaluation_quarters(evaluation_window)

    # 1. Pre-compute trailing flow terms per evaluation quarter and collect required historical years
    all_required_years: set[int] = set()
    quarters_flow_terms: dict[tuple[int, Period], list[tuple[int, Period, float]]] = {}

    for evaluation_year, evaluation_period in evaluation_quarters:
        terms = _build_trailing_twelve_months_flow_terms(
            start_year=evaluation_year,
            start_period=evaluation_period,
            trailing_months=evaluation_window.trailing_months,
        )
        quarters_flow_terms[(evaluation_year, evaluation_period)] = terms
        for trailing_year, _, _ in terms:
            all_required_years.add(trailing_year)
        all_required_years.add(evaluation_year)
        all_required_years.add(evaluation_year - 1)

    filtered_accounts_dataframe = unified_canonical_accounts.filter(
        pl.col("year").is_in(list(all_required_years))
    )
    if filtered_accounts_dataframe.is_empty():
        return FinancialRatio.DataFrame()

    # 2. Compute 12M TTM flow reconstructions and 12-month average stock values
    trailing_dataframe = _compute_trailing_and_average_stock_values(
        filtered_accounts_dataframe=filtered_accounts_dataframe,
        evaluation_quarters=evaluation_quarters,
        quarters_flow_terms=quarters_flow_terms,
    )
    if trailing_dataframe.is_empty():
        return FinancialRatio.DataFrame()

    # 3. Build wide metrics dataframe with explicit column names
    all_canonical_names = [
        spec.canonical_account for spec in canonical_catalog.canonical_accounts
    ]
    account_statement_map = {
        spec.canonical_account: spec.statement
        for spec in canonical_catalog.canonical_accounts
    }

    wide_metrics_dataframe = _build_wide_metrics_dataframe(
        trailing_dataframe=trailing_dataframe,
        all_canonical_names=all_canonical_names,
    )

    # 4. Evaluate each ratio formula
    evaluated_ratio_frames: list[pl.DataFrame] = []

    for ratio_specification in ratio_catalog.ratios:
        ratio_frame = _evaluate_single_ratio(
            wide_metrics_dataframe=wide_metrics_dataframe,
            ratio_specification=ratio_specification,
            account_statement_map=account_statement_map,
        )
        if ratio_frame is not None:
            evaluated_ratio_frames.append(ratio_frame)

    if not evaluated_ratio_frames:
        return FinancialRatio.DataFrame()

    combined_ratios_dataframe = pl.concat(evaluated_ratio_frames).sort(
        "entry_point",
        "emiten_code",
        "year",
        "period",
        "ratio_scope",
        "ratio_code",
    )
    return FinancialRatio.validate(combined_ratios_dataframe)
