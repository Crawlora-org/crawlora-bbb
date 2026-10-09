package net.crawlora.bbb;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Better Business Bureau endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 16;
    public static final List<String> OPERATION_IDS = List.of(
            "bbb-article",
            "bbb-business",
            "bbb-business-complaints",
            "bbb-business-more-info",
            "bbb-business-reviews",
            "bbb-category",
            "bbb-local-bbb",
            "bbb-local-bbbs",
            "bbb-news",
            "bbb-news-topics",
            "bbb-regions",
            "bbb-scamtracker-detail",
            "bbb-scamtracker-search",
            "bbb-scamtracker-state-stats",
            "bbb-search",
            "bbb-search-filters"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("bbb-article", new Operation("bbb-article", "GET", "/bbb/article", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-business", new Operation("bbb-business", "GET", "/bbb/business", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-business-complaints", new Operation("bbb-business-complaints", "GET", "/bbb/business/complaints", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-business-more-info", new Operation("bbb-business-more-info", "GET", "/bbb/business/more-info", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-business-reviews", new Operation("bbb-business-reviews", "GET", "/bbb/business/reviews", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-category", new Operation("bbb-category", "GET", "/bbb/category", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("Relevance", "Distance", "Rating", "AToZ", "ZToA"), "csv")), Map.entry("distance", new Param("distance", "query", false, "string", List.of("5", "10", "25", "50", "100"), "csv")), Map.entry("rating", new Param("rating", "query", false, "array", List.of("A", "B", "C", "D", "F"), "multi")), Map.entry("category_id", new Param("category_id", "query", false, "array", List.of(), "multi")), Map.entry("state", new Param("state", "query", false, "array", List.of(), "multi")), Map.entry("accredited", new Param("accredited", "query", false, "boolean", List.of(), "csv")), Map.entry("get_quote", new Param("get_quote", "query", false, "boolean", List.of(), "csv")), Map.entry("service_area", new Param("service_area", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-local-bbb", new Operation("bbb-local-bbb", "GET", "/bbb/local-bbb", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-local-bbbs", new Operation("bbb-local-bbbs", "GET", "/bbb/local-bbbs", Map.ofEntries(Map.entry("country", new Param("country", "query", true, "string", List.of("us", "ca"), "csv")), Map.entry("region", new Param("region", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-news", new Operation("bbb-news", "GET", "/bbb/news", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-news-topics", new Operation("bbb-news-topics", "GET", "/bbb/news/topics", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-regions", new Operation("bbb-regions", "GET", "/bbb/regions", Map.of(), List.of("application/json")));
        operations.put("bbb-scamtracker-search", new Operation("bbb-scamtracker-search", "GET", "/bbb/scamtracker/search", Map.ofEntries(Map.entry("query", new Param("query", "query", false, "string", List.of(), "csv")), Map.entry("scam_type", new Param("scam_type", "query", false, "string", List.of("Advance Fee Loan", "Bank/Credit Card Company Imposter", "Business Email Compromise", "Charity", "Counterfeit Product", "COVID-19", "Credit Cards", "Credit Repair/Debt Relief", "CryptoCurrency", "Debt Collections", "Employment", "Fake Check/Money Order", "Fake Invoice/Supplier Bill", "Family/Friend Emergency", "Foreign Money Exchange", "Government Agency Imposter", "Government Grant", "Healthcare/Medicaid/Medicare", "Home Improvement", "Identity Theft", "Investment", "Moving", "Online Purchase", "Other", "Phishing", "Rental", "Retail Business", "Romance", "Scholarship", "Sweepstakes/Lottery/Prizes", "Tax Collection", "Tech Support", "Travel/Vacation/Timeshare", "Utility", "Vanity Award", "Worthless Problem-solving Service", "Yellow Pages/Directories"), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of(), "csv")), Map.entry("scammer_state", new Param("scammer_state", "query", false, "string", List.of(), "csv")), Map.entry("date_from", new Param("date_from", "query", false, "string", List.of(), "csv")), Map.entry("date_to", new Param("date_to", "query", false, "string", List.of(), "csv")), Map.entry("min_dollars_lost", new Param("min_dollars_lost", "query", false, "integer", List.of(), "csv")), Map.entry("max_dollars_lost", new Param("max_dollars_lost", "query", false, "integer", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-scamtracker-state-stats", new Operation("bbb-scamtracker-state-stats", "GET", "/bbb/scamtracker/state-stats", Map.ofEntries(Map.entry("period", new Param("period", "query", false, "string", List.of("30", "90", "365", "all"), "csv"))), List.of("application/json")));
        operations.put("bbb-scamtracker-detail", new Operation("bbb-scamtracker-detail", "GET", "/bbb/scamtracker/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-search", new Operation("bbb-search", "GET", "/bbb/search", Map.ofEntries(Map.entry("query", new Param("query", "query", true, "string", List.of(), "csv")), Map.entry("location", new Param("location", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of("USA", "CAN"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("Relevance", "Distance", "Rating", "AToZ", "ZToA"), "csv")), Map.entry("distance", new Param("distance", "query", false, "string", List.of("5", "10", "25", "50", "100"), "csv")), Map.entry("rating", new Param("rating", "query", false, "array", List.of("A", "B", "C", "D", "F"), "multi")), Map.entry("category_id", new Param("category_id", "query", false, "array", List.of(), "multi")), Map.entry("state", new Param("state", "query", false, "array", List.of(), "multi")), Map.entry("accredited", new Param("accredited", "query", false, "boolean", List.of(), "csv")), Map.entry("get_quote", new Param("get_quote", "query", false, "boolean", List.of(), "csv")), Map.entry("service_area", new Param("service_area", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("bbb-search-filters", new Operation("bbb-search-filters", "GET", "/bbb/search/filters", Map.ofEntries(Map.entry("query", new Param("query", "query", false, "string", List.of(), "csv")), Map.entry("location", new Param("location", "query", false, "string", List.of(), "csv")), Map.entry("category_url", new Param("category_url", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of("USA", "CAN"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("Relevance", "Distance", "Rating", "AToZ", "ZToA"), "csv")), Map.entry("distance", new Param("distance", "query", false, "string", List.of("5", "10", "25", "50", "100"), "csv")), Map.entry("rating", new Param("rating", "query", false, "array", List.of("A", "B", "C", "D", "F"), "multi")), Map.entry("category_id", new Param("category_id", "query", false, "array", List.of(), "multi")), Map.entry("state", new Param("state", "query", false, "array", List.of(), "multi")), Map.entry("accredited", new Param("accredited", "query", false, "boolean", List.of(), "csv")), Map.entry("get_quote", new Param("get_quote", "query", false, "boolean", List.of(), "csv")), Map.entry("service_area", new Param("service_area", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Better Business Bureau operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest request = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation))
                .GET().build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object article(Map<String, ?> params) { return request("bbb-article", params); }
    public Object business(Map<String, ?> params) { return request("bbb-business", params); }
    public Object businessComplaints(Map<String, ?> params) { return request("bbb-business-complaints", params); }
    public Object businessMoreInfo(Map<String, ?> params) { return request("bbb-business-more-info", params); }
    public Object businessReviews(Map<String, ?> params) { return request("bbb-business-reviews", params); }
    public Object category(Map<String, ?> params) { return request("bbb-category", params); }
    public Object localBbb(Map<String, ?> params) { return request("bbb-local-bbb", params); }
    public Object localBbbs(Map<String, ?> params) { return request("bbb-local-bbbs", params); }
    public Object news(Map<String, ?> params) { return request("bbb-news", params); }
    public Object newsTopics(Map<String, ?> params) { return request("bbb-news-topics", params); }
    public Object regions(Map<String, ?> params) { return request("bbb-regions", params); }
    public Object scamtrackerSearch(Map<String, ?> params) { return request("bbb-scamtracker-search", params); }
    public Object scamtrackerStateStats(Map<String, ?> params) { return request("bbb-scamtracker-state-stats", params); }
    public Object scamtrackerDetail(Map<String, ?> params) { return request("bbb-scamtracker-detail", params); }
    public Object search(Map<String, ?> params) { return request("bbb-search", params); }
    public Object searchFilters(Map<String, ?> params) { return request("bbb-search-filters", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
