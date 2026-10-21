"""Domain models, specifications, and value objects for accounting equations.

Provides strongly-typed AccountingEquationSpecification and EquationComponentTerm definitions
down to the smallest atomic grain, supporting vertical aggregation verification,
macro accounting balance identities, and cross-statement articulation audits.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from enum import StrEnum

import polars as pl

from idx_hamilton.transformations.hierarchy import (
    AccountRole,
    AccountSpec,
    SignRule,
)


class AccountingEquationOperator(StrEnum):
    """Algebraic relationship operator between target and component accounts."""

    EQUALS = "=="
    DELTA = "delta"


class AccountingEquationCategory(StrEnum):
    """Classification of accounting equation verification scope."""

    VERTICAL_AGGREGATION = "vertical_aggregation"
    HORIZONTAL_BALANCE_IDENTITY = "horizontal_balance_identity"
    CROSS_STATEMENT_ARTICULATION = "cross_statement_articulation"


@dataclass(frozen=True, slots=True)
class EquationComponentTerm:
    """A single atomic account term participating in component recalculation.

    Represents a constituent line item in a vertical breakdown or a counterpart account
    in cross-statement articulation, with its associated sign and namespace metadata.
    """

    account_specification: AccountSpec
    weight: float = 1.0
    statement_namespace: str | None = None
    reporting_context: str | None = None

    def resolve_multiplier(self) -> float:
        """Determines the net algebraic multiplier respecting underlying AccountSpec sign rule."""
        if self.account_specification.sign_rule in (SignRule.SUB, SignRule.SUB_RAW):
            return -abs(self.weight)
        return abs(self.weight)

    @property
    def target_physical_column_name(self) -> str:
        """Resolves target physical column identifier respecting statement/context namespaces."""
        if self.statement_namespace and self.reporting_context:
            return f"{self.statement_namespace}__{self.reporting_context}__{self.account_specification.account}"
        elif self.statement_namespace:
            return f"{self.statement_namespace}__{self.account_specification.account}"
        return self.account_specification.account


@dataclass(frozen=True, slots=True)
class AccountingEquationSpecification:
    """Declarative specification for an accounting integrity verification equation.

    Attributes:
        equation_name: Human-readable descriptive name of the equation.
        statement_type: Canonical category of financial statement (e.g. balance_statement).
        target_account: Benchmark account specification serving as the control target.
        component_terms: Constituent accounts whose sum or relationship is reconciled.
        operator: Relationship operator (default: EQUALS).
        numerical_tolerance: Permitted absolute deviation tolerance for rounding difference.
        equation_category: Structural classification of the accounting equation.
        target_statement_namespace: Optional statement namespace override for target account.
        target_reporting_context: Optional reporting context override for target account.
    """

    equation_name: str
    statement_type: str
    target_account: AccountSpec
    component_terms: Sequence[EquationComponentTerm]
    operator: AccountingEquationOperator = AccountingEquationOperator.EQUALS
    numerical_tolerance: float = 1.0
    equation_category: AccountingEquationCategory = (
        AccountingEquationCategory.VERTICAL_AGGREGATION
    )
    target_statement_namespace: str | None = None
    target_reporting_context: str | None = None

    def __post_init__(self) -> None:
        if not self.component_terms:
            raise ValueError(
                f"AccountingEquationSpecification '{self.equation_name}' must contain at least one component term."
            )

    @property
    def equation_identifier(self) -> str:
        """Deterministic unique identifier for this equation specification."""
        if (
            self.equation_category
            == AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY
        ):
            tag = "horiz"
        elif (
            self.equation_category
            == AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION
        ):
            tag = "cross"
        else:
            tag = "rollup"
        return f"{tag}_{self.target_account.code}"

    @property
    def target_physical_column_name(self) -> str:
        """Resolves target physical column identifier respecting statement/context namespaces."""
        if self.target_statement_namespace and self.target_reporting_context:
            return f"{self.target_statement_namespace}__{self.target_reporting_context}__{self.target_account.account}"
        elif self.target_statement_namespace:
            return f"{self.target_statement_namespace}__{self.target_account.account}"
        return self.target_account.account

    @property
    def formula_representation(self) -> str:
        """Human-readable accounting formula representation."""
        if (
            self.equation_category
            == AccountingEquationCategory.CROSS_STATEMENT_ARTICULATION
            or len(self.component_terms) <= 4
        ):
            component_parts: list[str] = []
            for index, term in enumerate(self.component_terms):
                sign_multiplier = term.resolve_multiplier()
                code_repr = f"`[{term.account_specification.code}]`"
                if index == 0:
                    component_parts.append(
                        f"-{code_repr}" if sign_multiplier < 0 else code_repr
                    )
                else:
                    operator_symbol = " - " if sign_multiplier < 0 else " + "
                    component_parts.append(f"{operator_symbol}{code_repr}")
            components_string = "".join(component_parts)
            return f"`[{self.target_account.code}]` == {components_string}"
        else:
            first_term_code = self.component_terms[0].account_specification.code
            last_term_code = self.component_terms[-1].account_specification.code
            terms_count = len(self.component_terms)
            return f"`[{self.target_account.code}]` == `[{first_term_code}]` + ... + `[{last_term_code}]` ({terms_count} pos)"

    @property
    def required_account_identifiers(self) -> set[str]:
        """Returns canonical account identifiers required for this equation."""
        return {self.target_account.account} | {
            term.account_specification.account for term in self.component_terms
        }

    @property
    def required_physical_columns(self) -> set[str]:
        """Returns physical column names required for this equation."""
        return {self.target_physical_column_name} | {
            term.target_physical_column_name for term in self.component_terms
        }

    @property
    def required_taxonomic_codes(self) -> set[str]:
        """Returns taxonomic codes required for this equation."""
        return {self.target_account.code} | {
            term.account_specification.code for term in self.component_terms
        }

    def is_applicable(self, available_columns: set[str]) -> bool:
        """Type and schema guard checking if target or at least one component term exists in target schema."""
        return self.target_physical_column_name in available_columns or any(
            term.target_physical_column_name in available_columns
            for term in self.component_terms
        )

    def build_target_balance_expression(
        self, available_columns: set[str] | None = None
    ) -> pl.Expr:
        """Polars expression evaluating reported target balance."""
        target_column = self.target_physical_column_name
        expression_alias = f"target_{self.equation_identifier}"
        if available_columns is not None and target_column not in available_columns:
            return pl.lit(0.0).alias(expression_alias)
        return pl.col(target_column).fill_null(0.0).alias(expression_alias)

    def build_recalculated_components_expression(
        self, available_columns: set[str] | None = None
    ) -> pl.Expr:
        """Polars expression evaluating component summation."""
        expressions: list[pl.Expr] = []
        expression_alias = f"recalculated_{self.equation_identifier}"
        for term in self.component_terms:
            term_column = term.target_physical_column_name
            if available_columns is not None and term_column not in available_columns:
                continue
            expressions.append(
                pl.col(term_column).fill_null(0.0) * term.resolve_multiplier()
            )

        if not expressions:
            return pl.lit(0.0).alias(expression_alias)
        return pl.sum_horizontal(expressions).alias(expression_alias)

    def build_reconciliation_variance_expression(
        self, available_columns: set[str] | None = None
    ) -> pl.Expr:
        """Polars expression evaluating reconciliation absolute variance: |target - recalculated|."""
        target_balance = self.build_target_balance_expression(available_columns)
        recalculated_balance = self.build_recalculated_components_expression(
            available_columns
        )
        return (
            (target_balance - recalculated_balance)
            .abs()
            .alias(f"variance_{self.equation_identifier}")
        )

    def build_audit_conformance_expression(
        self, available_columns: set[str] | None = None
    ) -> pl.Expr:
        """Polars expression checking balance conformance against numerical tolerance."""
        variance = self.build_reconciliation_variance_expression(available_columns)
        return (variance <= self.numerical_tolerance).alias(
            f"is_conformant_{self.equation_identifier}"
        )


def build_vertical_aggregation_equations(
    statement_type: str,
    specifications: Sequence[AccountSpec],
    excluded_taxonomic_codes: Sequence[str] | None = None,
) -> tuple[AccountingEquationSpecification, ...]:
    """Constructs vertical aggregation AccountingEquationSpecifications down to atomic grain.

    Args:
        statement_type: Financial statement identifier (e.g. balance_statement).
        specifications: Taxonomy account specifications forming hierarchical tree.
        excluded_taxonomic_codes: Sequence of account codes to omit from generation.

    Returns:
        Tuple of declarative AccountingEquationSpecification instances.
    """
    parent_accounts_map = {spec.code: spec for spec in specifications if spec.is_total}
    children_accounts_map: dict[str, list[AccountSpec]] = defaultdict(list)

    for account_spec in specifications:
        if account_spec.parent_code and account_spec.role == AccountRole.SUMMATIVE:
            children_accounts_map[account_spec.parent_code].append(account_spec)

    excluded_codes_set = set(excluded_taxonomic_codes or ())
    equations: list[AccountingEquationSpecification] = []

    for account_spec in specifications:
        parent_code = account_spec.code
        if parent_code in excluded_codes_set:
            continue
        if parent_code in children_accounts_map and parent_code in parent_accounts_map:
            parent_account = parent_accounts_map[parent_code]
            children_accounts = children_accounts_map[parent_code]
            equations.append(
                AccountingEquationSpecification(
                    equation_name=f"Rollup: [{parent_account.code}] {parent_account.account}",
                    statement_type=statement_type,
                    target_account=parent_account,
                    component_terms=tuple(
                        EquationComponentTerm(account_specification=child)
                        for child in children_accounts
                    ),
                    operator=AccountingEquationOperator.EQUALS,
                    equation_category=AccountingEquationCategory.VERTICAL_AGGREGATION,
                )
            )
    return tuple(equations)
