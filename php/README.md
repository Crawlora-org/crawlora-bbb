# Crawlora Better Business Bureau API client for PHP (`crawlora/bbb`)

This PHP package calls Crawlora's hosted Better Business Bureau API at `https://api.crawlora.net/api/v1`. It exposes 16 endpoints covering business search, profiles, complaints, reviews, categories, and ScamTracker reports. It does not call or scrape Better Business Bureau directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/bbb
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Bbb\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("bbb-search", ['query' => 'sample', 'location' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 16 API operations.

## Supported Better Business Bureau API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-bbb/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-bbb). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-bbb/blob/main/docs/usage.md).
