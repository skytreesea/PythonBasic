# 국회도서관 크롤링: 사람이름 입력후 제어번호 찾기, 제어 번호 찾은 후 초록과 논문 정보 찾기
from bs4 import BeautifulSoup
import requests
import re
from warnings import simplefilter
author = '김창현'
controlno_sample = 'KDMT1201106059'

# 태그가 있다면 없애주는 함수
def remove_tags(html):
    # Remove HTML tags using regular expressions
    clean_text = re.sub('<.*?>', '', html)
    return clean_text

def get_paper_minister(controlNo):
    result = {
    'year': None,  # 발행년도  DETAIL_PUB 
    'author': None, # 저자
    'title_1': None, # main 제목
    'title_2': None, # sub 제목
    'supervisor': None, # 지도교수(검색조건 김창현 또는 Jamie Kim)
    'gubun': None, # 석박사
    'abstract': None # 초록 
}

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

    url =  'http://dl.nanet.go.kr/search/searchInnerDetail.do?controlNo=' + controlNo
    soup = BeautifulSoup(requests.get(url, verify=False, headers=headers).text, 'lxml')
    #필수정보
    result['controlNo'] = controlNo
    result['year'] = re.findall("\d\d\d\d",re.split(',', soup.find('dl', {'id': 'DETAIL_PUB'}).text)[-1])[-1]
    result['author'] = re.sub(r'\n\n','',re.split('/', soup.find('dl', {'id': 'DP_TITLE_FULL'}).text)[-1])
    result['title_1'] = re.sub(r'저자명\n\n','', re.split(r'=',re.split('/', soup.find('dl', {'id': 'DP_TITLE_FULL'}).text)[-2])[0])
    try:
        result['gubun'] = re.findall('학위.+', re.split('--', soup.find('dl', {'id': 'DETAIL_REMARK'}).text)[0])[0]
    except:
        print('no 구분')
    try:
        result['title_2'] = re.split(r'=',re.split('/', soup.find('dl', {'id': 'DP_TITLE_FULL'}).text)[-2])[1]
    except:
        print("no title 2")
    try:
        result['supervisor'] = re.findall(r'지도교수:\s*(\w+ \w+|\w+)',soup.find('dl', {'id': 'DETAIL_REMARK'}).text)[0]
    except:
        print('no supervisor')
    try:
        for i in soup.find_all('div',{'class':'scrollY'}):
            result['abstract'] = (i.find_all('p')[0].text.strip('\ufeff'))
    except:
        print('no abstract')
    return result 
     
nos = ['KDMT12023000005375',
'KDMT12023000005376',
'KDMT12021000006731',
'KDMT12021000006732',
'KDMT12021000006733',
'KDMT12021000006734',
'KDMT1201304119',
'KDMT1201304120',
'KDMT1201304121',
'KDMT1201304122',
'KDMT1201848652',
'KDMT12021000006735',
'KDMT12023000005378']

for i in nos:
    print(get_paper_minister(i))