# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests,re
#네이버 기사 url만 바꾸기: 따옴표 안에 url을 붙여넣으세요.
productName = '홈트'

basic = 'https://search.shopping.naver.com'
url = 'https://search.shopping.naver.com/search/all?query={}'.format(productName)

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
a=[]
import pandas as pd
#상품명
#상품명만 따로 크롤링(연습) basicList_title__3P9Q7
product = soup.find_all('div',{'class':'basicList_title__3P9Q7'})
print(product.find('a').get('title'))
# for i in product:
#     print(i.find('a'))

# 각 상품정보에서 특정 정보를 리스트 형태로 모으기(데이터프레임 용)
# for i in soup.find_all('li',{'class':'search-product'}):
#     try:
#         k=[i.find('div',{'class':'name'}).text,
#         i.find('strong',{'class':'price-value'}).text,
#         i.find('span',{'class':'star'}).text,
#         i.find('span',{'class':'rating-total-count'}).text[1:-1],
#         basic + i.find('a').get('href')]
#         info.append(k)
#     except:
#         pass 
# # 판다스 이용해 자료를 행열 전환하고, 바로 df로 만들어 클립보드에 저장, 칼럼명 처음에 지정해주기 
# df = pd.DataFrame(info, columns=['상품명','가격','리뷰평점','리뷰수','링크'])
# # 천의 자리 제거(가격)
# df['가격']=df['가격'].str.replace(',', '').astype('int64')
# # 가격 높은 순으로 클립보드 저장
# df.sort_values(by = '가격', ascending = False).to_clipboard()
# # 파일로 저장
# df.sort_values(by = '가격', ascending = False).to_excel(productName+'.xlsx',encoding='cp949')
 