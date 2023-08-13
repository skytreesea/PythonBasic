import pandas as pd
import matplotlib.pyplot as plt
path = r"C:\Users\skytr\OneDrive\문서\PythonBasic\csv\nanet\20230730_experts.csv"
df = pd.read_csv(path, encoding='cp949')
# 0행과 1행 삭제
# df = df.drop([0, 1])
# 람다를 활용하여 정수로 바로 바꾸기 
r = lambda  x : x.astype(int)
print(df.head())
print(df[['pub_year', 'name', 'organization', 'degree','title']]) 

 