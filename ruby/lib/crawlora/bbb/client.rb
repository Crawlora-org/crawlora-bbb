require "json"
require "net/http"
require "uri"

module Crawlora
  module Bbb
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"bbb-article": {"id": "bbb-article", "method": "GET", "params": [{"description": "Canonical BBB article URL", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/article/news-releases/34935-bbb-scam-alert-dont-be-fooled-by-free-gas-and-grocery-card-postcards"}], "path": "/bbb/article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-business": {"id": "bbb-business", "method": "GET", "params": [{"description": "BBB business profile URL, from a bbb-search result's url or hq_profile_url", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803"}], "path": "/bbb/business", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-business-complaints": {"id": "bbb-business-complaints", "method": "GET", "params": [{"description": "BBB business profile URL, from a bbb-search result's url or hq_profile_url", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803"}], "path": "/bbb/business/complaints", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-business-more-info": {"id": "bbb-business-more-info", "method": "GET", "params": [{"description": "BBB business profile URL, from a bbb-search result's url or hq_profile_url", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803"}], "path": "/bbb/business/more-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-business-reviews": {"id": "bbb-business-reviews", "method": "GET", "params": [{"description": "BBB business profile URL, from a bbb-search result's url or hq_profile_url", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803"}, {"description": "Result page (10 per page), default 1", "in": "query", "name": "page", "type": "integer"}], "path": "/bbb/business/reviews", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bbb-category": {"id": "bbb-category", "method": "GET", "params": [{"description": "BBB category browse URL, from a bbb-search result's related_categories", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/us/tx/austin/category/plumber"}, {"description": "Result page, default 1", "in": "query", "name": "page", "type": "integer"}, {"description": "Sort order", "enum": ["Relevance", "Distance", "Rating", "AToZ", "ZToA"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum distance in miles; omit for all distances", "enum": ["5", "10", "25", "50", "100"], "in": "query", "name": "distance", "type": "string"}, {"collectionFormat": "multi", "description": "One or more BBB rating buckets", "in": "query", "items": {"enum": ["A", "B", "C", "D", "F"], "type": "string"}, "name": "rating", "type": "array"}, {"collectionFormat": "multi", "description": "Query-scoped category ID from bbb-search-filters", "in": "query", "items": {"type": "string"}, "name": "category_id", "type": "array"}, {"collectionFormat": "multi", "description": "Query-scoped state or province code from bbb-search-filters", "in": "query", "items": {"type": "string"}, "name": "state", "type": "array"}, {"description": "Only BBB-accredited businesses", "in": "query", "name": "accredited", "type": "boolean"}, {"description": "Only businesses offering quote requests", "in": "query", "name": "get_quote", "type": "boolean"}, {"description": "Only businesses serving the searched area", "in": "query", "name": "service_area", "type": "boolean"}], "path": "/bbb/category", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["Relevance", "Distance", "Rating", "AToZ", "ZToA"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["5", "10", "25", "50", "100"], "in": "query", "name": "distance", "type": "string"}, {"collectionFormat": "multi", "enum": ["A", "B", "C", "D", "F"], "in": "query", "name": "rating", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "category_id", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "state", "type": "array"}, {"in": "query", "name": "accredited", "type": "boolean"}, {"in": "query", "name": "get_quote", "type": "boolean"}, {"in": "query", "name": "service_area", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "bbb-local-bbb": {"id": "bbb-local-bbb", "method": "GET", "params": [{"description": "Canonical BBB chapter URL from bbb-local-bbbs or a business record's local_bbb_url", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/local-bbb/bbb-serving-the-heart-of-texas"}], "path": "/bbb/local-bbb", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-local-bbbs": {"id": "bbb-local-bbbs", "method": "GET", "params": [{"description": "Country code from bbb-regions", "enum": ["us", "ca"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "us"}, {"description": "Two-letter region code from bbb-regions", "in": "query", "name": "region", "required": true, "type": "string", "x-example": "tx"}], "path": "/bbb/local-bbbs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["us", "ca"], "in": "query", "name": "country", "required": true, "type": "string"}, {"in": "query", "name": "region", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-news": {"id": "bbb-news", "method": "GET", "params": [{"description": "Canonical BBB newsroom or topic page URL; include page=N for pagination", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/us/news/scams?page=2"}], "path": "/bbb/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-news-topics": {"id": "bbb-news-topics", "method": "GET", "params": [{"description": "Canonical BBB newsroom page URL", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https://www.bbb.org/us/news"}], "path": "/bbb/news/topics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-regions": {"id": "bbb-regions", "method": "GET", "params": [], "path": "/bbb/regions", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "bbb-scamtracker-detail": {"id": "bbb-scamtracker-detail", "method": "GET", "params": [{"description": "BBB Scam Tracker report id, from a bbb-scamtracker-search result's id or url", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1397968"}], "path": "/bbb/scamtracker/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "bbb-scamtracker-search": {"id": "bbb-scamtracker-search", "method": "GET", "params": [{"description": "Free-text search (phone number, website, email, business name, scam ID, description). Omit to browse the most-recent feed", "in": "query", "name": "query", "type": "string", "x-example": "amazon"}, {"description": "Scam category filter", "enum": ["Advance Fee Loan", "Bank/Credit Card Company Imposter", "Business Email Compromise", "Charity", "Counterfeit Product", "COVID-19", "Credit Cards", "Credit Repair/Debt Relief", "CryptoCurrency", "Debt Collections", "Employment", "Fake Check/Money Order", "Fake Invoice/Supplier Bill", "Family/Friend Emergency", "Foreign Money Exchange", "Government Agency Imposter", "Government Grant", "Healthcare/Medicaid/Medicare", "Home Improvement", "Identity Theft", "Investment", "Moving", "Online Purchase", "Other", "Phishing", "Rental", "Retail Business", "Romance", "Scholarship", "Sweepstakes/Lottery/Prizes", "Tax Collection", "Tech Support", "Travel/Vacation/Timeshare", "Utility", "Vanity Award", "Worthless Problem-solving Service", "Yellow Pages/Directories"], "in": "query", "name": "scam_type", "type": "string"}, {"description": "Optional 2-letter targeted-victim state/province code (US state or Canadian province)", "in": "query", "name": "state", "type": "string", "x-example": "TX"}, {"description": "Optional 2-letter reported-scammer state/province code (US state or Canadian province) -- where the scammer is reported to be, not the victim", "in": "query", "name": "scammer_state", "type": "string", "x-example": "NY"}, {"description": "Optional report-date range start (YYYY-MM-DD), inclusive. Must be set together with date_to", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-01-01"}, {"description": "Optional report-date range end (YYYY-MM-DD), inclusive. Must be set together with date_from", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-01-31"}, {"description": "Optional minimum reported dollar loss. Must be set together with max_dollars_lost", "in": "query", "name": "min_dollars_lost", "type": "integer", "x-example": 500000}, {"description": "Optional maximum reported dollar loss. Must be set together with min_dollars_lost", "in": "query", "name": "max_dollars_lost", "type": "integer", "x-example": 1000000}, {"description": "Result page (10 per page), default 1", "in": "query", "name": "page", "type": "integer"}], "path": "/bbb/scamtracker/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"enum": ["Advance Fee Loan", "Bank/Credit Card Company Imposter", "Business Email Compromise", "Charity", "Counterfeit Product", "COVID-19", "Credit Cards", "Credit Repair/Debt Relief", "CryptoCurrency", "Debt Collections", "Employment", "Fake Check/Money Order", "Fake Invoice/Supplier Bill", "Family/Friend Emergency", "Foreign Money Exchange", "Government Agency Imposter", "Government Grant", "Healthcare/Medicaid/Medicare", "Home Improvement", "Identity Theft", "Investment", "Moving", "Online Purchase", "Other", "Phishing", "Rental", "Retail Business", "Romance", "Scholarship", "Sweepstakes/Lottery/Prizes", "Tax Collection", "Tech Support", "Travel/Vacation/Timeshare", "Utility", "Vanity Award", "Worthless Problem-solving Service", "Yellow Pages/Directories"], "in": "query", "name": "scam_type", "type": "string"}, {"in": "query", "name": "state", "type": "string"}, {"in": "query", "name": "scammer_state", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}, {"in": "query", "name": "min_dollars_lost", "type": "integer"}, {"in": "query", "name": "max_dollars_lost", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "bbb-scamtracker-state-stats": {"id": "bbb-scamtracker-state-stats", "method": "GET", "params": [{"description": "Aggregation window, default 90", "enum": ["30", "90", "365", "all"], "in": "query", "name": "period", "type": "string"}], "path": "/bbb/scamtracker/state-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["30", "90", "365", "all"], "in": "query", "name": "period", "type": "string"}], "security": ["ApiKeyAuth"]}, "bbb-search": {"id": "bbb-search", "method": "GET", "params": [{"description": "Business name or category/service keyword", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "plumber"}, {"description": "City and state (e.g. 'Austin, TX') or a ZIP code", "in": "query", "name": "location", "required": true, "type": "string", "x-example": "Austin, TX"}, {"description": "Result page, default 1", "in": "query", "name": "page", "type": "integer"}, {"default": "USA", "description": "BBB country code", "enum": ["USA", "CAN"], "in": "query", "name": "country", "type": "string"}, {"description": "Sort order", "enum": ["Relevance", "Distance", "Rating", "AToZ", "ZToA"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum distance in miles; omit for all distances", "enum": ["5", "10", "25", "50", "100"], "in": "query", "name": "distance", "type": "string"}, {"collectionFormat": "multi", "description": "One or more BBB rating buckets", "in": "query", "items": {"enum": ["A", "B", "C", "D", "F"], "type": "string"}, "name": "rating", "type": "array"}, {"collectionFormat": "multi", "description": "Query-scoped category ID from bbb-search-filters", "in": "query", "items": {"type": "string"}, "name": "category_id", "type": "array"}, {"collectionFormat": "multi", "description": "Query-scoped state or province code from bbb-search-filters", "in": "query", "items": {"type": "string"}, "name": "state", "type": "array"}, {"description": "Only BBB-accredited businesses", "in": "query", "name": "accredited", "type": "boolean"}, {"description": "Only businesses offering quote requests", "in": "query", "name": "get_quote", "type": "boolean"}, {"description": "Only businesses serving the searched area", "in": "query", "name": "service_area", "type": "boolean"}], "path": "/bbb/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "location", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["USA", "CAN"], "in": "query", "name": "country", "type": "string"}, {"enum": ["Relevance", "Distance", "Rating", "AToZ", "ZToA"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["5", "10", "25", "50", "100"], "in": "query", "name": "distance", "type": "string"}, {"collectionFormat": "multi", "enum": ["A", "B", "C", "D", "F"], "in": "query", "name": "rating", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "category_id", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "state", "type": "array"}, {"in": "query", "name": "accredited", "type": "boolean"}, {"in": "query", "name": "get_quote", "type": "boolean"}, {"in": "query", "name": "service_area", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "bbb-search-filters": {"id": "bbb-search-filters", "method": "GET", "params": [{"description": "Business name or category/service keyword; use with location when category_url is omitted", "in": "query", "name": "query", "type": "string", "x-example": "plumber"}, {"description": "City and state/province or ZIP code; use with query when category_url is omitted", "in": "query", "name": "location", "type": "string", "x-example": "Austin, TX"}, {"description": "BBB category browse URL; use instead of query and location", "in": "query", "name": "category_url", "type": "string", "x-example": "https://www.bbb.org/us/tx/austin/category/plumber"}, {"default": "USA", "description": "BBB country code", "enum": ["USA", "CAN"], "in": "query", "name": "country", "type": "string"}, {"description": "Result page, default 1", "in": "query", "name": "page", "type": "integer"}, {"description": "Sort order", "enum": ["Relevance", "Distance", "Rating", "AToZ", "ZToA"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum distance in miles; omit for all distances", "enum": ["5", "10", "25", "50", "100"], "in": "query", "name": "distance", "type": "string"}, {"collectionFormat": "multi", "description": "Selected rating values", "in": "query", "items": {"enum": ["A", "B", "C", "D", "F"], "type": "string"}, "name": "rating", "type": "array"}, {"collectionFormat": "multi", "description": "Selected category IDs previously returned for this search context", "in": "query", "items": {"type": "string"}, "name": "category_id", "type": "array"}, {"collectionFormat": "multi", "description": "Selected state/province codes previously returned for this search context", "in": "query", "items": {"type": "string"}, "name": "state", "type": "array"}, {"description": "Only BBB-accredited businesses", "in": "query", "name": "accredited", "type": "boolean"}, {"description": "Only businesses offering quote requests", "in": "query", "name": "get_quote", "type": "boolean"}, {"description": "Only businesses serving the searched area", "in": "query", "name": "service_area", "type": "boolean"}], "path": "/bbb/search/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"in": "query", "name": "location", "type": "string"}, {"in": "query", "name": "category_url", "type": "string"}, {"enum": ["USA", "CAN"], "in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["Relevance", "Distance", "Rating", "AToZ", "ZToA"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["5", "10", "25", "50", "100"], "in": "query", "name": "distance", "type": "string"}, {"collectionFormat": "multi", "enum": ["A", "B", "C", "D", "F"], "in": "query", "name": "rating", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "category_id", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "state", "type": "array"}, {"in": "query", "name": "accredited", "type": "boolean"}, {"in": "query", "name": "get_quote", "type": "boolean"}, {"in": "query", "name": "service_area", "type": "boolean"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["bbb-article", "bbb-business", "bbb-business-complaints", "bbb-business-more-info", "bbb-business-reviews", "bbb-category", "bbb-local-bbb", "bbb-local-bbbs", "bbb-news", "bbb-news-topics", "bbb-regions", "bbb-scamtracker-detail", "bbb-scamtracker-search", "bbb-scamtracker-state-stats", "bbb-search", "bbb-search-filters"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-bbb-ruby/0.2.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = Net::HTTP::Get.new(uri)
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = @transport.call(url, request.to_hash, @timeout)
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('article') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-article', params, response_type: response_type)
      end
      define_method('business') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-business', params, response_type: response_type)
      end
      define_method('business_complaints') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-business-complaints', params, response_type: response_type)
      end
      define_method('business_more_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-business-more-info', params, response_type: response_type)
      end
      define_method('business_reviews') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-business-reviews', params, response_type: response_type)
      end
      define_method('category') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-category', params, response_type: response_type)
      end
      define_method('local_bbb') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-local-bbb', params, response_type: response_type)
      end
      define_method('local_bbbs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-local-bbbs', params, response_type: response_type)
      end
      define_method('news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-news', params, response_type: response_type)
      end
      define_method('news_topics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-news-topics', params, response_type: response_type)
      end
      define_method('regions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-regions', params, response_type: response_type)
      end
      define_method('scamtracker_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-scamtracker-search', params, response_type: response_type)
      end
      define_method('scamtracker_state_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-scamtracker-state-stats', params, response_type: response_type)
      end
      define_method('scamtracker_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-scamtracker-detail', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-search', params, response_type: response_type)
      end
      define_method('search_filters') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('bbb-search-filters', params, response_type: response_type)
      end

      private

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
