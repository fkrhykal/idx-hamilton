import abc
import logging
import time
from abc import abstractmethod
from typing import Any, override

from curl_cffi import Response, Session
from curl_cffi.requests.impersonate import DEFAULT_CHROME

log = logging.getLogger(__name__)


class HttpClient(abc.ABC):
    @abstractmethod
    def get(self, url: str, **kwargs: Any) -> Response:
        pass


class IdxHttpClient(HttpClient):
    def __init__(
        self,
        impersonate: str = DEFAULT_CHROME,
        min_interval_seconds: float = 1.5,
        timeout: int = 30,
    ):
        self._session = Session(
            impersonate=impersonate,
        )
        self._min_interval = min_interval_seconds
        self._timeout = timeout
        self._is_fresh = True
        self._last_request_time = 0.0

    @override
    def get(self, url: str, max_retries: int = 3, **kwargs: Any) -> Response:
        kwargs.setdefault("timeout", self._timeout)

        if self._is_fresh:
            self._session.get(
                "https://www.idx.co.id/en/listed-companies/financial-statements-and-annual-report/"
            ).raise_for_status()

            time.sleep(1)

            self._is_fresh = False

        for attempt in range(max_retries):
            now = time.monotonic()
            elapsed = now - self._last_request_time
            if elapsed < self._min_interval:
                time.sleep(self._min_interval - elapsed)
            self._last_request_time = time.monotonic()
            res = self._session.get(url, **kwargs)
            if res.status_code in (502, 503, 504) and attempt < max_retries - 1:
                wait_time = (attempt + 1) * 3.0
                time.sleep(wait_time)
                continue
            return res
        return res
