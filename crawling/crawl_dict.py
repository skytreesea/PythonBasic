# 다음사전 크롤링 초기 버젼 
import requests 
from bs4 import BeautifulSoup
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
url = 'https://dic.daum.net/search.do?q=life&dic=eng' 
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')

# 뜻 찾기 
for i in soup.find_all('span',{"class":"txt_search"}):
    print(i.text)
     
#예문 찾기 
for i in soup.find_all('ul',{"class":"list_example sound_example"}):
    print(i.text)
