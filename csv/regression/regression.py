import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
path = r"C:\Users\skytr\OneDrive\문서\PythonBasic\csv\regression\for_regression.csv" 
df = pd.read_csv(path, encoding='cp949')

print(df.head()) 
print(df.columns) 
 
def regression(indep, dep):
    # df 칼럼명만 입력하면 regression 
    # df를 np로 바꿔주는 핵심함수
    ch = lambda value : np.reshape(df[value].tolist(), (-1, 1))
    model = LinearRegression()
    x= ch(indep)
    y = ch(dep)
    #회귀분석
    model.fit(x,y)
    # 0행과 1행 삭제
    r_squared = model.score(x, y)
    # 결과값 출력
    print(f"독립변수: {indep} 종속변수: {dep}\n변동계수: {model.coef_[0][0]} 절편:{model.intercept_[0]}, r제곱: {r_squared}")
    
regression('연도', '농산물 물량(kg/인)_1')