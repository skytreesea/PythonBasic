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
    print(f"독립변수: {indep} ***종속변수: {dep}***\n변동계수: {round(model.coef_[0][0],2)} 절편:{round(model.intercept_[0],2)}, r제곱: {round(r_squared,2)}")
    
variables = [ '농산물 물량(톤)', '농산물 금액(억원)', '수산물 물량(톤)',
       '수산물 금액(억원)', '대구', '영남권', '농산물 물량(kg/인)', '농산물 금액(원/인)',
       '수산물 물량(kg/인)', '수산물 금액(원/인)', '농산물 물량(kg/인)_1', '농산물 금액(원/인)_2',
       '수산물 물량(kg/인)_3', '수산물 금액(원/인)_4']
for i in variables:
    regression('연도', i)