require_relative "lib/crawlora/bbb/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-bbb"
  spec.version = Crawlora::Bbb::VERSION
  spec.summary = "Better Business Bureau API client for Crawlora (17 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Better Business Bureau API. Covers business search, profiles, complaints, reviews, categories, and ScamTracker reports across 17 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bbb-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-bbb", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-bbb/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
