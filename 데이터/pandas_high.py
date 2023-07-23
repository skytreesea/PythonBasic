#merge 와 concat, 피봇테이블 사용법 

import pandas as pd

# 첫 번째 데이터 프레임
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# 두 번째 데이터 프레임
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [25, 30, 22, 28]
})

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)

# 첫 번째 데이터 프레임
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# 두 번째 데이터 프레임
df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})
concatenated_df = pd.concat([df1, df2], axis=0)
print(concatenated_df)

# 샘플 데이터 프레임 생성
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 8, 6, 9, 12],
    'Quantity': [3, 2, 4, 3, 2, 5]
}

df = pd.DataFrame(data)

# 피봇 테이블 생성
pivot_table = pd.pivot_table(df, index='Category', values='Value', aggfunc='mean')
print(pivot_table)