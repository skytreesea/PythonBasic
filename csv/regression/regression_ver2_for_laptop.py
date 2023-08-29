import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
path = r"C:\Users\ERC\Documents\GitHub\PythonBasic\csv\regression\for_regression.csv"
df = pd.read_csv(path, encoding='cp949', thousands=',')

print(df.head()) 
print(df.columns) 
 
df['year'] = df['연도'].astype(int) - 2000
# Reshape the data into a 2-dimensional array.
ch = lambda value : np.reshape(df[value].tolist(), (-1, 1))

indep = 'year'

def reg(x,y):
    model = LinearRegression()
    x = ch(x)
    y = ch(y)
    try:
    #회귀분석
        model.fit(x,y)
    # 0행과 1행 삭제
        r_squared = model.score(x, y)
        print(f"종속변수: {i}\n변동계수: {model.coef_[0][0]} 절편:{model.intercept_[0]}, r제곱: {r_squared}\n")
    except:
        print(f'{y}변수는 분석하지 못했습니다.')
    
for i in df.columns:
    reg(indep, i)
    
 