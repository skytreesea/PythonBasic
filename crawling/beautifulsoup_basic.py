# 뷰티풀수프
from bs4 import BeautifulSoup 
import requests
url = 'https://www.naver.com/'
req = requests.get(url)
#기본명령
soup = BeautifulSoup(req.text)
#a태그 리스트로 반환
a_list = soup.find_all('a')
#텍스트만 출력
print([i.text for i in a_list])