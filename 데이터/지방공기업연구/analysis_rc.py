# 당선인 정보 불러와서 분석
import requests,re 
import matplotlib  
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt  
from scipy import stats
df = pd.read_csv(r'C:\Users\ERC\Documents\GitHub\PythonBasic\데이터\지방공기업연구\rc_grand.csv')
total = []
#일단 전체로 수행
def regression(cotype, sudo, depen, indepen, year):
    model = smf.ols(formula = depen+'~'+indepen, data = df[(df['공기업유형']==cotype)&(df['수도권여부']==sudo)])
    result = model.fit()
    if result.pvalues[1] < .05:
        total.append(['*',cotype, sudo, depen, indepen, result.pvalues[1], result.params[1], result.rsquared])
    else:
        total.append([' ',cotype, sudo, depen, indepen, result.pvalues[1],result.params[1],result.rsquared])

cotypeList = ['상수도','하수도','도시개발공사','공영개발','기타공사','도시철도공사']
# 유형에서 지방공단은 제외 
sudoList = ['수도권', '비수도권']
depenList = ['영업수지비율','경상수지비율','당기순이익']
indepenList = ['부채비율']

# period = ['전체','2020','2011-2018']

for co in cotypeList:
    for su in sudoList:
        for inde in indepenList:
            for depen in depenList:
                regression(co, su,inde, depen,2020)

pd.DataFrame(total).to_clipboard()