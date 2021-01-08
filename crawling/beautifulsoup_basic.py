# 뷰티풀수프
from bs4 import BeautifulSoup 
import requests
url = 'https://www.naver.com/'
req = requests.get(url)
soup = BeautifulSoup(req.text)
a_list = soup.find_all('a')
print([i.text for i in a_list])