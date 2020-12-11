# 판다스 예제 업데이트 특정 조건의 서울시 아파트 가격 구하기 
import os
import pandas as pd
# 할 때마다 경로 바꿔주어야 함
os.chdir(r'E:\실거래가분석\data')
# 콤마 빼기 
df = pd.read_csv('sales_20201212024316.csv', encoding ='cp949', thousands = ',')
# 일단 df를 제대로 추출했는지 확인 필요 
#print(df.head())
# 주요 아파트 정보 입력: 기초통계량(평균, 최대, 최소)
month = 202011
name_apt = '푸르지오'
area_limit = 60
sigungu = '봉천'
# 간단한 버젼
print(df.loc[:,('거래금액(만원)','전용면적(㎡)')][(df['시군구'].str.find(sigungu) > -1 ) ].describe())
# 특정 시점, 특정 단지명 포함, 기초통계량, 단지명
#print(month, name_apt, area_limit,'이하 아파트 매매 ')
#print(df.loc[:,('단지명','계약년월','거래금액(만원)','전용면적(㎡)')][(df['계약년월'] == month) & (df['단지명'].str.find(name_apt) > -1 ) & (df['전용면적(㎡)'] < area_limit )].describe())
print(month, sigungu,name_apt,  '아파트 매매 ')
# 특정 시점(2020년), 특정 단지명 포함(대치동), 단지명, 기초통계량
print(df.loc[:,('단지명','계약년월','거래금액(만원)','전용면적(㎡)')][(df['계약년월'] == month) & (df['단지명'].str.find(name_apt) > -1 ) & (df['시군구'].str.find(sigungu) > -1 ) ])
# csv로 출력하기
df.loc[:,('단지명','계약년월','거래금액(만원)','전용면적(㎡)')][(df['계약년월'] == month) & (df['단지명'].str.find(name_apt) > -1 ) & (df['시군구'].str.find(sigungu) > -1 ) ].to_csv(name_apt + 'apt_sales.csv',encoding='cp949')
