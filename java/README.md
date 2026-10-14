# Crawlora Better Business Bureau API client for Java

The official Java client for Crawlora's hosted Better Business Bureau API. It exposes 17 endpoints covering business search, profiles, complaints, reviews, categories, and ScamTracker reports. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-bbb</artifactId>
  <version>0.6.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-java-console) to get an API key.

```java
import net.crawlora.bbb.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("query", "coffee"), Map.entry("location", "New York, NY")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Better Business Bureau API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-bbb/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-bbb)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-java-api-docs)
