import pandas as pd
import statsmodels.api as sm

df = pd.read_csv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장장_프로젝트_2023\factory_test\test_201801_202308\total_factory.csv', thousands=',')

depen = ['대지면적당거래금액','연면적당거래금액','거래금액(만원)']
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
        
df_new = df[df['연도'].isin([2021, 2022, 2023])]
regression(df_new)
 