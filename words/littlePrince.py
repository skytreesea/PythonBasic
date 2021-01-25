from konlpy.tag import *
from konlpy.corpus import kolaw
import re
kkma = Kkma()
hannanum = Hannanum()
ok = Okt()
# 어린왕자 스크립트 scripts로 크롤링
from bs4 import BeautifulSoup  
import requests,re
#네이버 기사 url만 바꾸기: 따옴표 안에 url을 붙여넣으세요. 원 글은 http://blog.daum.net/8pm/2 에서 발췌하였습니다. 
url = 'http://blog.daum.net/8pm/2'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
new_text = soup.find_all('td',{'id':'user_contents'})
scripts=''
for i in new_text:
    scripts += i.text  
#판다스로 수정
import pandas as pd
df = pd.DataFrame({'noun': hannanum.nouns(scripts)})
new = df['noun'].value_counts().sort_values(ascending=False)
# 가장 많이 쓰인 단어(2개 이상 어절로 된)
new  = new[:15]
print(new)
# import matplotlib.pyplot as plt
# # bar에 색깔 입히기 
# import seaborn as sns
# colors = sns.color_palette('hls',15) 
# # 폰트가 없어서 한글 깨지는 것을 막기 위해서 
# plt.rcParams['font.family'] = 'gulim'
# plt.barh(new.index, new.values, color = colors)
# plt.show()