"""Typed Better Business Bureau client for the Crawlora hosted API."""

from .platform import BBBClient, AsyncBBBClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BBBClient
AsyncClient = AsyncBBBClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Better Business Bureau'
PLATFORM = 'bbb'
CONTRACT_REVISION = 'sha256:c4cf6f235ba96193e786f97a88b354660c07e34d9ae86429136e17dacb7efd48'

__all__ = [
    "BBBClient", "AsyncBBBClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
