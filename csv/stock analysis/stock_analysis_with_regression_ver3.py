import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
from sklearn.linear_model import LinearRegression
os.chdir(r"C:\Users\skytr\OneDrive\문서\PythonBasic\csv\stock analysis\stocks")
stocks = os.listdir()
print(stocks)
r = lambda  x : x.astype(float)
ro = lambda  x : round(x,2)
# Reshape the data into a 2-dimensional array.
ch = lambda value : np.reshape(df[value].tolist(), (-1, 1))
# major_index = ('Date', 'Prev_ror_x','ror_day_x','Prev_Close_x','Open_x','Close_x','rate_of_return_x')
def create_df(name_of_stock_csv):
    df = pd.read_csv(name_of_stock_csv)
    x = r(df['Open'])
    y = r(df['Close'])
    # 수익률 
    df['rate_of_return'] = (y - x)*100/x
    df['diff'] = y - x
    df['hl_diff'] = r(df['High']) - r(df['Low']) 
    df = df.sort_values(by='Date', ascending=True)
    # 전날의 종가
    df['Prev_Close'] = df['Close'].shift(1) 
    df['Prev_ror'] = df['rate_of_return'].shift(1) 
    df['ror_day'] = (df['Open']-df['Prev_Close'])*100/df['Prev_Close'] # 전날 종가 대비 다음날 시가 수익률
    # 칼럼명 각각 지정 성공 
    df.columns = ['Date']+[col + "_"+name_of_stock_csv[:-4] for col in df.columns if col != "Date"]
    return df

df = create_df(stocks[0]) 

for i in stocks[1:]:
    df = pd.merge(df,create_df(i), on="Date")
    
print(df.head())
# print(df.sort_values(by="rate_of_return", ascending=False))
# df.to_clipboard()
def reg(indep, dep):
    model = LinearRegression()
    x = ch(indep)
    y = ch(dep)
#회귀분석
    model.fit(x,y)
# 0행과 1행 삭제
    r_squared = model.score(x, y)
    if r_squared > .3:
        print(f"독립변수: {indep}\n종속변수: {dep}\n변동계수: {ro (model.coef_[0][0])} 절편:{ro (model.intercept_[0])}, r제곱: {ro (r_squared)}\n")
    
#plt.plot(df['ror_day_x'][-50:],df['rate_of_return_y'][:50], '*')  
#plt.xticks(rotation=45)
df = df.drop(0)
# plt.show()
# NVDA 전날 수익 3% 이상 났을 때 수익률
# print(df[(df['Prev_ror_NVDA'] > 3)].loc[:, ('Date','Prev_ror_NVDA','rate_of_return_NVDA','Prev_ror_SOXL','rate_of_return_SOXL','rate_of_return_TQQQ')][:20].sort_values(by='Prev_ror_NVDA', ascending=False))
indeps = ['Prev_ror_NVDA','Prev_ror_SOXL','Prev_ror_TQQQ']
for i in df.columns:
    for j in indeps:
        if i != j:
            try:    
                reg(j,i) 
            except:
                print(i)
        
# tot = len(df)
# num = len(df[df['rate_of_return_x']> 0 ])
# num_2 = len(df[(df['rate_of_return_x']> 2) & (df['Prev_ror_x']> 2) ])
# num_plusplus = len(df[(df['rate_of_return_x']> 2) & (df['Prev_ror_x']> 3)& (df['ror_day_x']> 0) ])

# num3 = len(df[df['rate_of_return_x']> 3 ])

# ynum_2 = len(df[(df['rate_of_return_y']> 2) & (df['Prev_ror_y']> 2) ])
# print(f'총거래: {len(df)}')  
# print(f'soxl + 확률: {round(num*100/tot,2)   }')  

# print(f'이틀 연속 soxl+2 + 확률: {round(num_2*100/tot,2)} 전날 2%이상 오르고 오늘 또 2%이상 오름')  

# print(f'soxl\n전날수익률3+종가수익률+/오늘 수익률+2 : {round(num_plusplus*100/num,2)} 위와 같음')  

