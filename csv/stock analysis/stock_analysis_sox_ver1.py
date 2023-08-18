import pandas as pd
import matplotlib.pyplot as plt
import os 
os.chdir(r"C:\Users\skytr\OneDrive\문서\PythonBasic\csv\stock analysis\stocks")
stocks = os.listdir()
print(stocks)
r = lambda  x : x.astype(float)
# major_index = ('Date', 'Prev_ror_x','ror_day_x','Prev_Close_x','Open_x','Close_x','rate_of_return_x')
def create_df(name_of_stock_csv):
    df = pd.read_csv(name_of_stock_csv)
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
    df.columns = ['Date']+[col + "_"+name_of_stock_csv[:-4] for col in df.columns if col != "Date"]
    return df

df = create_df(stocks[0]) 

for i in stocks[1:]:
    df = pd.merge(df,create_df(i), on="Date")
    
print(df.head())
# df = pd.merge(create_df('SOXL'), create_df('SOXS'), on="Date" )

# print(df.sort_values(by="rate_of_return", ascending=False))
df.to_clipboard()

#plt.plot(df['ror_day_x'][-50:],df['rate_of_return_y'][:50], '*')  
#plt.xticks(rotation=45)

# plt.show()
# 전날 수익 3% 이상 나고, 시가-종가 수익률 0보다 클때
# print(df[(df['Prev_ror_x'] > 3) &(df['ror_day_x'] > 0)].sort_values(by='rate_of_return_x', ascending=False).loc[:, major_index][:10])
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
