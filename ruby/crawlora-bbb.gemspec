require_relative "lib/crawlora/bbb/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-bbb"
  spec.version = Crawlora::Bbb::VERSION
  spec.summary = "Better Business Bureau client for the Crawlora hosted API"
  spec.description = "Credential-free Better Business Bureau API access through Crawlora's hosted service."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://github.com/Crawlora-org/crawlora-bbb"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-bbb", "rubygems_mfa_required" => "true" }

end
