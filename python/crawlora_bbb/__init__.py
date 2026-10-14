"""Typed Better Business Bureau client for the Crawlora hosted API."""

from .platform import BBBClient, AsyncBBBClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BBBClient
AsyncClient = AsyncBBBClient
__version__ = '0.6.0'
DISPLAY_NAME = 'Better Business Bureau'
PLATFORM = 'bbb'
CONTRACT_REVISION = 'sha256:36a641c351110f2052aa82b8b347c191d3b046d36429078907c0b4b08c1e1936'

__all__ = [
    "BBBClient", "AsyncBBBClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
