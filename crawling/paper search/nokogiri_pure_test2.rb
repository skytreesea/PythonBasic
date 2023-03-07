require 'nokogiri'
require 'open-uri'
require 'openssl'
# 다음기사
url = 'https://news.daum.net/'

# 중요한 코드 한 줄 

parsed_page = Nokogiri::HTML(URI.open(url,{ssl_verify_mode: OpenSSL::SSL::VERIFY_NONE}))

href={}
titles = parsed_page.xpath("//div[@class='cont_thumb']").css("a").map{|link| link.text.strip}
links = parsed_page.xpath("//div[@class='cont_thumb']").css("a").map{|link| link["href"]} 

puts links
 
 


