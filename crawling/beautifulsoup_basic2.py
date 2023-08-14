# 뷰티풀수프
from bs4 import BeautifulSoup 
import requests
#기본명령
url ='https://urban.yonsei.ac.kr/urban/research/urban_planning_members.do?mode=list&srSearchKey=&srSearchVal=&srCategoryId1=361'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
#텍스트만 출력 - 

new = [i for i in soup.find_all('div',{'class':'board-faculty-box'})] 

for i in new:
    print(i.find('img').get('alt')[:4])
    for j in i.find_all('dd'):
        print(j.text)