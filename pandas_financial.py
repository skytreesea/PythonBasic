import pandas as pd
df = pd.read_excel(r'C:\Users\user\Documents\pythontest\지방공기업현황.xlsx')
to_firms=pd.crosstab(df['지역'],df['공기업유형'])
# sum()을 통해 '지역','공기업유형'별 합을 따로 구함 
regionSum =to_firms.transpose().sum()
typeSum =  to_firms.sum()
# 행에 있는 것(지역)부터 합치고 회전시켜서 공기업유형 더함 
new = pd.concat([to_firms, regionSum], axis=1 )
new = pd.concat([new.transpose(), typeSum], axis=1)
# 값을 클립보드로 복사함
#new.transpose().to_clipboard()
 
#경상수지비율 원자료 
df2 = pd.read_excel(r'C:\Users\user\Documents\pythontest\financial.xlsx')
#행열 뒤집음(항목 계산 쉽게 하기 위해)
df3 = df2.transpose()
df3 = df3.iloc[1:,:]
#각 연도별 항목 합 
df3['합'] = df2.sum()
df3['경상수지비율']=df3[0]*100/df3[1]
df3.columns =['수입','비용','인건비','운영비','경상수지','합' ]

#df3.to_clipboard()