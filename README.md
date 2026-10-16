# Better Business Bureau clients for Crawlora

Official Crawlora client packages for the hosted Better Business Bureau API. Access 17 API endpoints covering business search, profiles, complaints, reviews, categories, and ScamTracker reports from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape Better Business Bureau locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Better Business Bureau or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/bbb`](javascript/README.md)
- Python: [`crawlora-bbb`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-bbb`](go.mod)
- Ruby: [`crawlora-bbb`](ruby/README.md)
- Java: [`net.crawlora:crawlora-bbb:0.7.1`](java/README.md)
- PHP: [`crawlora/bbb`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 17 selected public Better Business Bureau API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
