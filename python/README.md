# crawlora-bbb — Better Business Bureau API client for Python

Python client for Crawlora's hosted Better Business Bureau API. It exposes 16 API endpoints covering business search, profiles, complaints, reviews, categories, and ScamTracker reports. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-python-homepage); the package does not run a browser or scrape
Better Business Bureau locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Better Business Bureau or its owners.

## Install

```sh
python -m pip install crawlora-bbb
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_bbb import BBBClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with BBBClient(api_key=api_key) as client:
    result_1 = client.search(query='coffee', location='New York, NY')
    print(result_1)
    result_2 = client.business(url='https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803')
    print(result_2)
    result_3 = client.scamtracker_search(query='package delivery', state='NY')
    print(result_3)
```

The package also exports `Client` as an alias for `BBBClient`. Operation
methods are available directly in snake_case and through the `bbb`
group. The async package client is `AsyncBBBClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-bbb/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-bbb/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_bbb import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(query='coffee', location='New York, NY')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-bbb/blob/main/examples/python.py) for a complete usage example.

## Supported Better Business Bureau API endpoints

This package exposes every route below through direct snake_case methods and the `bbb` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-bbb/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/bbb/article` | `bbb-article` | Get a BBB article |
| `GET` | `/bbb/business` | `bbb-business` | Get a Better Business Bureau business profile |
| `GET` | `/bbb/business/complaints` | `bbb-business-complaints` | Get a Better Business Bureau business's complaint history |
| `GET` | `/bbb/business/more-info` | `bbb-business-more-info` | Get a Better Business Bureau business's full rating reasons and service area |
| `GET` | `/bbb/business/reviews` | `bbb-business-reviews` | Get a Better Business Bureau business's customer reviews |
| `GET` | `/bbb/category` | `bbb-category` | Browse a Better Business Bureau category |
| `GET` | `/bbb/local-bbb` | `bbb-local-bbb` | Get a local BBB chapter profile |
| `GET` | `/bbb/local-bbbs` | `bbb-local-bbbs` | List local BBB chapters serving a region |
| `GET` | `/bbb/news` | `bbb-news` | Get BBB newsroom stories |
| `GET` | `/bbb/news/topics` | `bbb-news-topics` | List BBB newsroom topics |
| `GET` | `/bbb/regions` | `bbb-regions` | List Better Business Bureau directory regions |
| `GET` | `/bbb/scamtracker/search` | `bbb-scamtracker-search` | Search Better Business Bureau Scam Tracker reports |
| `GET` | `/bbb/scamtracker/state-stats` | `bbb-scamtracker-state-stats` | Get Better Business Bureau Scam Tracker state/province aggregate stats |
| `GET` | `/bbb/scamtracker/{id}` | `bbb-scamtracker-detail` | Get a Better Business Bureau Scam Tracker report |
| `GET` | `/bbb/search` | `bbb-search` | Search Better Business Bureau businesses |
| `GET` | `/bbb/search/filters` | `bbb-search-filters` | Discover Better Business Bureau search filters |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
