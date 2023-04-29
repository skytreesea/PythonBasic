# At present, it doesn't work. 
# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests 
import re
#검색할 저자 이름
Name = '윤세찬'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
 
url = 'https://scholar.google.com/scholar?hl=ko&as_sdt=0%2C5&q='  + Name
urls = []
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')
# 아직 아주 기본적인 코드만 짜놓음 추후 개발 예정
print(soup.find_all('div',{"class":"gs_ri"}) )
 