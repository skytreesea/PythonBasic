from bs4 import BeautifulSoup 
import requests, re, json

# Riss를 get 방식으로 데이터를 넣은 다음 출력값에서 원하는 데이터를 추출
name = '김창현'
school = '서울대'
yearGraduate = '2009' 
 
 #학위논문
url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query='+ name +'&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=bib_t&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=1000'
#학술논문
url2 = 'http://www.riss.kr/search/Search.do?isDetailSearch=Y&searchGubun=true&viewYn=OP&strQuery=&queryText=&exQuery=&resultSearch=false&icate=re_a_kor&order=%2FDESC&strSort=RANK&pageScale=10&isTab=Y&sflag=1&fsearchMethod=searchDetail&isFDetailSearch=N&fsearchSort=&fsearchOrder=&resultKeyword=&pageNumber=1&colName=re_a_kor&field1=znTitle&keyword1=&op1=AND&field2=znCreator&keyword2='+name +'&op2=AND&field3=znSubject&keyword3=&op3=AND&field4=znPublisher&keyword4=&op4=AND&field5=znAbstract&keyword5=&p_year1=&p_year2=&language=&l_sub_code='

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

#get_pa
def papers(url):
    soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
    total = {}
#url로 하면 학위논문, url2로 하면 학술논문
    for i in soup.find_all('div',{'class':'cont ml60'}):
        new = [i.find('p',{'class':'title'}).text, i.find('p',{'class':'etc'}).text]
        if re.search(name, new[1]):
            total[new[1]] = new[0]
    return total
new  = papers(url) 
 
data = json.dumps(new).encode().decode('unicode_escape')

# json 파일로 저장, 웹으로 저장 서툴러서
with open(r"C:\Users\skytr\OneDrive\문서\김창현\책\파이썬 생활프로그래밍\testcode\web_paper.json", 'w', encoding="UTF-8") as file:
    json.dump(data, file, indent="\t", ensure_ascii=False) 
    