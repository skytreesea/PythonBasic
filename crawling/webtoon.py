#기본: 네이버 웹툰 순위 예쁘게 크롤링하기 
from bs4 import BeautifulSoup as bs
import requests,re
url = ('https://comic.naver.com/webtoon')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = bs(res.text, 'lxml')

# ol만 찾아서 text를 찾을 경우, 성공 그러나 지저분함
for div in soup.find_all('div', {'class':'TripleRecommendList__info_area--DVTdh'}):
    # Do something with the found <div> elements
    print(div)