"""Typed Better Business Bureau client for the Crawlora hosted API."""

from .platform import BBBClient, AsyncBBBClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BBBClient
AsyncClient = AsyncBBBClient
__version__ = '0.7.0'
DISPLAY_NAME = 'Better Business Bureau'
PLATFORM = 'bbb'
CONTRACT_REVISION = 'sha256:20f92e653763923b1828617ebb5afc09d2e590cc5acbd669f8064cb075c358be'

__all__ = [
    "BBBClient", "AsyncBBBClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
