# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests,re
#네이버 기사 url만 바꾸기: 따옴표 안에 url을 붙여넣으세요.
url = ''
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')

# 요약본만 가져오기 
# for i in soup.find('strong',{'class':'media_end_summary'}):
#     print(i)
# # 제목만 가져오기
# for i in soup.find('h3',{'id':'articleTitle'}):
#     print(i)

# # 기사입력시간
# for i in soup.find('span',{'class':'t11'}):
#     print(i)

#페이지 따라가서 크롤링하기 
url2='https://finance.naver.com/sise/sise_index_time.nhn?code=KPI200&thistime=20210114170300&page='
for i in range(1,3):
    url = url2 + str(i)
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url2, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    soup.find_all('table')