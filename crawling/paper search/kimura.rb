require 'watir'
require 'webdrivers'
require 'nokogiri'
require 'open-uri'

#browser = Watir::Browser.new
#browser.goto 'https://apis.data.go.kr/9720000/searchservice/basic?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageno=1&displaylines=10&search=%EC%9E%90%EB%A3%8C%EB%AA%85,%EB%AF%B8%EA%B5%AD'

 
url = 'https://apis.data.go.kr/9720000/searchservice/basic?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageno=1&displaylines=10&search=%EC%9E%90%EB%A3%8C%EB%AA%85,%EB%AF%B8%EA%B5%AD'

parsed_page = Nokogiri::HTML(URI.open(url,{ssl_verify_mode: OpenSSL::SSL::VERIFY_NONE}))
puts parsed_page.css("value").text

#browser.close