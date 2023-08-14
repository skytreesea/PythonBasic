# 국회도서관 크롤링: 상세페이지에서 정보 꺼내기
from bs4 import BeautifulSoup
import requests
import re
from warnings import simplefilter
author = '김창현'
controlno_sample = 'KDMT1201106059'
# 두 리스트가 있을 때 이것을 dataset으로 만들어주는 코드 필요
def make_list_to_dict(list1, list2):
    result = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            result[list1[i]] = list2[i]
    return result

# 태그가 있다면 없애주는 함수
def remove_tags(html):
    # Remove HTML tags using regular expressions
    clean_text = re.sub('<.*?>', '', html)
    return clean_text

def get_paper_minister(controlNo):
    data = []
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

    url =  'http://dl.nanet.go.kr/search/searchInnerDetail.do?controlNo=' + controlNo
    soup = BeautifulSoup(requests.get(url, verify=False, headers=headers).text, 'lxml')
    # Loop through all <item> tags
    
    with open(r'C:\Users\skytr\Documents\GitHub\GixpertUtilWorker\data\a_new_result2.txt','w') as f:
        for i in soup.find_all('div',{'class':'scrollY'}):
             f.write(i.find_all('p')[0].text.strip('\ufeff'))
             print(i.find_all('p')[0].text.strip('\ufeff'))
           
        try:  
            supervisor = re.search(r'지도교수:\s*(\w+)', soup.find('dl', {'id': 'DETAIL_REMARK'}).text)
            f.write(supervisor.group(1))

        except:
            print('정보 없음')


get_paper_minister(controlno_sample)
 
	                                                   
	                                                   