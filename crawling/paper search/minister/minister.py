import secrets
import string
import re
from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
#
from app import schemas
#from app.database import crud, models
#
from app.error import exceptions
from bs4 import BeautifulSoup
import requests
from app.utils import univ_names

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
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
def purify(s):
    # 문자열 s에서 ['kaist', '카이스트', '가이스트'] 중 하나가 있으면 'KAIST'로 변환하여 반환하는 함수
    s = s.lower()
    # ['kaist', '카이스트', '가이스트'] 중 하나가 있으면 'KAIST'로 변환합니다.
    for keyword in ['kaist', '카이스트', '가이스트','한국과학기술원','Korea Advanced Institute of Science and Technology']:
        s = s.replace(keyword, 'KAIST')
    for keyword in ['포항공대', '포스텍', 'postech']:
        s = s.replace(keyword, '포항공과')
    for keyword in ['서울태', '서울ㄷ', 'snu','서울대학','서울대학교']:
        s = s.replace(keyword, '서울대')
    for keyword in ['總神大學校']:
        s = s.replace(keyword, '총신대')
    return s
      
def get_papers(schema: schemas.PapersSearchIn) -> schemas.PaperSearchOut:
    author = schema.name
    #연도 필더링 테스트
    success, fail= 0, 0
    #학위논문
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    items = []
    url = 'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageno=1&displaylines=1000&search=저자,' + author
    soup = BeautifulSoup(requests.get(url, verify=False, headers=headers).text, 'lxml')
    # Loop through all <item> tags
    try:
        for recode in soup.find_all('recode'):
            for i in recode.find_all('item'):
                if i.find('name').text == '지도교수':
                    newData = make_list_to_dict(
                        [i.text for i in recode.find_all('name')],
                        [remove_tags(i.text) for i in recode.find_all('value')]
                    )
                    #'제어번호', '논문명', '지도교수', '저자명', '발행자', '키워드', '목차', '전공', 'DDC', '청구기호', '본문언어', '저작권허락', '초록유무', '학위년도', '별치기호', '원본DB유무', '음성지원유무', '자료실'])

                    newData = schemas.PaperItem(
                        title=newData['논문명'],
                        author=newData['저자명'],
                        university=newData['발행자'],
                        norm_university=newData['발행자'],
                        year=newData[ '학위년도'],
                        gubun=newData['전공'],  # 박사/석사 구분 HTML 추가 필요
                        link=newData[ '키워드']
                    )
                    success += 1
                    items.append(newData)
    except:
        fail += 1
    ret = schemas.PaperSearchOut(
        items=items,
        success=success,
        fail=fail,
        )
    print(fail)
    return ret
