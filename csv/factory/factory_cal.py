import pandas as pd
import matplotlib.pyplot as plt
import usecsv
from scipy import stats
df = pd.read_csv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장장_프로젝트_2023\raw\merged_v2.csv', thousands=',')
base_url = r"C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장장_프로젝트_2023\factory_test\test_201801_202308"
df['대지면적당거래금액'] = df['거래금액(만원)']/df[ '대지면적(㎡)']
df['연면적당거래금액'] = df['거래금액(만원)']/df[ '전용/연면적(㎡)']
df['용적률'] = df['전용/연면적(㎡)']/df[ '대지면적(㎡)']
 
major_value = ['건축물주용도',  '계약년월','도로조건','용도지역','연도', '시군구_통합']
# 지역 리스트
cities = [
    "서울", "부산광역시", "대구광역시", "인천광역시", "광주광역시",
    "대전광역시", "울산광역시", "세종", "경기도", "강원",
    "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주"
]

df['연도'] = df['계약년월'].astype(str).str[:4]
# '시군구_통합' 열 생성
def get_city(value):
    for city in cities:
        if city in value:
            return city
    return value  # 만약 일치하는 값이 없을 경우 원래 값 반환

df['시군구_통합'] = df['시군구'].apply(get_city)
for i in major_value:
    result = df.groupby(by=i).agg({
        '거래금액(만원)': 'mean',
        '연면적당거래금액': 'mean',
        '대지면적당거래금액': 'mean', 
        '시군구': 'count'
    })
    result.to_csv(base_url + r'\평균 및 거래량_'+i+'.csv', encoding='utf-8-sig')
 
df.to_csv(base_url + r'\total_factory.csv', encoding = 'utf=8-sig')
df.describe().to_csv(base_url + r'\전체_describe.csv', encoding = 'utf=8-sig')
 # 전체 상위 5개 출력
df2 = df.sort_values(by = '대지면적당거래금액', ascending = False).loc[:5,('시군구_통합','도로조건','건축물주용도','용도지역','전용/연면적(㎡)', '대지면적(㎡)', '거래금액(만원)', '대지면적당거래금액','용적률')]
# 상위 5개 제외
df3 = df.sort_values(by = '대지면적당거래금액', ascending = False).loc[5:,('시군구_통합','도로조건','건축물주용도','용도지역','전용/연면적(㎡)', '대지면적(㎡)', '거래금액(만원)', '대지면적당거래금액','용적률')]
depen = ['대지면적당거래금액','연면적당거래금액','거래금액(만원)']
for i in depen:
    for j in major_value[:-1]:
        result = df.pivot_table(values= i, index='시군구_통합', columns=j, aggfunc='mean')
        result.to_csv(base_url + r'\시군구_통합_'+j+i+ '.csv', encoding = 'utf=8-sig')
        result = df.pivot_table(values=  i, index='시군구_통합', columns=j, aggfunc='count')
        result.to_csv(base_url + r'\시군구_통합_'+j+i+'(거래량).csv', encoding = 'utf=8-sig')

#기초자료 
df['계약년월'].value_counts().to_csv(base_url + r'\계약년월.csv', encoding = 'utf=8-sig')
df['연도'].value_counts().to_csv(base_url + r'\연도.csv', encoding = 'utf=8-sig')
import pandas as pd
import statsmodels.api as sm

def regression(df):
    for i in depen:
        # '시군구_통합', '건축물주용도', '용도지역' 범주형 변수들을 dummy 변수로 변환
        df_dummies = pd.get_dummies(df[['시군구_통합','건축물주용도', '용도지역','도로조건']], drop_first=True) #True로 하면 최빈값이 없어지면서 y절편으로 들어감 
        # 변환된 dummy 변수와 연면적당거래금액을 새로운 데이터프레임으로 합침
        df_model = pd.concat([df[i], df_dummies], axis=1)
        # 독립변수와 종속변수 설정
        X = df_model.drop(i, axis=1)
        # bool로 되어 있을 경우 오류발생하므로 정수로 바꿔줌
        X = X.astype({col: 'int' for col in X.columns if X[col].dtype == 'bool'})
        y = df_model[i]
        # 절편(intercept) 추가
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        # OLS 회귀분석 모델 생성 및 학습
        print(f'{i} 종속변수')
        # 결과 출력
        print(model.summary())  
        
df_new = df[df['연도'].isin(['2020', '2021', '2022', '2023'])]
regression(df_new)

