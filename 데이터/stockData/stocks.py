import pandas as pd

#soxl 주식의 가격 기본 정보 구하기
df = pd.read_csv(r"C:\Users\ERC\Documents\GitHub\PythonBasic\데이터\stockData\SOXL.csv")

# 앞 부분만 출력해보기 
print(df.head())
#기초통계량 구하기
print(df['Low'].describe())
