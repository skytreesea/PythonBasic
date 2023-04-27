from bs4 import BeautifulSoup
import requests,  re
my_name = '김진영'
my_university = 'snu' 
 
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
      
def make_soup(name, university):
    university = purify(university)
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query='+ name +'&queryText=&iStartCount=0&iGroupView=10&icate=all&colName=bib_t&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=1000'
    success, fail, k = 0, 0, 0 
    items = []
    return BeautifulSoup(requests.get(url, headers = headers).text, 'html.parser')
    
def collect_from_soup(soup):
	for row in soup.select('div.srchResultListW > ul > li'): 
        k += 1
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
    ret = [items,success,fail]
    return ret
	
print(collect_from_soup(make_soup(my_name, my_university)))
