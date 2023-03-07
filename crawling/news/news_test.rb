require 'nokogiri'
require 'open-uri'
require 'openssl'
# table_test 액션을 위한 테스트

titles = []
links = []
urlnews =  'https://news.daum.net/'

def callurl(url)
    return Nokogiri::HTML(URI.open(url,{ssl_verify_mode: OpenSSL::SSL::VERIFY_NONE}))
end
parsed = callurl(urlnews)

titles = parsed.xpath("//div[@class='cont_thumb']").css("a").map{|link| link.text.strip}
links = parsed.xpath("//div[@class='cont_thumb']").css("a").map{|link| link["href"]} 


url2 = 'https://v.daum.net/v/20230212000022935'
#parsed2 = callurl(url2)
#p parsed2.css(".article_view").css("p").text 
puts url2.match(/\d+/)  