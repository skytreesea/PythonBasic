# 국회도서관 크롤링 1차 성공
from bs4 import BeautifulSoup  
import requests 
import re
import requests
from bs4 import BeautifulSoup

author = '김창현'
url = 'https://www.earticle.net/Search/Result?aq='+ author +'&jt=&c1=&c2=&y=2019-2023&issn=&ps=1D50' 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
response = requests.get(url, verify=True)

# 이하 파싱 코드
soup = BeautifulSoup(response.text, 'html.parser')
#제어번호  
from bs4 import BeautifulSoup
def make_list_to_dict(list1, list2):
    result = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            result[list1[i]]=list2[i]
    return result
 
# Loop through all <item> tags
for recode in soup.find_all('div', {"class":"info"}):
    print(recode.text)
 
        
        