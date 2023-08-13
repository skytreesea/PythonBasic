import requests 
from bs4 import BeautifulSoup
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'} 

url ='https://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2/getSummFinaStat_V2?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&numOfRows=1&pageNo=1&resultType=xml&crno=1746110000741&bizYear=2019'
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')

print(soup.find('enpSaleAmt'.lower()).text)
