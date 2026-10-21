import patito as pt
import polars as pl
from hamilton.function_modifiers import extract_fields, group, inject, source

from idx_hamilton.models import Model
from idx_hamilton.stagings.dei import DeiMetadata
from idx_hamilton.stagings.statement import STATEMENTS, EntryPoint
from idx_hamilton.transformations.backfilling import AccountFact

FACT_PARTITIONS = [
    (ep.slug(), stmt.statement_type, f"{ep.slug()}_{stmt.statement_type}_facts")
    for ep in EntryPoint
    for stmt in STATEMENTS
]


class AccountMetadata(Model):
    account: str
    entry_points: str
    variants: str
    sectors: str
    subsectors: str

    class c:
        account: pl.Expr
        entry_points: pl.Expr
        variants: pl.Expr
        sectors: pl.Expr
        subsectors: pl.Expr

    class n:
        account: str
        entry_points: str
        variants: str
        sectors: str
        subsectors: str


from idx_hamilton.transformations.hierarchy import hierarchy_dataframe


@extract_fields(
    {
        f"{stmt.statement_type}_metadata": pt.DataFrame[AccountMetadata]
        for stmt in STATEMENTS
    }
)
@inject(facts=group(*[source(node_name) for _, _, node_name in FACT_PARTITIONS]))
def account_metadata(
    dei_metadata: pt.DataFrame[DeiMetadata],
    facts: list[pt.DataFrame[AccountFact]],
) -> dict[str, pt.DataFrame[AccountMetadata]]:
    tagged_facts = [
        df.with_columns(entry_point=pl.lit(ep_slug))
        for (ep_slug, _, _), df in zip(FACT_PARTITIONS, facts, strict=True)
        if not df.is_empty()
    ]

    emiten_dei = (
        dei_metadata.select(
            DeiMetadata.c.emiten_code,
            DeiMetadata.c.Sector,
            DeiMetadata.c.Subsector,
        )
        .drop_nulls(subset=[DeiMetadata.n.Sector, DeiMetadata.n.Subsector])
        .unique(subset=[DeiMetadata.n.emiten_code], keep="last")
    )

    all_enriched = (
        pl.concat(tagged_facts)
        .filter(AccountFact.c.value != 0)
        .join(
            emiten_dei,
            on=AccountFact.n.emiten_code,
            how="left",
        )
        if tagged_facts
        else pl.DataFrame()
    )

    total_sectors = (
        emiten_dei.get_column(DeiMetadata.n.Sector).drop_nulls().n_unique()
        if not emiten_dei.is_empty()
        else 0
    )
    total_subsectors = (
        emiten_dei.get_column(DeiMetadata.n.Subsector).drop_nulls().n_unique()
        if not emiten_dei.is_empty()
        else 0
    )

    hier_df = hierarchy_dataframe()
    results: dict[str, pt.DataFrame[AccountMetadata]] = {}

    for stmt in STATEMENTS:
        stmt_type = stmt.statement_type
        node_name = f"{stmt_type}_metadata"

        # 1. Base hierarchy accounts & entry_points & variants
        sub_hier = hier_df.filter(pl.col("statement") == stmt_type)
        if sub_hier.is_empty():
            results[node_name] = AccountMetadata.DataFrame()
            continue

        total_eps = sub_hier["entry_point"].n_unique()
        total_vars = sub_hier["variant"].n_unique()

        hier_meta = sub_hier.group_by("account").agg(
            pl.when(pl.col("entry_point").n_unique() == total_eps)
            .then(pl.lit("all_entry_points"))
            .otherwise(pl.col("entry_point").unique().sort().str.join(", "))
            .alias(AccountMetadata.n.entry_points),
            pl.when(pl.col("variant").n_unique() == total_vars)
            .then(pl.lit("all_variants"))
            .otherwise(pl.col("variant").unique().sort().str.join(", "))
            .alias(AccountMetadata.n.variants),
        )

        # 2. Empirical DEI sectors from facts if available
        if not all_enriched.is_empty():
            df_stmt = all_enriched.filter(AccountFact.c.statement == stmt_type)
            fact_meta = df_stmt.group_by(AccountFact.n.account).agg(
                pl.when(DeiMetadata.c.Sector.drop_nulls().n_unique() == total_sectors)
                .then(pl.lit("all_sectors"))
                .otherwise(
                    DeiMetadata.c.Sector.drop_nulls().unique().sort().str.join(", ")
                )
                .alias(AccountMetadata.n.sectors),
                pl.when(
                    DeiMetadata.c.Subsector.drop_nulls().n_unique() == total_subsectors
                )
                .then(pl.lit("all_subsectors"))
                .otherwise(
                    DeiMetadata.c.Subsector.drop_nulls().unique().sort().str.join(", ")
                )
                .alias(AccountMetadata.n.subsectors),
            )
            df_merged = hier_meta.join(
                fact_meta, on="account", how="left"
            ).with_columns(
                pl.col(AccountMetadata.n.sectors).fill_null("all_sectors"),
                pl.col(AccountMetadata.n.subsectors).fill_null("all_subsectors"),
            )
        else:
            df_merged = hier_meta.with_columns(
                pl.lit("all_sectors").alias(AccountMetadata.n.sectors),
                pl.lit("all_subsectors").alias(AccountMetadata.n.subsectors),
            )

        df_sorted = df_merged.sort("account")
        results[node_name] = AccountMetadata.validate(df_sorted)

    return results
