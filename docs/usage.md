# Better Business Bureau API endpoint reference and client usage

This reference lists all 17 public Better Business Bureau API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/bbb`, `crawlora-bbb`, and `crawlora-bbb` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Better Business Bureau locally; Crawlora is independent from and not endorsed by Better Business Bureau or its owners.

The package tracks the public API contract revision `sha256:87c46a47bf53d834b6c3bdb183a5897ad430ce73273684e9bcbe73106e4df086` bundled with release `0.7.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `bbb`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `article` | `article` | `bbb.article` | `GET /bbb/article` | `url` (query, required) | Get a BBB article |
| `business` | `business` | `bbb.business` | `GET /bbb/business` | `url` (query, required) | Get a Better Business Bureau business profile |
| `businessComplaints` | `business_complaints` | `bbb.business_complaints` | `GET /bbb/business/complaints` | `url` (query, required), `page` (query, optional) | Get a Better Business Bureau business's complaint history |
| `businessMoreInfo` | `business_more_info` | `bbb.business_more_info` | `GET /bbb/business/more-info` | `url` (query, required) | Get a Better Business Bureau business's full rating reasons and service area |
| `businessReviews` | `business_reviews` | `bbb.business_reviews` | `GET /bbb/business/reviews` | `url` (query, required), `page` (query, optional) | Get a Better Business Bureau business's customer reviews |
| `category` | `category` | `bbb.category` | `GET /bbb/category` | `url` (query, required), `page` (query, optional), `sort` (query, optional; values: `Relevance`, `Distance`, `Rating`, `AToZ`, `ZToA`), `distance` (query, optional; values: `5`, `10`, `25`, `50`, `100`), `rating` (query, optional; values: `A`, `B`, `C`, `D`, `F`), `category_id` (query, optional), `state` (query, optional), `accredited` (query, optional), `get_quote` (query, optional), `service_area` (query, optional) | Browse a Better Business Bureau category |
| `localBbb` | `local_bbb` | `bbb.local_bbb` | `GET /bbb/local-bbb` | `url` (query, required) | Get a local BBB chapter profile |
| `localBbbs` | `local_bbbs` | `bbb.local_bbbs` | `GET /bbb/local-bbbs` | `country` (query, required; values: `us`, `ca`), `region` (query, required) | List local BBB chapters serving a region |
| `news` | `news` | `bbb.news` | `GET /bbb/news` | `url` (query, required) | Get BBB newsroom stories |
| `newsTopics` | `news_topics` | `bbb.news_topics` | `GET /bbb/news/topics` | `url` (query, required) | List BBB newsroom topics |
| `page` | `page` | `bbb.page` | `GET /bbb/page` | `url` (query, required) | Get a BBB evergreen page |
| `regions` | `regions` | `bbb.regions` | `GET /bbb/regions` | — | List Better Business Bureau directory regions |
| `scamtrackerDetail` | `scamtracker_detail` | `bbb.scamtracker_detail` | `GET /bbb/scamtracker/{id}` | `id` (path, required) | Get a Better Business Bureau Scam Tracker report |
| `scamtrackerSearch` | `scamtracker_search` | `bbb.scamtracker_search` | `GET /bbb/scamtracker/search` | `query` (query, optional), `scam_type` (query, optional; values: `Advance Fee Loan`, `Bank/Credit Card Company Imposter`, `Business Email Compromise`, `Charity`, `Counterfeit Product`, `COVID-19`, `Credit Cards`, `Credit Repair/Debt Relief`, `CryptoCurrency`, `Debt Collections`, `Employment`, `Fake Check/Money Order`, `Fake Invoice/Supplier Bill`, `Family/Friend Emergency`, `Foreign Money Exchange`, `Government Agency Imposter`, `Government Grant`, `Healthcare/Medicaid/Medicare`, `Home Improvement`, `Identity Theft`, `Investment`, `Moving`, `Online Purchase`, `Other`, `Phishing`, `Rental`, `Retail Business`, `Romance`, `Scholarship`, `Sweepstakes/Lottery/Prizes`, `Tax Collection`, `Tech Support`, `Travel/Vacation/Timeshare`, `Utility`, `Vanity Award`, `Worthless Problem-solving Service`, `Yellow Pages/Directories`), `state` (query, optional), `scammer_state` (query, optional), `date_from` (query, optional), `date_to` (query, optional), `min_dollars_lost` (query, optional), `max_dollars_lost` (query, optional), `page` (query, optional) | Search Better Business Bureau Scam Tracker reports |
| `scamtrackerStateStats` | `scamtracker_state_stats` | `bbb.scamtracker_state_stats` | `GET /bbb/scamtracker/state-stats` | `period` (query, optional; values: `30`, `90`, `365`, `all`) | Get Better Business Bureau Scam Tracker state/province aggregate stats |
| `search` | `search` | `bbb.search` | `GET /bbb/search` | `query` (query, required), `location` (query, required), `page` (query, optional), `country` (query, optional; values: `USA`, `CAN`), `sort` (query, optional; values: `Relevance`, `Distance`, `Rating`, `AToZ`, `ZToA`), `distance` (query, optional; values: `5`, `10`, `25`, `50`, `100`), `rating` (query, optional; values: `A`, `B`, `C`, `D`, `F`), `category_id` (query, optional), `state` (query, optional), `accredited` (query, optional), `get_quote` (query, optional), `service_area` (query, optional) | Search Better Business Bureau businesses |
| `searchFilters` | `search_filters` | `bbb.search_filters` | `GET /bbb/search/filters` | `query` (query, optional), `location` (query, optional), `category_url` (query, optional), `country` (query, optional; values: `USA`, `CAN`), `page` (query, optional), `sort` (query, optional; values: `Relevance`, `Distance`, `Rating`, `AToZ`, `ZToA`), `distance` (query, optional; values: `5`, `10`, `25`, `50`, `100`), `rating` (query, optional; values: `A`, `B`, `C`, `D`, `F`), `category_id` (query, optional), `state` (query, optional), `accredited` (query, optional), `get_quote` (query, optional), `service_area` (query, optional) | Discover Better Business Bureau search filters |

## Client forms

- JavaScript: import `BBBClient` (also exported as `Client`) from `@crawlora-org/bbb`; use `new BBBClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `BBBClient` (also exported as `Client`) from `crawlora_bbb`; use `with BBBClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncBBBClient`, used with `async with` and `await`.
- Rust: add `crawlora-bbb` with Cargo; import `Client` and the generated operation parameter struct, then call `client.bbb.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-bbb/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
