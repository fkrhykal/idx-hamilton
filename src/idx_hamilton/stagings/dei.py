import collections
import io
import itertools
import logging
import os
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import cast

import patito as pt
import polars as pl
from ixbrlparse import IXBRL, ixbrlNonNumeric, ixbrlNumeric

from idx_hamilton.models import Model
from idx_hamilton.sources import IxbrlFilling, Period

log = logging.getLogger(__name__)

DEI = "1000000.html"


class MetadataItem(Model):
    emiten_code: str
    year: int
    period: Period
    context: str
    property: str
    value: str

    class c:
        emiten_code: pl.Expr
        year: pl.Expr
        period: pl.Expr
        context: pl.Expr
        property: pl.Expr
        value: pl.Expr


class DeiMetadata(Model):
    emiten_code: str
    year: int
    period: Period

    EntityName: str
    EntityCode: str
    DescriptionOfPresentationCurrency: str
    TypeOfReportOnFinancialStatements: str
    CurrentPeriodStartDate: str
    CurrentPeriodEndDate: str

    Sector: str | None = None
    Subsector: str | None = None
    Industry: str | None = None
    Subindustry: str | None = None
    TypeOfAuditorsOpinion: str | None = None
    CurrentYearAuditor: str | None = None

    class c:
        emiten_code: pl.Expr
        year: pl.Expr
        period: pl.Expr

        EntityName: pl.Expr
        EntityCode: pl.Expr
        DescriptionOfPresentationCurrency: pl.Expr
        TypeOfReportOnFinancialStatements: pl.Expr
        CurrentPeriodStartDate: pl.Expr
        CurrentPeriodEndDate: pl.Expr

        Sector: pl.Expr
        Subsector: pl.Expr
        Industry: pl.Expr
        Subindustry: pl.Expr
        TypeOfAuditorsOpinion: pl.Expr
        CurrentYearAuditor: pl.Expr


def _get_dei_bytes(z: zipfile.ZipFile) -> bytes | None:
    if "1000000.html" in z.NameToInfo:
        return z.read("1000000.html")
    if "inlineXBRL/1000000.html" in z.NameToInfo:
        return z.read("inlineXBRL/1000000.html")
    for name in z.namelist():
        if name.endswith("1000000.html"):
            return z.read(name)
    return None


def _parse_dei_filling(filling: IxbrlFilling) -> list[MetadataItem]:
    records: list[MetadataItem] = []
    try:
        with zipfile.ZipFile(filling.zip_path) as z:
            raw_bytes = _get_dei_bytes(z)
            if not raw_bytes:
                log.warning("[DEI_NOT_FOUND] %s", filling.zip_path)
                return records

        normalized = (
            raw_bytes.replace(b"ix:nonnumeric", b"ix:nonNumeric")
            .replace(b"ix:nonfraction", b"ix:nonFraction")
            .replace(b"contextref=", b"contextRef=")
            .replace(b"unitref=", b"unitRef=")
        )
        ixbrl = IXBRL(io.BytesIO(normalized))

        for item in cast(list[ixbrlNonNumeric], ixbrl.nonnumeric):
            if item.name and item.value is not None:
                records.append(
                    MetadataItem(
                        emiten_code=filling.emiten_code,
                        year=filling.year,
                        period=filling.period,
                        context=str(item.context),
                        property=str(item.name),
                        value=str(item.value).strip(),
                    )
                )
        for num in cast(list[ixbrlNumeric], ixbrl.numeric):
            if num.name and num.value is not None:
                records.append(
                    MetadataItem(
                        emiten_code=filling.emiten_code,
                        year=filling.year,
                        period=filling.period,
                        context=str(num.context),
                        property=str(num.name),
                        value=str(num.value),
                    )
                )

    except (KeyError, zipfile.BadZipFile, Exception) as err:  # noqa: BLE001
        log.warning("[PARSE_DEI_ERROR] %s: %s", filling.zip_path, err)
        return []

    return records


def staged_dei_items(ixbrl_fillings: list[IxbrlFilling]) -> pt.DataFrame[MetadataItem]:
    cache_dir = Path(".data") / "stagings" / "dei"
    cache_dir.mkdir(parents=True, exist_ok=True)

    by_period: dict[tuple[int, Period], list[IxbrlFilling]] = collections.defaultdict(
        list
    )
    for filling in ixbrl_fillings:
        by_period[(filling.year, filling.period)].append(filling)

    cores = os.cpu_count() or 4
    with ProcessPoolExecutor(max_workers=cores) as executor:
        for (year, period), period_fillings in by_period.items():
            cache_file = cache_dir / f"{year}_{period}.parquet"
            if cache_file.is_file() and cache_file.stat().st_size > 0:
                continue
            log.info(
                "[PARSING_DEI] %d %s (%d filings)",
                year,
                period,
                len(period_fillings),
            )
            tasks_each_core = 4
            chunksize = max(1, len(period_fillings) // (cores * tasks_each_core))
            batch_results = executor.map(
                _parse_dei_filling, period_fillings, chunksize=chunksize
            )
            items = list(itertools.chain.from_iterable(batch_results))
            if items:
                df_period = MetadataItem.DataFrame(items)
                df_period.write_parquet(cache_file)

    parquet_files = list(cache_dir.glob("*.parquet"))
    if not parquet_files:
        return MetadataItem.DataFrame()
    return MetadataItem.validate(pl.read_parquet(cache_dir / "*.parquet"))


def dei_metadata(
    staged_dei_items: pt.DataFrame[MetadataItem],
) -> pt.DataFrame[DeiMetadata]:
    if staged_dei_items.is_empty():
        return DeiMetadata.DataFrame()

    key_properties = [
        "EntityName",
        "EntityCode",
        "Sector",
        "Subsector",
        "Industry",
        "Subindustry",
        "DescriptionOfPresentationCurrency",
        "TypeOfReportOnFinancialStatements",
        "TypeOfAuditorsOpinion",
        "CurrentYearAuditor",
        "CurrentPeriodStartDate",
        "CurrentPeriodEndDate",
    ]

    filtered = staged_dei_items.filter(pl.col("property").is_in(key_properties))

    pivoted = filtered.pivot(
        on="property",
        index=["emiten_code", "year", "period"],
        values="value",
        aggregate_function="first",
    )

    return DeiMetadata.validate(pivoted)
