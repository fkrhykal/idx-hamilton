import io
import logging
import zipfile
from dataclasses import dataclass
from enum import StrEnum
from itertools import product
from pathlib import Path
from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, ValidationError
from result import Err, Ok, Result

from idx_hamilton.resources import (
    HttpClient,
)

log = logging.getLogger(__name__)


type Period = Literal["TW1", "TW2", "TW3", "Audit"]

type EmitenType = Literal["s", "o"]


class Extension(StrEnum):
    ZIP = ".zip"
    FAILED = ".failed"
    CORRUPTED = ".corrupted"
    JSON = ".json"


@dataclass(frozen=True)
class ReportQuery:
    year: int
    period: Period
    emiten_type: EmitenType


@dataclass(frozen=True)
class IxbrlFillingUrl:
    emiten_code: str
    year: int
    period: Period
    url: str


@dataclass(frozen=True)
class IxbrlFilling:
    emiten_code: str
    year: int
    period: Period
    zip_path: Path


class Attachment(BaseModel):
    Emiten_Code: str
    File_ID: str
    File_Modified: str
    File_Name: str
    File_Path: str
    File_Size: int
    File_Type: str
    Report_Period: str
    Report_Type: str
    Report_Year: str
    NamaEmiten: str


class QueryResult(BaseModel):
    KodeEmiten: str
    Attachments: list[Attachment]


class FinancialReportURL(BaseModel):
    model_config = ConfigDict(extra="ignore")
    Results: list[QueryResult]

    @classmethod
    def safe_validate(cls, data: dict | bytes | str) -> Result[Self, ValidationError]:
        try:
            if isinstance(data, (bytes, str)):
                return Ok(cls.model_validate_json(data))
            return Ok(cls.model_validate(data))
        except ValidationError as err:
            print(err)
            return Err(err)


def report_queries(
    years: tuple[int, ...] = (2021, 2022, 2023, 2024, 2025, 2026),
    periods: tuple[Period, ...] = ("TW1", "TW2", "TW3", "Audit"),
    emiten_types: tuple[EmitenType, ...] = ("s",),
) -> list[ReportQuery]:
    return [
        ReportQuery(year=y, period=p, emiten_type=e)
        for y, p, e in product(years, periods, emiten_types)
    ]


def financial_report_urls(
    report_queries: list[ReportQuery], idx_http_client: HttpClient
) -> list[tuple[ReportQuery, FinancialReportURL]]:
    cache_dir = Path(".data/sources/financial_report_url")

    cached: dict[str, Path] = {
        f.stem: f
        for f in cache_dir.iterdir()
        if f.is_file() and f.suffix == Extension.JSON
    }

    report_urls = []

    for q in report_queries:
        filename = f"{q.year}_{q.period}_{q.emiten_type}"

        cached_file = cached.get(filename)
        if cached_file and cached_file.stat().st_size > 0:
            result = FinancialReportURL.safe_validate(cached_file.read_bytes())
            if result.is_ok():
                report_urls.append((q, result.unwrap()))
                continue

        target_file = cache_dir.joinpath(filename).with_suffix(Extension.JSON)

        url = f"https://www.idx.co.id/primary/ListedCompany/GetFinancialReport?indexFrom=1&pageSize=99999&year={q.year}&reportType=rdf&EmitenType={q.emiten_type}&periode={q.period}"
        response = idx_http_client.get(url)

        if not response.ok:
            log.warning(
                "[FETCH_FAILED] HTTP %d -> %s", response.status_code, target_file
            )
            continue

        result = FinancialReportURL.safe_validate(response.json())
        if result.is_err():
            log.warning("[]")
            continue

        data = result.unwrap()
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(data.model_dump_json(indent=2))
        report_urls.append((q, data))

        cached[filename] = target_file

    return report_urls


