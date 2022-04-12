# 출처 https://www.data.go.kr/data/15058242/openapi.do
import requests,re 
import matplotlib  
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
# 폰트 안 깨지게 
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False
# url_info  = 'https://apis.data.go.kr/9760000/CommonCodeService/getCommonSgCodeList?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=100' 
df2 = pd.read_csv(r'C:\Users\user\Documents\지방공기업평가원_김창현\연구\파이썬을 활용한 연구개발\데이터\당선인\sgtype.csv', engine='python' )

dfs=[]
for i in range(500):
    try:
        url = 'https://apis.data.go.kr/9760000/WinnerInfoInqireService2/getWinnerInfoInqire?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=500&sgId='+str(df2['날짜'][i])+'&sgTypecode='+str(df2['코드'][i])
        soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
        total = []
        total.append([])
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('jdName'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('sdname'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('sggname'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('name'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('job'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('age'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('birthday'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('edu'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('career1'.lower())])  
        total.append([re.sub('\\n','',i.text) for i in soup.find_all('dugyul'.lower())])  
        df = pd.DataFrame(total).transpose()
        df['선거명'] = str(df2['이름'][i])
        df['날짜'] = str(df2['날짜'][i])
        dfs.append(df)
    except:
        pass

print(dfs[0])
df2 = dfs[0]
t = 1
while t < len(dfs):
    df2 = pd.merge(df2,dfs[t], how ='outer')
    t += 1
df2.columns=['0',"정당",'시도명', '시군구',"이름", "직업",'나이','생일','교육','커리어','득표율','선거명','날짜']
del[df2['0']]
df2.to_csv(r'C:\Users\user\Documents\지방공기업평가원_김창현\연구\파이썬을 활용한 연구개발\데이터\당선인\\역대선거 당선자_total.csv', encoding='utf-8-sig')
