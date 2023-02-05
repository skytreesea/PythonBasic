
def scrape
  url = 'https://www.cars.com/shopping/sedan/'
  response = VehiclesSpider.process(url)
  if response[:status] == :completed && response[:error].nil?
    flash.now[:notice] = "Successfully scraped url"
  else
    flash.now[:alert] = response[:error]
  end
rescue StandardError => e
  flash.now[:alert] = "Error: #{e}"
end

scrape 