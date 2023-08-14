import requests
import requests 
from bs4 import BeautifulSoup
url = 'https://apis.data.go.kr/B552540/KCIOpenApi/artiInfo/openApiM330List?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&recordCnt=20&pageNo=1'
 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml') 
 
for i in soup.find_all('SEAR_CRET_KOR_NM'.lower()):
    print(i.text)