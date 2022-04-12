# 당선인 정보 불러와서 분석
import requests,re 
import matplotlib  
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
df = pd.read_csv(r'C:\Users\ERC\Documents\김창현\데이터\당선자\당선자total.csv')
df.columns=['0',"정당",'시도명', '시군구',"이름", "직업",'나이','생일','교육','커리어','득표율','선거명','날짜']
df['이름코드'] = df['이름'] + df['생일'].astype(str)
df['선거코드'] = df['선거명'] + df['날짜'].astype(str)
# 이름 코드로 당선자 
print(df['날짜'].value_counts().to_clipboard())

# 특정 조건으로 검색
# print(df[
#     (df['선거명'].str.contains('국회의원')) &
#     (df['커리어'].str.contains('노무현')) 
#     ]
#     )
# 코드 바꿔가며 특정 
print( 
df[
    df['교육'].str.contains('서울대') 
    
    ] 
)

    # ['시도명'].value_counts()

df[
    (df['교육'].str.contains('연세대')) & 
    (df['선거명'].str.contains('국회의원'))
].to_clipboard()