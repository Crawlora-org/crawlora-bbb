# Better Business Bureau client usage

The `@crawlora-org/bbb` and `crawlora-bbb` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Better Business Bureau locally; Crawlora is independent from and not endorsed by Better Business Bureau or its owners.

The package tracks the public API contract revision `sha256:c4cf6f235ba96193e786f97a88b354660c07e34d9ae86429136e17dacb7efd48` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 9 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `bbb` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `business` / `business` | `GET /bbb/business` | `url` (query, required) | Get a Better Business Bureau business profile |
| `businessComplaints` / `business_complaints` | `GET /bbb/business/complaints` | `url` (query, required) | Get a Better Business Bureau business's complaint history |
| `businessMoreInfo` / `business_more_info` | `GET /bbb/business/more-info` | `url` (query, required) | Get a Better Business Bureau business's full rating reasons and service area |
| `businessReviews` / `business_reviews` | `GET /bbb/business/reviews` | `url` (query, required), `page` (query, optional) | Get a Better Business Bureau business's customer reviews |
| `category` / `category` | `GET /bbb/category` | `url` (query, required), `page` (query, optional) | Browse a Better Business Bureau category |
| `scamtrackerDetail` / `scamtracker_detail` | `GET /bbb/scamtracker/{id}` | `id` (path, required) | Get a Better Business Bureau Scam Tracker report |
| `scamtrackerSearch` / `scamtracker_search` | `GET /bbb/scamtracker/search` | `query` (query, optional), `scam_type` (query, optional; values: `Advance Fee Loan`, `Bank/Credit Card Company Imposter`, `Business Email Compromise`, `Charity`, `Counterfeit Product`, `COVID-19`, `Credit Cards`, `Credit Repair/Debt Relief`, `CryptoCurrency`, `Debt Collections`, `Employment`, `Fake Check/Money Order`, `Fake Invoice/Supplier Bill`, `Family/Friend Emergency`, `Foreign Money Exchange`, `Government Agency Imposter`, `Government Grant`, `Healthcare/Medicaid/Medicare`, `Home Improvement`, `Identity Theft`, `Investment`, `Moving`, `Online Purchase`, `Other`, `Phishing`, `Rental`, `Retail Business`, `Romance`, `Scholarship`, `Sweepstakes/Lottery/Prizes`, `Tax Collection`, `Tech Support`, `Travel/Vacation/Timeshare`, `Utility`, `Vanity Award`, `Worthless Problem-solving Service`, `Yellow Pages/Directories`), `state` (query, optional), `scammer_state` (query, optional), `date_from` (query, optional), `date_to` (query, optional), `min_dollars_lost` (query, optional), `max_dollars_lost` (query, optional), `page` (query, optional) | Search Better Business Bureau Scam Tracker reports |
| `scamtrackerStateStats` / `scamtracker_state_stats` | `GET /bbb/scamtracker/state-stats` | `period` (query, optional; values: `30`, `90`, `365`, `all`) | Get Better Business Bureau Scam Tracker state/province aggregate stats |
| `search` / `search` | `GET /bbb/search` | `query` (query, required), `location` (query, required), `page` (query, optional) | Search Better Business Bureau businesses |

## Client forms

- JavaScript: import `BBBClient` (also exported as `Client`) from `@crawlora-org/bbb`; use `new BBBClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `BBBClient` (also exported as `Client`) from `crawlora_bbb`; use `with BBBClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncBBBClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
