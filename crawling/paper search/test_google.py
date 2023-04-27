import requests
from bs4 import BeautifulSoup

# 구글 검색 URL 생성
query = '김용창'
earticle_url = f'https://www.earticle.net/Search/Result?sf=1&q={query}'

# 구글 검색 페이지에서 HTML 가져오기
response = requests.get(earticle_url)
html = response.content

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 결과 출력
#print(soup.find_all('span', {'class': 'gs_ctc'}))
for i in soup.find_all('div', {'class': 'info'})[:10]:
    print(i.find('p'), {'class': 'title'})