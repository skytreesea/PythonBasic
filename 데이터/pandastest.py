import pandas as pd



# csv 파일 곧바로 판다스 객체로 만듦 
df = pd.read_csv(r"C:\Users\skytr\Documents\GitHub\do-it-python\04\popSeoul.csv", thousands=',') #인코딩 안될 때 'cp949', 'utf8'

#head
print(df.head())

# 서울시 구별 인구 한국인, 외국인, 노인 
print(df.mean())