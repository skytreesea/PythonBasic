# 출처 https://www.data.go.kr/data/15058242/openapi.do
import requests,re 
import matplotlib  
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
# 폰트 안 깨지게 
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False
url_info  = 'https://apis.data.go.kr/9760000/CommonCodeService/getCommonSgCodeList?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=100' 

soup = BeautifulSoup(requests.get(url_info, verify = False).text,'lxml')
total = []
total.append([re.sub('\\n','',i.text) for i in soup.find_all('sgVotedate'.lower())])  
total.append([re.sub('\\n','',i.text) for i in soup.find_all('sgname'.lower())])  
total.append([re.sub('\\n','',i.text) for i in soup.find_all('sgtypecode'.lower())])  
df = pd.DataFrame(total).transpose()
df.columns=["날짜", "이름", "코드"]
df.to_clipboard()