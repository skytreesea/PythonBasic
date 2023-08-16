import pandas as pd
import matplotlib.pyplot as plt

r = lambda  x : x.astype(float)
major_index = ('Date', 'Prev_ror_x','ror_day_x','Prev_Close_x','Open_x','Close_x','rate_of_return_x')
def create_df(name_of_stock):
    df = pd.read_csv(r"C:\Users\skytr\OneDrive\문서\PythonBasic\csv\stock analysis\\" + name_of_stock+".csv")
    x = r(df['Open'])
    y = r(df['Close'])
    df['rate_of_return'] = (y - x)*100/x
    df['diff'] = y - x
    df['hl_diff'] = r(df['High']) - r(df['Low']) 
    df = df.sort_values(by='Date', ascending=True)
    # 전날의 종가
    df['Prev_Close'] = df['Close'].shift(1) 
    df['Prev_ror'] = df['rate_of_return'].shift(1) 
    df['ror_day'] = (df['Open']-df['Prev_Close'])*100/df['Prev_Close'] # 전날 종가 대비 다음날 시가 수익률
    return df

df = pd.merge(create_df('SOXL'), create_df('SOXS'), on="Date" )


# print(df.sort_values(by="rate_of_return", ascending=False))
print(df.columns)
 

plt.plot(df['ror_day_x'][-50:],df['rate_of_return_y'][:50], '*')  
plt.xticks(rotation=45)

# plt.show()
# 전날 수익 3% 이상 나고, 시가-종가 수익률 0보다 클때
print(df[(df['Prev_ror_x'] > 3) &(df['ror_day_x'] > 0)].sort_values(by='rate_of_return_x', ascending=False).loc[:, major_index][:10])
tot = len(df)
num = len(df[df['rate_of_return_x']> 0 ])
num_2 = len(df[(df['rate_of_return_x']> 2) & (df['Prev_ror_x']> 2) ])
num_plusplus = len(df[(df['rate_of_return_x']> 2) & (df['Prev_ror_x']> 3)& (df['ror_day_x']> 0) ])
num_plusminus = len(df[(df['rate_of_return_x']> 2) & (df['Prev_ror_x']> 3)& (df['ror_day_x']< 0) ])
num_minusplus = len(df[(df['rate_of_return_x']> 2) & (df['Prev_ror_x']< 3)& (df['ror_day_x']> 0) ])
num_minusminus = len(df[(df['rate_of_return_x']> 2) & (df['Prev_ror_x']< 3)& (df['ror_day_x']> 0) ])
num3 = len(df[df['rate_of_return_x']> 3 ])
num5 = len(df[df['rate_of_return_x']> 5 ])
ynum = len(df[df['rate_of_return_y']> 0 ])
ynum3 = len(df[df['rate_of_return_y']> 3 ])
ynum5 = len(df[df['rate_of_return_y']> 5 ])
ynum_2 = len(df[(df['rate_of_return_y']> 2) & (df['Prev_ror_y']> 2) ])
print(f'총거래: {len(df)}')  
print(f'soxl + 확률: {round(num*100/tot,2)   }')  
print(f'soxl +3% 확률: {round(num3*100/tot,2)}')  
print(f'soxl +5% 확률: {round(num5*100/tot,2)}')  
print(f'soxs + 확률: {round(ynum*100/tot,2)}')  
print(f'soxs +3% 확률: {round(ynum3*100/tot,2)}')  
print(f'soxs +5% 확률: {round(ynum5*100/tot,2)}')  
print(f'이틀 연속 soxl+2 + 확률: {round(num_2*100/tot,2)} 전날 2%이상 오르고 오늘 또 2%이상 오름')  
print(f'이틀 연속 soxs+2 + 확률: {round(ynum_2*100/tot,2)} 위와 같음')  
print(f'soxl\n전날수익률3+종가수익률+/오늘 수익률+2 : {round(num_plusplus*100/num,2)} 위와 같음')  
print(f'전날수익률3+종가수익률-/오늘 수익률+2 : {round(num_plusminus*100/num,2)} 위와 같음')  
print(f'전날수익률3-종가수익률+/오늘 수익률+2 : {round(num_minusplus*100/num,2)} 위와 같음')  
print(f'전날수익률3-종가수익률-/오늘 수익률+2 : {round(num_plusplus*100/num,2)} 위와 같음')  
