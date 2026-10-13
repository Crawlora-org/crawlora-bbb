"""Typed Better Business Bureau client for the Crawlora hosted API."""

from .platform import BBBClient, AsyncBBBClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BBBClient
AsyncClient = AsyncBBBClient
__version__ = '0.5.0'
DISPLAY_NAME = 'Better Business Bureau'
PLATFORM = 'bbb'
CONTRACT_REVISION = 'sha256:74857e4df2d9776bfc5fb5cfe84d86326f53f87fe240204c62463f2ac4310a6a'

__all__ = [
    "BBBClient", "AsyncBBBClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
