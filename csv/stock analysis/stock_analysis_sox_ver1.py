import pandas as pd
import matplotlib.pyplot as plt

r = lambda  x : x.astype(int)

def create_df(name_of_stock):
    df = pd.read_csv(r"C:\Users\user\Downloads\\" + name_of_stock+".csv")
    x = r(df['Open'])
    y = r(df['Close'])
    df['rate_of_return'] = (y - x)/x
    return df
    

df = pd.merge(create_df('soxl'), create_df('soxs'), on="Date" )


print("최근 1년간 가장  soxl의 수익률이 좋았던 5일")
print(df.sort_values(by='rate_of_return_x', ascending=False).iloc[:10,:6])

print("최근 1년간 가장  soxs의 수익률이 좋았던 일")
print(df.sort_values(by='rate_of_return_y', ascending=False).iloc[:10,6:])
 
# print(df.sort_values(by="rate_of_return", ascending=False))

