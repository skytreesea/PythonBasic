# 국회도서관 크롤링 1차 성공
from bs4 import BeautifulSoup  
import requests 
import re

Name = '윤세찬'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
 
url = 'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageno=1&displaylines=100&search=저자,'+Name 
urls = []
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'xml')
#제어번호  
from bs4 import BeautifulSoup
#학위논문 제어번호: KDMT1201237821
#일반보고서 제어번호: NONB1201516520
#일반논문: KINX2013124087
# 두 리스트가 있을 때 이것을 dataset으로 만들어주는 코드 필요 
def make_list_to_dict(list1, list2):
    result = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            result[list1[i]]=list2[i]
    return result
    
data=[]
# Loop through all <item> tags
for recode in soup.find_all('recode'):
    for i in recode.find_all('item'):
        if i.find('name').text =='지도교수':
            data.append(make_list_to_dict(
            [i.text for i in recode.find_all('name')] ,
            [i.text for i in recode.find_all('value')]
            )
            )
print(data[0])
print(data[1])
            
        
        