def ixbrl_filling_urls(
    financial_report_urls: list[tuple[ReportQuery, FinancialReportURL]],
) -> list[IxbrlFillingUrl]:
    filling_urls = []
    for report_url in financial_report_urls:
        year = report_url[0].year
        period = report_url[0].period
        for result in report_url[1].Results:
            emiten_code = result.KodeEmiten.strip()
            candidates = (
                att
                for att in result.Attachments
                if att.File_Name.strip().lower() == "inlinexbrl.zip"
            )
            latest = max(candidates, key=lambda a: a.File_Modified, default=None)
            if not latest:
                log.warning(
                    "[IXBRL_MISSING] inlinexbrl.zip attachement missing for (%s, %d, %s)",
                    emiten_code,
                    year,
                    period,
                )
                continue
            filling_urls.append(
                IxbrlFillingUrl(
                    emiten_code=emiten_code,
                    year=year,
                    period=period,
                    url=latest.File_Path,
                )
            )
    return filling_urls


def ixbrl_fillings(
    ixbrl_filling_urls: list[IxbrlFillingUrl], idx_http_client: HttpClient
) -> list[IxbrlFilling]:
    root_dir = Path(".data/sources/ixbrl_financial_report")

    cached: dict[tuple[str, str], Path] = {}
    if root_dir.is_dir():
        for emiten_dir in root_dir.iterdir():
            if emiten_dir.is_dir() and not emiten_dir.name.startswith("."):
                for file_path in emiten_dir.iterdir():
                    if file_path.is_file() and file_path.suffix in (
                        Extension.ZIP,
                        Extension.CORRUPTED,
                        Extension.FAILED,
                    ):
                        cached[(emiten_dir.name, file_path.stem)] = file_path

    fillings = []

    for item in ixbrl_filling_urls:
        year_period = f"{item.year}_{item.period}"
        emiten = item.emiten_code
        cache_dir = root_dir / emiten / year_period

        key = (item.emiten_code, year_period)

        cached_file = cached.get(key)

        if cached_file is not None:
            if cached_file.suffix == Extension.CORRUPTED:
                log.warning("[CORRUPTED_ZIP] %s", cached_file)
                continue
            if cached_file.suffix == Extension.FAILED:
                log.warning("[INVALID_FILE] %s", cached_file)
                continue
            if cached_file.suffix == Extension.ZIP:
                fillings.append(
                    IxbrlFilling(
                        emiten_code=item.emiten_code,
                        year=item.year,
                        period=item.period,
                        zip_path=cached_file,
                    )
                )
            continue

        target_path = cache_dir.with_suffix(Extension.ZIP)
        failed_path = cache_dir.with_suffix(Extension.FAILED)
        corrupted_path = cache_dir.with_suffix(Extension.CORRUPTED)

        target_path.parent.mkdir(parents=True, exist_ok=True)

        log.info("[FETCH_IXBRL] %s", target_path)

        url = f"https://www.idx.co.id/{item.url.lstrip('/')}"
        res = idx_http_client.get(url)

        if res.status_code == 404:
            log.warning("[FETCH_FAILED] HTTP 404 -> %s (marked as .failed)", cache_dir)
            failed_path.write_text(f"HTTP_404: {url}")
            continue

        if not res.ok:
            log.warning("[FETCH_FAILED] HTTP %d -> %s", res.status_code, cache_dir)
            continue

        if not zipfile.is_zipfile(io.BytesIO(res.content)):
            log.warning(
                "[CORRUPTED_ZIP] invalid zip bytes -> %s (marked as .corrupted)",
                cache_dir,
            )
            corrupted_path.write_bytes(res.content)
            continue

        target_path.write_bytes(res.content)
        log.info("[IXBRL_SAVED] %s", target_path)

        cached[(item.emiten_code, year_period)] = target_path

        fillings.append(
            IxbrlFilling(
                emiten_code=item.emiten_code,
                year=item.year,
                period=item.period,
                zip_path=target_path,
            )
        )

    return fillings
