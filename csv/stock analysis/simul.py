import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, re
from sklearn.linear_model import LinearRegression
 
p_rate = lambda former, latter: (latter-former)*100/ former
r = lambda  x : x.astype(float)
ro = lambda  x : round(x,4)
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
    df['Prev_diff'] = df['diff'].shift(1) 
    df['Prev_Volume'] = df['Volume'].shift(1) 
    df['ror_day'] = (df['Open']-df['Prev_Close'])*100/df['Prev_Close'] # 전날 종가 대비 다음날 시가 수익률
    # 칼럼명 각각 지정 성공 
    df.columns = ['Date']+[col + "_"+name_of_stock_csv[:-4] for col in df.columns if col != "Date"]
    return df

df = pd.read_csv(r"C:\Users\skytr\OneDrive\문서\PythonBasic\csv\stock analysis\total\total0819.csv")
df = df.drop(0)
test_df = df.loc[:10, ('Date','Open_TQQQ','Close_TQQQ','Prev_ror_SOXL')]

# 1000달러 있음
init_money = 1000
buying_criteria = 23
total_stock = 0
total_money_to_buy = 0
stock_name = 'SOXL'
sample_df = df.loc[:,'Open_' + stock_name]
k = 0 
print(sample_df)
print(f'{stock_name} 매매시작')
for open_price in sample_df: 
    # 구매조건 
    unit = 10
    money_to_buy = open_price * unit
    if (open_price < buying_criteria) and (init_money > money_to_buy):
        init_money = init_money - money_to_buy 
        k += 1
        total_money_to_buy += money_to_buy
        print(f'산 가격: {ro(open_price)}  가격 구매수량 {unit} = {ro(money_to_buy)}, 남은 돈 {ro(init_money)} ')
        
present_value = df.iloc[-1]['Open_' + stock_name]
last_date = df.iloc[-1]['Date']
if total_money_to_buy > 0:
    #df.sort_values(by='Date', ascending = False).iloc[1,1] 
    print(f'잔금: {ro(init_money)}, 구매 주식량 {k* unit} 현재가 {ro(present_value*k* unit)} 달러, 매수가격 {ro(total_money_to_buy)}, 차익 {ro(present_value*k* unit-total_money_to_buy)}')    
    print(f'오늘날짜 {last_date}')
    print(f'현재 가격 {present_value} 달러 ')
    print(f'수익률 {ro(p_rate(total_money_to_buy, present_value*k* unit))}%')
else:
    print(f'could not buy a stock')
    print(f'오늘날짜 {last_date}')
    print(f'현재 가격 {present_value} 달러 ')
