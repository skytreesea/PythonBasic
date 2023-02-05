# 출처 https://www.data.go.kr/data/15058242/openapi.do
import requests,re 
import matplotlib  
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup

years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

dfs = []
for year in years:
    url = 'https://www.cleaneye.go.kr/user/openXmlMajorMngIdx.do?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=300&ac_year=' + year +'&type=xml&SG_APIM=2ug8Dm9qNBfD32JLZGPN64f3EoTlkpD8kSOHWfXpyrY'
    soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
    total  = []
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('AC_YEAR'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ENT_NAME'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_AN_YUD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_AN_JAD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_AN_BUD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_SI_MED'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_SI_JAD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_HWA_JAD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_HWA_CHJD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_HWA_CHHD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_HWA_JAHD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_SU_CHD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_SU_GYUNGD'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_SU_YUD'.lower())])  
    df = pd.DataFrame(total).transpose()
    df.columns=["조회연도", "기업명", '안정성유동비율', '자기자본구성비율','부채비율','매출액순이익율','자기자본순이익율','매출액영업이익율','총자산순이익율','총자산회전율','자기자본회전율','총수지비율','경상수지비율','영업수지비율']
    dfs.append(df)

df2 = dfs[0]
t = 1
while t < len(years):
    df2 = pd.merge(df2,dfs[t], how ='outer')
    t += 1

dfs = []
for year in years:
    url = 'https://www.cleaneye.go.kr/user/openXmlMngResult.do?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=500&ac_year='+year+'&type=xml&SG_APIM=2ug8Dm9qNBfD32JLZGPN64f3EoTlkpD8kSOHWfXpyrY'
    soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
    total  = []
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('AC_YEAR'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ENT_NAME'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_YI'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_YO'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_profit'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_YYI'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_YYO'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('IN_BEFORE_TAX'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_BS'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('NET_INCOME'.lower())])  
    df = pd.DataFrame(total).transpose()
    df.columns=["조회연도", "기업명", "영업수익", "영업비용",'영업이익','영업외수익','영업외비용','법인세차감전이익','법인세등','당기순이익' ]
    dfs.append(df)

df3 = dfs[0]
t = 1
while t < len(years):
    df3 = pd.merge(df3,dfs[t], how ='outer')
    t += 1

df4 = pd.read_csv(r'C:\Users\ERC\Documents\GitHub\PythonBasic\데이터\basic erc.csv', encoding = 'cp949')

df_total = pd.merge(df2, df3)
pd.merge(df_total, df4).to_clipboard()
