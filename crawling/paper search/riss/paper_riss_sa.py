
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

def purify(s):
    # 문자열 s에서 ['kaist', '카이스트', '가이스트'] 중 하나가 있으면 'KAIST'로 변환하여 반환하는 함수
    s = s.lower()
    # ['kaist', '카이스트', '가이스트'] 중 하나가 있으면 'KAIST'로 변환합니다.
    for keyword in ['kaist', '카이스트', '가이스트', 'Korea Advanced Institute of Science and Technology']:
        s = s.replace(keyword, 'KAIST')
    for keyword in ['포항공대', '포스텍', 'postech']:
        s = s.replace(keyword, '포항공과')
    for keyword in ['서울태', '서울ㄷ', 'snu', '서울대학', '서울대학교']:
        s = s.replace(keyword, '서울대')
    return s


def get_papers(author, authority):
    # 학교 이름을  입력한 경우에 대비하여
    authority = purify(authority)
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=' + author + '&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=bib_t&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=1000'
    # 연도 필더링 테스트
    year_test = '2014'
    year_test_list = ['2014', '2015', '2019']
    success, fail = 0, 0
    items = []

    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

    # 학위논문
    for row in soup.select('div.srchResultListW > ul > li'):
        try:
            tmp_etcs = row.select("p.etc > span") 
            if re.search(authority, row.select_one("span.assigned").text):  # 조건 테스트: re.search(author,row.select_one("span.writer").text) and tmp_etcs[2].text == year_test
                newData = [
                    row.select_one("p.title").text,
                    author,
                    authority,
                    tmp_etcs[2].text if len(tmp_etcs) > 2 else None,
                    tmp_etcs[3].text if len(tmp_etcs) > 3 else None,  # 박사/석사 구분 HTML 추가 필요
                    'http://www.riss.kr' + row.select_one("p.title > a").attrs["href"]
                ]
                items.append(newData)
                success += 1
        except:
            fail += 1
    print(f'학위논문성공 {success}')
    print(f'학위논문실패 {fail}')    
   # return items

print(get_papers('윤세찬','kaist'))

