import pandas as pd 
import statsmodels.formula.api as smf
from scipy import stats
df = pd.read_csv(r'C:\Users\ERC\Documents\GitHub\PythonBasic\데이터\지방공기업연구\rc_grand.csv')


#일단 전체로 수행
model = smf.ols(formula = '경상수지비율~부채비율', data = df)
result = model.fit()
# print(result.params.부채비율)
print(result.summary())