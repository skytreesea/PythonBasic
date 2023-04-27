from bs4 import BeautifulSoup
import requests,  re
my_name = '김용창'
my_university = '서울대' 
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
} 
def purify(s):
    # 문자열 s에서 ['kaist', '카이스트', '가이스트'] 중 하나가 있으면 'KAIST'로 변환하여 반환하는 함수

    s = s.lower()
    # ['kaist', '카이스트', '가이스트'] 중 하나가 있으면 'KAIST'로 변환합니다.
    for keyword in ['kaist', '카이스트', '가이스트']:
        s = s.replace(keyword, 'KAIST')
    for keyword in ['포항공대', '포스텍', 'postech']:
        s = s.replace(keyword, '포항공과')
    for keyword in ['서울태', '서울ㄷ', 'snu']:
        s = s.replace(keyword, '서울대')
    return s
      

def get_papers(name, university):
    university = purify(university)
    #학위논문
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query='+ name +'&queryText=&iStartCount=0&iGroupView=10&icate=all&colName=bib_t&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=1000'
    #학술논문
    url2 = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery='+name+'&exQuery=regnm%3AKCI%EB%93%B1%EC%9E%AC%E2%97%88regnm%3AKCI%EB%93%B1%EC%9E%AC%ED%9B%84%EB%B3%B4%E2%97%88&exQueryText=%EB%93%B1%EC%9E%AC%EC%A0%95%EB%B3%B4+%5BKCI%EB%93%B1%EC%9E%AC%5D%40%40regnm%3AKCI%EB%93%B1%EC%9E%AC%E2%97%88%EB%93%B1%EC%9E%AC%EC%A0%95%EB%B3%B4+%5BKCI%EB%93%B1%EC%9E%AC%ED%9B%84%EB%B3%B4%5D%40%40regnm%3AKCI%EB%93%B1%EC%9E%AC%ED%9B%84%EB%B3%B4%E2%97%88&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=%EA%B9%80%EC%B0%BD%ED%98%84&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=20&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query='+ name
    success, fail = 0, 0
    items = []
    soup = BeautifulSoup(requests.get(url, headers = headers).text, 'html.parser')
    soup2 = BeautifulSoup(requests.get(url2, headers = headers).text, 'html.parser')
    print('############여기서부터 학위논문###########')
    for row in soup.select('div.srchResultListW > ul > li'): 
        try:
        # name과 university를 포함했을 때에만 정보를 불러오게 함 
            if re.search(university, row.select_one("span.assigned").text) and re.search(name, row.select_one("span.writer").text):
                newData = [
                row.select_one("p.title").text,
                row.select_one("span.writer").text,
                row.select_one("span.assigned").text, 
                'http://www.riss.kr' + row.select_one("p.title > a").attrs["href"]
                ]
                print(newData)
            #items.append(newData)
        except:
            fail += 1
            print(f"{fail}번 실패")

    print('############여기서부터 학술논문###########')
    for row in soup2.select('div.srchResultListW > ul > li'): 
        try:
        # name만 포함했을 때에만 정보를 불러오게 함 
            if re.search(name, row.select_one("span.writer").text):
                newData = [
                row.select_one("p.title").text,
                row.select_one("span.writer").text,
                row.select_one("span.assigned").text, 
                'http://www.riss.kr' + row.select_one("p.title > a").attrs["href"]
                ]
                print(newData)
            #items.append(newData)
            # 저자가 여러명일 때,
            else:
                if writer in row.select("span.writer") == name:
                    print(name)
        except:
            fail += 1
            print(f"{fail}번 실패")
    
get_papers(my_name, my_university)
