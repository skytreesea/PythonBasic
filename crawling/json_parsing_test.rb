require 'json'

#filepath = 'C:\Users\ERC\Documents\김창현의 모든 자료\김창현 개인\coderKim\PythonBasic-master\데이터\ai hub\번역예제\일상생활및구어체_영한_valid_set.json'
filepath = 'C:\Users\ERC\Documents\김창현의 모든 자료\김창현 개인\coderKim\PythonBasic-master\데이터\ai hub\번역예제\일상생활및구어체_한영_valid_set.json'
file = File.read(filepath)
jsondata = JSON.load file
#puts jsondata["data"][0]

#갯수를 정해서 출력할 수 있도록 함
(1500..1520).each do |t|
    puts jsondata["data"][t]["ko"] 
    puts jsondata["data"][t]["en"] 
end
puts jsondata["data"].size