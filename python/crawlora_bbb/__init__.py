"""Typed Better Business Bureau client for the Crawlora hosted API."""

from .platform import BBBClient, AsyncBBBClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BBBClient
AsyncClient = AsyncBBBClient
__version__ = '0.7.1'
DISPLAY_NAME = 'Better Business Bureau'
PLATFORM = 'bbb'
CONTRACT_REVISION = 'sha256:87c46a47bf53d834b6c3bdb183a5897ad430ce73273684e9bcbe73106e4df086'

__all__ = [
    "BBBClient", "AsyncBBBClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
