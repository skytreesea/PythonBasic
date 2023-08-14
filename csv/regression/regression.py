import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
path = r"C:\Users\user\Documents\지방공기업평가원_김창현\타당성검토\설립 타당성\타당성검토\대구농수축산물유통공사\보고서\모델\경제성_도주은\test\for_regression.csv"
df = pd.read_csv(path, encoding='cp949')

model = LinearRegression()
print(df.head()) 
print(df.columns) 
 
# Reshape the data into a 2-dimensional array.
ch = lambda value : np.reshape(df[value].tolist(), (-1, 1))

indep = '연도'
dep = '수산물 물량(톤)'
x= ch(indep)
y = ch(dep)

#회귀분석
model.fit(x,y)

# 0행과 1행 삭제
r_squared = model.score(x, y)

print(f"독립변수: {indep} 종속변수: {dep}\n변동계수: {model.coef_[0][0]} 절편:{model.intercept_[0]}, r제곱: {r_squared}")