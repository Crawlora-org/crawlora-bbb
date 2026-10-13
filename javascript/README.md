# @crawlora-org/bbb — Better Business Bureau API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Better Business Bureau API.
It exposes 17 API endpoints for business search, profiles, complaints, reviews, categories, and ScamTracker reports through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-javascript-homepage). It does not run a browser or scrape Better Business Bureau locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Better Business Bureau or its owners.

## Install

```sh
npm install @crawlora-org/bbb
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { BBBClient } from "@crawlora-org/bbb";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new BBBClient({ apiKey });
const result1 = await client.search({ query: "coffee", location: "New York, NY" });
console.log(result1);
const result2 = await client.business({ url: "https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803" });
console.log(result2);
const result3 = await client.scamtrackerSearch({ query: "package delivery", state: "NY" });
console.log(result3);
```

The client also exports `Client` as an alias for `BBBClient`. Operation
methods are available directly in camelCase and through the `bbb`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-bbb/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-bbb/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Better Business Bureau API endpoints

This package exposes each route below as a direct method and through the `bbb` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-bbb/blob/main/docs/usage.md) for complete input details.

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
| `GET` | `/bbb/page` | `bbb-page` | Get a BBB evergreen page |
| `GET` | `/bbb/regions` | `bbb-regions` | List Better Business Bureau directory regions |
| `GET` | `/bbb/scamtracker/search` | `bbb-scamtracker-search` | Search Better Business Bureau Scam Tracker reports |
| `GET` | `/bbb/scamtracker/state-stats` | `bbb-scamtracker-state-stats` | Get Better Business Bureau Scam Tracker state/province aggregate stats |
| `GET` | `/bbb/scamtracker/{id}` | `bbb-scamtracker-detail` | Get a Better Business Bureau Scam Tracker report |
| `GET` | `/bbb/search` | `bbb-search` | Search Better Business Bureau businesses |
| `GET` | `/bbb/search/filters` | `bbb-search-filters` | Discover Better Business Bureau search filters |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
