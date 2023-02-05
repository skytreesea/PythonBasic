from bs4 import BeautifulSoup 
import requests, re

# Riss를 get 방식으로 데이터를 넣은 다음 출력값에서 원하는 데이터를 추출
url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EB%B6%88%EC%95%88%EC%9E%A5%EC%95%A0&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=re_a_kor&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=&isFDetailSearch=&sflag=1&searchQuery=%EB%B6%88%EC%95%88%EC%9E%A5%EC%95%A0&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn='

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
total = []

for i in soup.find_all('div',{'class':'cont'}):
    new = [i.find('p',{'class':'title'}).text, i.find('p',{'class':'etc'}).text]
    total.append(new)
# control-v를 하면 어디서든 붙여넣을 수 있도록 클립보드로 저장됨
import pandas 
df = pandas.DataFrame(total)
df.to_clipboard()
