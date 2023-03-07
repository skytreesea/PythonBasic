require 'nokogiri'
require 'open-uri'
require 'cgi'
require 'openssl'
def change_url(name)
    return CGI.escape name #한글을 %#@# 이런 형태로 바꿔주는...
    end
author = change_url('김용창')    
url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query='+ author  
parsed_page = Nokogiri::HTML(URI.open(url,{ssl_verify_mode: OpenSSL::SSL::VERIFY_NONE}))
parsed_page.css(".srchResultListW").css('.title').css('a').map(&:values).each do |t|
    puts t 
end

#browser.close