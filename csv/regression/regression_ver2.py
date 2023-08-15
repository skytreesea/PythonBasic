import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
path = r"C:\Users\user\Documents\지방공기업평가원_김창현\타당성검토\설립 타당성\타당성검토\대구농수축산물유통공사\보고서\모델\경제성_도주은\test\for_regression.csv"
df = pd.read_csv(path, encoding='cp949', thousands=',')

print(df.head()) 
print(df.columns) 
 
df['year'] = df['연도'].astype(int) - 2000
print(df['year'])
# Reshape the data into a 2-dimensional array.
ch = lambda value : np.reshape(df[value].tolist(), (-1, 1))

indep = 'year'

ys =  ['농산물 물량(kg/인)', '농산물 금액(원/인)',       '수산물 물량(kg/인)', '수산물 금액(원/인)', '농산물 물량(kg/인).1', '농산물 금액(원/인).1',      '수산물 물량(kg/인).1', '수산물 금액(원/인).1']

def reg(x,y):
    model = LinearRegression()
    x = ch(x)
    y = ch(y)
#회귀분석
    model.fit(x,y)
# 0행과 1행 삭제
    r_squared = model.score(x, y)
    print(f"종속변수: {i}\n변동계수: {model.coef_[0][0]} 절편:{model.intercept_[0]}, r제곱: {r_squared}")
    
for i in ys:
    reg(indep, i)
    
 