# frozen_string_literal: true

source 'http://rubygems.org'

git_source(:github) { |repo_name| "https://github.com/#{repo_name}" }

# Synchronize with https://pages.github.com/versions
# As for 14.05.2026 "commonmarker" is not compatible with ruby >= 4.0.0
ruby '>=3.2.0', '<4.0.0' 

gem 'github-pages', '232', group: :jekyll_plugins
gem "bigdecimal"
gem "webrick", "~> 1.7"

# Issues for some compilers
gem "jekyll-commonmark-ghpages", "~> 0.5.1"
gem "commonmarker", "~> 0.23.12"
gem "faraday-retry", "~> 2.4"
gem "wdm", ">= 0.1.0"
