import os
import pandas as pd
import numpy as np
from pandas.core.algorithms import value_counts
os.chdir(r'C:\Users\user\Documents\지방공기업평가원_김창현\연구\신규투자 타당성검토 지침 개발\결론작성을 위한')
df = pd.read_csv('inv_total.csv',encoding='cp949')
# os.chdir(r'C:\Users\user\Documents\지방공기업평가원_김창현\연구\신규투자 타당성검토 지침 개발\결론작성을 위한\result')  

#피봇테이블(파일출력)
#pd.pivot_table(df,index='계약년도',values=['B/C','PI'],aggfunc=np.mean).to_csv('피봇예시.csv',encoding='cp949')

#범주형 크로스테이블(파일출력)
#pd.crosstab(df['분류코드'], df['계약년도']).to_csv('크로스테이블.csv',encoding='cp949')

# 특정조건에서 특정행 호출(임대주택(b2)시 과제명)
# print(len(df[df['기존종합판단']!=df['종합판단(안)']]))

#df 조건에 맞게 칼럼 추가하는 방법
df['기존통과여부'] = np.where((df['판단']=="미흡") | (df['판단']=="다소 미흡")| (df['판단']=="매우 미흡"), '미통과', '통과')
df['신규통과여부'] = np.where((df['신규']=="미흡") | (df['신규']=="다소 미흡"), '미통과', '통과')
df['최종판단일치여부'] = np.where(df['기존통과여부']== df['신규통과여부'], '일치', '불일치')
# 특정 칼럼의 빈도분석
# print(df['판단'].value_counts())
print(df['최종판단일치여부'].value_counts())
os.chdir(r'C:\Users\user\Documents\지방공기업평가원_김창현\연구\신규투자 타당성검토 지침 개발\결론작성을 위한\csv_result')
df.to_csv('new_inv_result2.csv',encoding='cp949')

#  임대주택인 경우
#df_rent=df[df['분류코드'] =='b2']
#print(df_rent['기존통과여부'].value_counts())
#print(df_rent['신규통과여부'].value_counts())

# 임대주택: 최종판단 서로 다른 경우
#print(df['기존통과여부'][df['기존통과여부']!=df['신규통과여부']])
os.chdir(r'C:\Users\user\Documents\지방공기업평가원_김창현\연구\신규투자 타당성검토 지침 개발\결론작성을 위한\table_results')
# 연도별 B/C PI
#pd.pivot_table(df,index='계약년도',values=['B/C','PI'],aggfunc=np.mean).to_csv('연도별 BC PI.csv',encoding='cp949')

#  df3는 분류코드별 B/C PI
#pd.pivot_table(df,index='분류코드',values=['B/C','PI'],aggfunc=np.mean)
#크로스테이블 지역별 분류코드
#pd.crosstab(df['지역'], df['기존통과여부']).to_csv('지역별 기존통과여부.csv',encoding='cp949')
#피봇 지역별 분류코드
#pd.pivot_table(df,index='계약년도',values=['판단'],aggfunc=np.sum).to_csv('계약연도별 판단.csv',encoding='cp949')
# 
# 지역코드 별 통과여부
# df2 = pd.crosstab(df['지역코드'], df['기존통과여부'])
# df2['수행건수'] = df2['통과']+df2['미통과']
# df2['기각률'] = df2['미통과']/df2['수행건수']
#데이터 열 방향으로 합치기 ,axis =1 없으면 행 방향으로 합침
# df2 = pd.concat([df2, df3], axis=1)
#  df2.to_csv('지역코드 기존통과여부 BC PI 통합.csv',encoding='cp949') 

# 임대주택
# df_rent = df[df['분류코드']=='b2']
# # 연도별 통과여부BC PI 통합
# df_year_value= pd.pivot_table(df,index='분류코드',values=['B/C','PI'],aggfunc=np.mean) 
# df_year = pd.crosstab(df['분류코드'], df['기존통과여부'])
# df_year['수행건수'] = df_year['통과']+df_year['미통과']
# df_year['기각률'] = df_year['미통과']/df_year['수행건수']
# df_year= pd.concat([df_year, df_year_value], axis=1)
# df_year.to_csv('분류코드별 기존통과여부 BC PI.csv',encoding='cp949') 

import matplotlib.pyplot as plt
#B/C 히스토그램
# x= df['B/C']
# y= df['PI']
# plt.hist(df['PI'], bins=20, density=True, histtype='step')
# plt.hist(x, bins=20, density=True, alpha=0.7, histtype='stepfilled')
# plt.hist(df['정책성score'], bins=20, density=True, alpha=0.7, histtype='stepfilled')
# plt.show()
# plt.hist(y, bins=20, density=True, alpha=0.7, histtype='stepfilled')
# plt.show()
#산점도 
# np.random.seed(11)    # Reproducible random state
# N = len(x)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# print(df_rent['최종판단일치여부'].value_counts())
#df_rent[df_rent['최종판단일치여부'] == '불일치'].loc[:,['계약년도','과제명','B/C','PI','판단','신규','최종판단일치여부']].to_csv('임대주택 최종판단_다른경우.csv',encoding='cp949')
# 임대주택 제외
# df[df['최종판단일치여부'] == '불일치'].loc[:,['계약년도','과제명','B/C','PI','판단','신규','최종판단일치여부']].to_csv('종합 최종판단_다른경우.csv',encoding='cp949')
# # 계약년도
# df_detail = pd.crosstab(df['계약년도'], df['최종판단일치여부']) 
# df_detail['합']= df_detail['불일치'] + df_detail['일치']
# df_detail['불일치비율']= df_detail['불일치'] / df_detail['합'] 
# df_detail.to_csv('계약년도 최종판단 불일치건수.csv',encoding='cp949')
# df_rent[df_rent['기존통과여부'] == '미통과'].loc[:,['계약년도','과제명','B/C','PI','판단','신규','최종판단일치여부']].to_csv('임대 미통과사업.csv',encoding='cp949')
# 계약년도
# # 분류코드 최종불일치 
# df_final['합']= df_final['불일치'] + df_final['일치']
# df_final['불일치비율']= df_final['불일치'] / df_final['합']
# df_final.to_clipboard()
# # 신규 기존 판단결과
# dfp = df['B/Cscore'].value_counts()
# dff = df['Piscore'].value_counts()
dfb= df['판단일치여부'][df['계약년도']=='b2']
#dfc = df['최종판단일치여부'][df['분류코드']=='b2'].value_counts()

# pd.concat([dfp, dff,dfc], axis=1).to_clipboard()
# 정책성

df_gen = df[df['분류코드'] !='b2']
pd.crosstab(df_gen['계약년도'], df_gen['최종판단일치여부']).to_clipboard()




