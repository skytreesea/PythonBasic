import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\skytr\Downloads\주민등록인구_20230806115221.csv")
# 0행과 1행 삭제
df = df.drop([0, 1])
# 람다를 활용하여 정수로 바로 바꾸기 
r = lambda  x : x.astype(int)

#print((df['2023 1/4'].astype(int) / df['2023 1/4.1'].astype(int)).mean())
#print(df.columns)
#x1 = r(df['2023 1/4'])
#x2 = r(df['2023 1/4.2'])
#print( x1 - x2)
#plt.plot(x1, x2, 'ob')
#plt.show()

myfile = r"C:\Users\skytr\Downloads\SOXL.csv"
df = pd.read_csv(myfile)
print(df.head())
print(df.columns)
x = r(df['Open'])
y = r(df['Close'])

z = (y - x)/x
print("수익률 +", len(df[z > 0]) )
print("수익률 -",len(df[z <= 0]) ) 
print("### 수익률 + 일 때 ") 
print( df[z > 0].describe())
print("### 수익률 - 일 때 ") 
print( df[z <= 0].describe())



