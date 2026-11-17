import io
import logging
import sys
import time
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, get_origin, override

import graphviz
import polars as pl
from hamilton import driver
from hamilton.driver import Variable
from hamilton.io.data_adapters import DataSaver
from hamilton.io.materialization import to
from hamilton.lifecycle import NodeExecutionHook
from hamilton.registry import register_adapter

from idx_hamilton.stagings.statement import TuplePartitionKey
from idx_hamilton.transformations.ratios import RatioEvaluationWindow

from . import sources
from .marts import data_quality as data_quality_mart
from .marts import ratios as ratios_mart
from .resources import IdxHttpClient
from .schema import nodes as schema_nodes
from .stagings import dei, statement
from .transformations import canonical, enriched, ratios, validation

type FinalVars = list[str | Callable | Variable]

log = logging.getLogger(__name__)


class HamiltonProgress(NodeExecutionHook):
    def __init__(self):
        self._starts: dict[str, float] = {}

    @override
    def run_before_node_execution(
        self,
        *,
        node_name: str,
        node_tags: dict[str, Any],
        node_kwargs: dict[str, Any],
        node_return_type: type,
        task_id: str | None,
        run_id: str,
        node_input_types: dict[str, Any],
        **future_kwargs: Any,
    ):
        self._starts[node_name] = time.perf_counter()
        print(f"⏳ [{node_name}] running...", flush=True)

    @override
    def run_after_node_execution(
        self,
        *,
        node_name: str,
        node_tags: dict[str, Any],
        node_kwargs: dict[str, Any],
        node_return_type: type,
        result: Any,
        error: Exception | None,
        success: bool,
        task_id: str | None,
        run_id: str,
        **future_kwargs: Any,
    ):
        elapsed = time.perf_counter() - self._starts.pop(node_name, time.perf_counter())
        status = "✅" if success else "❌"
        print(f"{status} [{node_name}] done in {elapsed:.2f}s", flush=True)


@dataclass
class PartitionedParquetSaver(DataSaver):
    path: str

    @classmethod
    def name(cls) -> str:
        return "partitioned_parquet"

    @classmethod
    def applicable_types(cls):
        return [Any]

    @classmethod
    def applies_to(cls, type_: type) -> bool:
        origin = get_origin(type_) or type_
        return isinstance(origin, type) and issubclass(origin, dict)

    def save_data(self, data: dict[TuplePartitionKey, pl.DataFrame]) -> dict[str, Any]:
        base = Path(self.path)

        for partition_name, df in data.items():
            target_path = base.joinpath(*partition_name.to_tuple())
            target_path.mkdir(parents=True, exist_ok=True)
            df.write_parquet(target_path / "accounts.parquet")

        return {"path": str(base), "partitions": list(data.keys())}


def main() -> None:
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    evaluation_window = RatioEvaluationWindow(
        start_year=2026,
        start_period="TW3",
    )
    http_client = IdxHttpClient()

    register_adapter(PartitionedParquetSaver)

    dr = (
        driver.Builder()
        .with_modules(sources)
        .with_modules(dei)
        .with_modules(statement)
        .with_modules(schema_nodes)
        .with_modules(enriched)
        .with_modules(validation)
        .with_modules(canonical)
        .with_modules(ratios)
        .with_modules(ratios_mart)
        .with_modules(data_quality_mart)
        .with_adapters(HamiltonProgress())
        .build()
    )

    materializers = [
        to.partitioned_parquet(
            id="materialized_enriched_accounts",
            path=".data/transformations/enriched_accounts",
            dependencies=["enriched_accounts"],
        ),
        to.partitioned_parquet(
            id="materialized_reconciled_accounts",
            path=".data/transformations/reconciled_accounts",
            dependencies=["reconciled_accounts"],
        ),
        to.partitioned_parquet(
            id="materialized_canonical_accounts",
            path=".data/transformations/canonical_accounts",
            dependencies=["canonical_accounts"],
        ),
        to.parquet(
            id="materialized_unified_canonical_accounts",
            file=".data/transformations/unified_canonical_accounts.parquet",
            dependencies=["unified_canonical_accounts"],
        ),
        to.parquet(
            id="materialized_financial_ratios",
            file=".data/transformations/financial_ratios.parquet",
            dependencies=["financial_ratios"],
        ),
        to.parquet(
            id="materialized_canonical_diagnostics",
            file=".data/transformations/canonical_diagnostics.parquet",
            dependencies=["canonical_diagnostics"],
        ),
    ]

    final_vars: FinalVars = [
        "financial_ratios_heatmaps_html",
        "data_quality_report_html",
    ]

    inputs = {
        "idx_http_client": http_client,
        "evaluation_window": evaluation_window,
    }

    try:
        dr.visualize_materialization(
            *materializers,
            additional_vars=final_vars,
            inputs=inputs,
            output_file_path="docs/dag_execution.png",
            render_kwargs={"format": "png"},
            deduplicate_inputs=True,
        )
    except graphviz.ExecutableNotFound as e:
        log.warning(
            "Graphviz executable not found in system PATH. Skipping DAG visualization: %s",
            e,
        )

    dr.materialize(
        *materializers,
        additional_vars=final_vars,
        inputs=inputs,
    )
