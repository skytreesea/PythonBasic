import pandas as pd
import matplotlib.pyplot as plt
path = r"C:\Users\skytr\Documents\GitHub\PythonBasic\csv\apt_2308.csv"
df = pd.read_csv(path, thousands=',')
r = lambda  x : x.astype(int)
df.drop(df.columns[[1, 2, 3]], axis=1, inplace=True)
#print(df[df['단지명'].str.contains('봉천우성')].iloc[:,:7])
#시군구 포함
sigungu = "관악"
#최대면적 및 최소면적
up_scale = 90
down_scale = 65
#오름차순 True
asc = True
# 보고싶은 숫자
show_number = 20
print(df[(df['시군구'].str.contains(sigungu))&(df['전용면적(㎡)'] > down_scale) & (df['전용면적(㎡)'] < up_scale) ].iloc[:,:7][-show_number:].sort_values(by = r"거래금액(만원)", ascending= asc))

# 0행과 1행 삭제
# df = df.drop([0, 1])
# 람다를 활용하여 정수로 바로 바꾸기   

 