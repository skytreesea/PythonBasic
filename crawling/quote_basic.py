# 명언 사이트 크롤링 
import requests 
from bs4 import BeautifulSoup
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
url = 'http://quotes.toscrape.com/' 
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')
for i in soup.find_all('div',{"class":"quote"}):
    try:
        print(i.find('span',{'class':'text'}).text)
    except UnicodeEncodeError as e:
        print(f"Error encoding character: {e}")
        # 유니코드 인코드 에러는 챗GPT로 해결 