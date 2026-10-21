import logging
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any, override

from hamilton import driver
from hamilton.driver import Variable
from hamilton.io.materialization import to
from hamilton.lifecycle import NodeExecutionHook

from idx_hamilton.stagings.statement import STATEMENTS

from . import sources
from .marts import coverage
from .resources import IdxHttpClient
from .stagings import dei, statement
from .transformations import account, backfilling

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


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    http_client = IdxHttpClient()

    dr = (
        driver.Builder()
        .with_modules(sources)
        .with_modules(dei)
        .with_modules(statement)
        .with_modules(backfilling)
        .with_modules(account)
        .with_modules(coverage)
        .with_adapters(HamiltonProgress())
        .build()
    )

    output_dir = Path("docs/accounts")
    output_dir.mkdir(parents=True, exist_ok=True)

    materializers = [
        to.csv(
            id=f"{stmt.statement_type}_metadata_csv",
            dependencies=[f"{stmt.statement_type}_metadata"],
            separator=";",
            file=str(output_dir.joinpath(f"{stmt.statement_type}_metadata.csv")),
        )
        for stmt in STATEMENTS
    ]

    final_vars: FinalVars = [
        "report_coverage_png",
        "backfill_coverage_png",
        "coverage_summary_png",
    ]

    try:
        dr.visualize_materialization(
            *materializers,
            additional_vars=final_vars,
            inputs={"idx_http_client": http_client},
            output_file_path="docs/dag_execution.png",
            render_kwargs={"format": "png"},
        )
    except Exception as e:  # noqa: BLE001
        log.warning(
            "Graphviz executable not found in system PATH. Skipping DAG visualization: %s",
            e,
        )

    dr.materialize(
        *materializers,
        additional_vars=final_vars,
        inputs={"idx_http_client": http_client},
    )
