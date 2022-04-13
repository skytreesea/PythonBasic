# 당선인 정보 불러와서 분석
import requests,re 
import matplotlib  
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt  
from scipy import stats
df = pd.read_csv(r'C:\Users\user\Documents\PythonBasic\데이터\rc_grand.csv')

print( 
df[(df['공기업유형']=='기타공사')].groupby('수도권여부')['경상수지비율'].describe().transpose() 
)
df[(df['공기업유형']=='도시철도공사')].groupby('수도권여부')['영업수지비율'].describe().transpose().to_clipboard()

#일단 전체로 수행
def regression(cotype, sudo, depen, indepen):
    model = smf.ols(formula = depen+'~'+indepen, data = df[(df['공기업유형']==cotype)&(df['수도권여부']==sudo)])
    result = model.fit()
    print(cotype, sudo, depen, indepen, result.summary())

cotypeList = ['상수도','하수도','도시개발공사','공영개발','기타공사','도시철도공사','도시개발공사']
# 유형에서 지방공단은 제외 
sudoList = ['수도권', '비수도권']
depenList = '부채비율'
indepenList = ['영업수지비율','경상수지비율']

for co in cotypeList:
    for su in sudoList:
        for inde in indepenList:
            regression(co, su,inde,'부채비율')