"""Vectorized calculation engine for declarative accounting equations."""

from __future__ import annotations

from collections.abc import Sequence

import polars as pl

from .domain import AccountingEquationSpecification


class AccountingEquationEngine:
    """Vectorized calculation engine for verifying accounting equation specifications."""

    @staticmethod
    def evaluate_financial_statements(
        financial_statements_pivoted: pl.DataFrame,
        equation_specifications: Sequence[AccountingEquationSpecification],
    ) -> pl.DataFrame:
        """Evaluates applicable equation specifications across pivoted entity reporting periods.

        Args:
            financial_statements_pivoted: Polars DataFrame containing pivoted accounts across entities and periods.
            equation_specifications: Sequence of declarative accounting equation specifications.

        Returns:
            DataFrame enriched with target balance, recalculated components, variance, and audit conformance columns.
        """
        available_columns = set(financial_statements_pivoted.columns)
        evaluation_expressions: list[pl.Expr] = []

        for equation in equation_specifications:
            if not equation.is_applicable(available_columns):
                continue

            evaluation_expressions.extend(
                [
                    equation.build_target_balance_expression(available_columns),
                    equation.build_recalculated_components_expression(
                        available_columns
                    ),
                    equation.build_reconciliation_variance_expression(
                        available_columns
                    ),
                    equation.build_audit_conformance_expression(available_columns),
                ]
            )

        if not evaluation_expressions:
            return financial_statements_pivoted

        return financial_statements_pivoted.with_columns(evaluation_expressions)
