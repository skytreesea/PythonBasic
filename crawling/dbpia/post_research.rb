# Success! But it isn't free and expensive for me and gixpert. api_key is only available for 100 times. 
# url = "https://serpapi.com/search-api"

require 'google_search_results' 

keyword = "진중권"
params = {
  engine: "google_scholar",
  q: keyword,
  api_key: "c87922ae37647d6fb10f2459b3e84757530811f8de4af26645fc985ecfbe94bc"
}

search = GoogleSearch.new(params)
organic_results = search.get_hash[:organic_results]
organic_results.each do |t|
  puts t[:title] 
end

