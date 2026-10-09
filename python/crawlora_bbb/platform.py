"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class BBBClient(CrawloraClient):
    """Synchronous Better Business Bureau API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-bbb-python/0.2.0')
        super().__init__(*args, **kwargs)

    def article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-article', params, response_type=response_type, timeout=timeout, headers=headers)

    def business(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-business', params, response_type=response_type, timeout=timeout, headers=headers)

    def business_complaints(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-business-complaints', params, response_type=response_type, timeout=timeout, headers=headers)

    def business_more_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-business-more-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def business_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-business-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-category', params, response_type=response_type, timeout=timeout, headers=headers)

    def local_bbb(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-local-bbb', params, response_type=response_type, timeout=timeout, headers=headers)

    def local_bbbs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-local-bbbs', params, response_type=response_type, timeout=timeout, headers=headers)

    def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-news-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    def regions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-regions', params, response_type=response_type, timeout=timeout, headers=headers)

    def scamtracker_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-scamtracker-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def scamtracker_state_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-scamtracker-state-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def scamtracker_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-scamtracker-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('bbb-search-filters', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncBBBClient(AsyncCrawloraClient):
    """Asynchronous Better Business Bureau API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-bbb-python/0.2.0')
        super().__init__(*args, **kwargs)

    async def article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-article', params, response_type=response_type, timeout=timeout, headers=headers)

    async def business(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-business', params, response_type=response_type, timeout=timeout, headers=headers)

    async def business_complaints(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-business-complaints', params, response_type=response_type, timeout=timeout, headers=headers)

    async def business_more_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-business-more-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def business_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-business-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-category', params, response_type=response_type, timeout=timeout, headers=headers)

    async def local_bbb(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-local-bbb', params, response_type=response_type, timeout=timeout, headers=headers)

    async def local_bbbs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-local-bbbs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-news-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def regions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-regions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scamtracker_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-scamtracker-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scamtracker_state_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-scamtracker-state-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scamtracker_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-scamtracker-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('bbb-search-filters', params, response_type=response_type, timeout=timeout, headers=headers)
