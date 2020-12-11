# 판다스 예제 업데이트 
import os
import pandas as pd
# 할 때마다 경로 바꿔주어야 함
os.chdir(r'E:\실거래가분석\data')
# 콤마 빼기 
df = pd.read_csv('sales_20201212024316.csv', encoding ='cp949', thousands = ',')
# 일단 df를 제대로 추출했는지 확인 필요 
#print(df.head())
# 관악구 전용면적 120㎡ 이상 아파트의 기초통계량(평균, 최대, 최소)
# print(df.loc[:,'거래금액(만원)'][(df['전용면적(㎡)'] > 120) | (df['시군구'].str.find('관악') > -1 )].describe() )
place ='봉천'
month = 202011
name_apt = '봉천우성'
area_limit = 60
# 특정 시점(202011), 특정 단지명 포함(봉천우성), 기초통계량
print(month, name_apt, area_limit,'이하 아파트 매매 ')
print(df.loc[:,('단지명','거래금액(만원)','전용면적(㎡)')][(df['계약년월'] == month) | (df['단지명'].str.find(name_apt) > -1 ) | (df['전용면적(㎡)'] < area_limit )].describe() )



