# 뷰티풀수프
from bs4 import BeautifulSoup 
import requests
#기본명령
url ='https://n.news.naver.com/mnews/article/015/0004871030?sid=105'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')

#텍스트만 출력 - 
for i in soup.find_all('div',{'id':'newsct_article'}):
    print(i.text)

