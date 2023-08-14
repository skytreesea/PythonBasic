# 명언 사이트 크롤링 
import requests 
from bs4 import BeautifulSoup
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
url = 'http://quotes.toscrape.com/' 
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')
# 기본 명령어로 quote라는 class를 가진 div에서 text만 찾아서 출력함
for i in soup.find_all('div',{"class":"quote"}):
    print(i.find('span',{'class':'text'}).text)
