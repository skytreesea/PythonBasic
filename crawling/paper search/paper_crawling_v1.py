# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests 
import re
# 국회 도서관 자료를 이용
Name = "김창현"

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
#국회도서관 api 키를 공공데이터서비스에서 받아서 사용 중(아직까지 트래픽 이슈는 없음)
url = 'https://apis.data.go.kr/9720000/searchservice/basic?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageno=1&displaylines=10&search=저자,'+Name 
urls = []
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')
 
dataset = [i.find('value').text for i in soup.find_all("item") ] 

for i in dataset[:10]:
    if re.search('[각-힣]+ [각-힣]+', i):
        print (i)
    else:
        pass
 
 