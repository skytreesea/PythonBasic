# At present, it doesn't work. 
# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests 
import re
#네이버 기사 url만 바꾸기: 따옴표 안에 url을 붙여넣으세요.
Name = input("권규상")

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
 
url = 'https://scholar.google.com/scholar?hl=ko&as_sdt=0%2C5&q='  + Name
urls = []
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')
# 각 상품정보에서 특정 정보를 리스트 형태로 모으기(데이터프레임 용)
print(soup.find_all('div',{"class":"gs_ri"}) )
 