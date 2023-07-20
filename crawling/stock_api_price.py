import requests 
from bs4 import BeautifulSoup

# 내 서비스키를 이용해서 만든 예제 코드 
url = 'https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&numOfRows=100'
 
def add_commas(num):
    num_str = str(num)
    result = ''
    count = 0
    for i in range(len(num_str) - 1, -1, -1):
        result = num_str[i] + result
        count += 1
        if count % 3 == 0 and i != 0:
            result = ',' + result
    return result
    

# 일반 크롤링 코드와 유사함
def soupMaker(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml') 
    return soup
    
for i in soupMaker(url).find_all('items'):
    total = []
    total.append(i.select('basdt'))
    total.append(i.select('itmsnm'))
    total.append(i.select('mrktctg'))
    total.append(i.select('mkp'))


for i in range(50):
    print(total[0][i].text, '\t', total[1][i].text, '\t', total[2][i].text, '\t',add_commas(total[3][i].text))