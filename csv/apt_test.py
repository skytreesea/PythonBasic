import pandas as pd
df = pd.read_csv(r'C:\Users\user\Documents\PythonBasic\apt_23007.csv', encoding='cp949')

df[(df['단지명'].str.contains('봉천우성') == True)].mean()

df[(df['시군구'].str.contains('강남구') == True) and (df[r'전용면적(㎡)'] >  50)].groupby(r'전용면적(㎡)').mean()