# crawlora-bbb

Python client for Crawlora's hosted Better Business Bureau API. It calls Crawlora's
service at [Crawlora](https://crawlora.net?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-python-homepage); it does not run a browser or scrape
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

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
