import requests
from bs4 import BeautifulSoup 
url = 'https://en.dict.naver.com/#/search?query=arrow'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'} # 봇으로 인식하지 않도록 브라우져
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
print(soup.find_all('a'))