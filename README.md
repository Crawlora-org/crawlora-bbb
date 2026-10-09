# Better Business Bureau clients for Crawlora

Official Crawlora client packages for the hosted Better Business Bureau API. These clients call Crawlora's hosted API; they do not scrape Better Business Bureau locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Better Business Bureau or its owners.

- JavaScript / TypeScript: [`@crawlora-org/bbb`](javascript/README.md)
- Python: [`crawlora-bbb`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-bbb`](go.mod)
- Ruby: [`crawlora-bbb`](ruby/README.md)
- Java: [`net.crawlora:crawlora-bbb:0.1.1`](java/README.md)
- PHP: [`crawlora/bbb`](php/README.md)
- [API endpoint and parameter reference](docs/usage.md)
- [Runnable examples](examples/)
- [Package repository](https://github.com/Crawlora-org/crawlora-bbb)

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-repository-api-docs).

## Install

```sh
npm install @crawlora-org/bbb
python -m pip install crawlora-bbb
go get github.com/Crawlora-org/crawlora-bbb@latest
gem install crawlora-bbb
composer require crawlora/bbb
```

For Java, add `net.crawlora:crawlora-bbb:0.1.1` to your Maven dependencies; see [java/README.md](java/README.md).

Set your API key before running a client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

Do not commit API keys. See each language README for runnable usage examples.

## PHP example

```sh
composer require crawlora/bbb
```

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$apiKey = getenv('CRAWLORA_API_KEY');
if (!$apiKey) throw new RuntimeException('Set CRAWLORA_API_KEY before running this example.');
$client = new \Crawlora\Bbb\Client(apiKey: $apiKey);
$result = $client->request("bbb-search", ['query' => 'coffee', 'location' => 'New York, NY']);
print_r($result);
$client->close();
```

## API coverage

The six clients provide access to 9 public API operations. See the [API reference](docs/usage.md) for supported operations, parameters, and response details.

## License

MIT. See [LICENSE](LICENSE).
