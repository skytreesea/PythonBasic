# 서울대 공대 연구실 주소 
# 뷰티풀수프
from bs4 import BeautifulSoup 
import requests, re, usecsv
#기본명령
url ='https://eng.snu.ac.kr/research?keys=&field_resetype_value=E&title=&department=All&page=1&language=ko'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
#텍스트만 출력 - 

new =  soup.find('ul',{'class':'lc09 research'}) 


text_info = [i.text for i in new.find_all('li')]
total = []

for i in text_info:
    split1 = re.split("\|",i) 
    final = re.split(r'\n\n',split1[0]) + split1[1:-1]  
    final.append(re.split(r'\n',split1[-1])[1])
    total.append(final)
    
print(total)