# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests, time
def bs(url):
    return BeautifulSoup(requests.get(url).text,'lxml')       
basicurl = 'https://www.sisain.co.kr/news/articleList.html?sc_section_code=S1N14'
soup = bs(basicurl)
# 각 단계별로 제대로 작동하는지 살펴본다. 
# print(soup.find_all('div',{'id':'article-view-content-div'}))
total = []
# 만화가 모여있는 사이트 주소에서 각 링크를 얻어 total이라는 리스트로 저장
for i in soup.find_all('article',{'class':'items'}):
    total.append('https://www.sisain.co.kr'+i.find('a').get('href'))

# print(total)
# 각 만화가 있는 위치를 찾아 거기에 img item을 저장한다. .content
for item in total:
    # 오류가 생기면 실행되지 않도록 
    try:
        soup = bs(item)
        for i in soup.find_all('div',{'id':'article-view-content-div'}):
            with open(r'C:\Users\ERC\Pictures\Saved Pictures\\'+ item[-5:]+'.jpg','wb') as b:
                    # 파일을 열어 특정 파일을 jpg 형태로 저장한다
                    b.write(requests.get('https://www.sisain.co.kr'+i.find('img').get('src')).content)
    except:
        pass          
  