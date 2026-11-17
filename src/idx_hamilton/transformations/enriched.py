import patito as pt
import polars as pl

from idx_hamilton.models import Model
from idx_hamilton.sources import Period
from idx_hamilton.stagings.dei import DeiMetadata
from idx_hamilton.stagings.statement import Account, StatementPartition, Variant


class EnrichedAccount(Model):
    emiten_code: str
    year: int
    period: Period

    account: str

    statement: str
    variant: Variant

    value: float

    sector: str
    subsector: str


def enriched_accounts(
    dei_metadata: pt.DataFrame[DeiMetadata],
    staged_accounts: StatementPartition[pt.DataFrame[Account]],
) -> StatementPartition[pt.DataFrame[EnrichedAccount]]:

    mapping = {
        EnrichedAccount.n.emiten_code: DeiMetadata.c.emiten_code,
        EnrichedAccount.n.sector: DeiMetadata.c.Sector,
        EnrichedAccount.n.subsector: DeiMetadata.c.Subsector,
    }

    mapping_metadata = (
        dei_metadata.select(**mapping)
        .drop_nulls(subset=[EnrichedAccount.n.sector, EnrichedAccount.n.subsector])
        .unique(subset=[EnrichedAccount.n.emiten_code], keep="last")
    )

    return {
        partition: EnrichedAccount.validate(
            account_facts.filter(pl.col("context").str.starts_with("Current"))
            .join(
                mapping_metadata,
                on=[EnrichedAccount.n.emiten_code],
                how="left",
            )
            .select(
                emiten_code=Account.n.emiten_code,
                year=Account.n.year,
                period=Account.n.period,
                account=Account.n.account,
                statement=Account.n.statement,
                variant=Account.n.variant,
                value=Account.n.value,
                sector=EnrichedAccount.n.sector,
                subsector=EnrichedAccount.n.subsector,
            )
        )
        for partition, account_facts in staged_accounts.items()
    }
