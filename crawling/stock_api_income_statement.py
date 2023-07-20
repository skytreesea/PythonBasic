import requests 
from bs4 import BeautifulSoup
crnos = {
'삼성전자':'1301110006246',
'네이버':'1101111707178',
'LG전자':'1101112487050',
'카카오':'1101111129497'}
# 내 서비스키를 이용해서 만든 예제 코드 
url = 'https://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2/getIncoStat_V2?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&numOfRows=1&pageNo=1&resultType=xml&bizYear=2022&crno='
 
# 일반 크롤링 코드와 유사함
def soupMaker(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml') 
    return soup
    
for i in crnos.keys():
    try:
        soup = soupMaker(url + crnos[i])
        print(i, soup.find('acitnm').text)
        print(soup.find('crtmacitamt').text)
        print(soup.find('pvtracitamt').text)
    except:
        pass