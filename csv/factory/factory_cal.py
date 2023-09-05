import pandas as pd
import matplotlib.pyplot as plt
import usecsv
from scipy import stats
df = pd.read_csv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\raw\공장2308.csv', thousands=',')
base_url = r"C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\factory_test"
df['대지면적당거래금액'] = df['거래금액(만원)']/df[ '대지면적(㎡)']
df['용적률'] = df['전용/연면적(㎡)']/df[ '대지면적(㎡)']
print(df.columns)
print(df.value_counts('유형'))
print(df.value_counts('용도지역'))
print(df.value_counts('건축물주용도'))
df.groupby(by = '건축물주용도')['거래금액(만원)'].describe().to_csv(base_url + r'\건축물주용도_거래금액.csv', encoding = 'utf=8-sig')
df.groupby(by = '건축물주용도')['대지면적당거래금액'].describe().to_csv(base_url + r'\건축물주용도_대지면적당거래금액.csv', encoding = 'utf=8-sig')
df.groupby(by = '도로조건')['대지면적당거래금액'].describe().to_csv(base_url + r'\도로조건_대지면적당거래금액.csv', encoding = 'utf=8-sig')
df.groupby(by = '용도지역')['대지면적당거래금액'].describe().to_csv(base_url + r'\test_v1.csv', encoding = 'utf=8-sig')
df.describe().to_csv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\factory_test\전체_describe.csv', encoding = 'utf=8-sig')
 # 전체 상위 5개 출력
df2 = df.sort_values(by = '대지면적당거래금액', ascending = False).loc[:5,('시군구','도로조건','건축물주용도','용도지역','전용/연면적(㎡)', '대지면적(㎡)', '거래금액(만원)', '대지면적당거래금액','용적률')]
# 상위 5개 제외
df3 = df.sort_values(by = '대지면적당거래금액', ascending = False).loc[5:,('시군구','도로조건','건축물주용도','용도지역','전용/연면적(㎡)', '대지면적(㎡)', '거래금액(만원)', '대지면적당거래금액','용적률')]

df2['용적률'].describe().to_csv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\factory_test\용적률test_v1.csv', encoding = 'utf=8-sig')

result = df.pivot_table(values= '대지면적당거래금액', index='도로조건', columns='건축물주용도', aggfunc='mean')
print(result)
result.to_csv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\factory_test\도로조건_건축물주용도_대지면적당거래금액_v1.csv', encoding = 'utf=8-sig')


# x = df3['용적률'] 
# y = df3['대지면적당거래금액']  
# plt.plot(x,y,'o')
# plt.show()

# 특정지역
# df[df['시군구'].str.contains('동산동')].to_clipboard() 
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