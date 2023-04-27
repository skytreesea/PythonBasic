from bs4 import BeautifulSoup
import requests 

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

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
      
def get_papers(author):
    #author = schema.name
    #birth_year = schema.birth_year # 나중에 던져주세요(지금은 디폴트입니다)
    #gubun = schema.gubun #처음에는 구분에서 국내석사만 검색 --> 국내석사 정보 취득 후 국내박사 -->(추후) 외국박사까지
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=Y&searchGubun=true&viewYn=OP&sflag=1&fsearchMethod=searchDetail&isFDetailSearch=N&colName=re_a_kor&field1=znTitle&keyword1=&op1=AND&field2=znCreator&keyword2='+author+'&op2=AND&field3=znSubject&keyword3=&op3=AND&field4=znPublisher&keyword4=&op4=AND&field5=znAbstract&keyword5=&p_year1=&p_year2=&language=&l_sub_code='

    #연도 필더링 테스트
    success, fail= 0, 0
    items = []
    soup = BeautifulSoup(requests.get(url, headers = headers).text, 'html.parser')
    #학위논문
    
    for row in soup.select('div.srchResultListW > ul > li'):
        try:
            tmp_etcs = row.select("p.etc > span")
            name = row.select_one("span.writer").text
            year = int(tmp_etcs[2].text)
            title = row.select_one("p.title").text
            link = row.select_one("p.title > a").attrs["href"]
            gubun=tmp_etcs[3].text
            assigned=row.select_one("span.assigned").text
            #print(name, year, title, tmp_etcs[0], tmp_etcs[1], link)
            if author == name:
                print(name, year, title, assigned, gubun, link)
                
        
            #if name == author : name == author  and (year < (birth_year + 34)) and int(tmp_etcs[2].text) > (birthYear + 21) and tmp_etcs[2].text in year_test_list and tmp_etcs[2].text == year_test and re.search(authority, purify(row.select_one("span.assigned").text)) and tmp_etcs[3].text == gubun and (year > (birth_year + 21)) and (year < (birth_year + 34))
                #data = {}
                #data['title']=row.select_one("p.title").text
                    #author=name,
                    #university=row.select_one("span.assigned").text,
                    #norm_university=univ_names.convert_univ_name(row.select_one("span.assigned").text),
                    #year=tmp_etcs[2].text if len(tmp_etcs)>2 else None,
                    #gubun=tmp_etcs[3].text if len(tmp_etcs)>3 else None, #박사/석사 구분 HTML 추가 필요
                    #data['link']='http://www.riss.kr' + row.select_one("p.title > a").attrs["href"]
            
                #items.append(newData)
                #success += 1
        except:
            pass
            #fail += 1
    #return items
 
print(get_papers('김창현'))