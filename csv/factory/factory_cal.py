import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
df = pd.read_csv(r'C:\Users\skytr\OneDrive\문서\PythonBasic\csv\factory\factory_test.csv', thousands=',')
df['전용면적당거래금액'] = df['거래금액(만원)']/df[ '전용/연면적(㎡)']
df['용적률'] = df['전용/연면적(㎡)']/df[ '대지면적(㎡)']
print(df.columns)
print(df.value_counts('유형'))
print(df.value_counts('용도지역'))
print(df.value_counts('건축물주용도'))
print(df.groupby(by = '건축물주용도')['거래금액(만원)'].mean())
print(df.groupby(by = '건축물주용도')['전용면적당거래금액'].mean())
df.groupby(by = '용도지역')['전용면적당거래금액'].describe().to_clipboard()
# 전체 상위 5개 출력
df2 = df.sort_values(by = '전용면적당거래금액', ascending = False).loc[:5,('시군구','도로조건','건축물주용도','용도지역','전용/연면적(㎡)', '대지면적(㎡)', '거래금액(만원)', '전용면적당거래금액','용적률')]
# 상위 5개 제외
df3 = df.sort_values(by = '전용면적당거래금액', ascending = False).loc[5:,('시군구','도로조건','건축물주용도','용도지역','전용/연면적(㎡)', '대지면적(㎡)', '거래금액(만원)', '전용면적당거래금액','용적률')]

# print(df2.corr())

print(df2['용적률'].describe())
x = df3['용적률'] 
y = df3['전용면적당거래금액']  
print(df2.describe())
result = df.pivot_table(values= '전용면적당거래금액', index='용도지역', columns='건축물주용도', aggfunc='mean')
print(result)
result.to_clipboard()
# plt.plot(x,y,'o')
# plt.show()

'''
correlation_values = {}
for col1 in df.columns:
    for col2 in df.columns:
        try:
            if col1 != col2:
                corr_coeff, p_value = stats.pearsonr(df[col1], df[col2])
                correlation_values[(col1, col2)] = (corr_coeff, p_value)
        except:
            pass

for cols, (corr, p) in correlation_values.items():
    print(f"Columns: {cols}")
    print(f"Correlation Coefficient: {corr}")
    print(f"P-value: {p}")
    print("----" * 10)'''