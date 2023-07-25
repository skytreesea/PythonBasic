import numpy as np
import pandas as pd
# 자료를 분석, np: 수치자료, 계산, pd: 다양한 자료, 수치, 범주형
# array: 배열 
a = np.array([[1,2,3,3,4,5],[2,3,4,4,5,6]])
print(a[1]) # number 

b_list =['tree','bird','sky']

print(b_list[1])
# 컴퓨터는 숫자를 0부터 센다 

print(a.transpose())

print(a[0])
print(a[1].sum()) # 합
print(a[1].mean()) # 평균
print(a[1].min()) # 최소
print(a[1].max()) # 최대
print(a[0][0]) # 슬라이싱
print(a[-1][-1]) # 슬라이싱
print(a[:,3:]) # 슬라이싱
c= np.ones((5,5)) # 0으로만 이뤄진
d = np.ones((5,5)) # 1로만 이뤄진

print(3* c / 5*d) 
print(a.shape)

new_a = a[:,3:] 
print(new_a.shape)
print(new_a[0].mean())
print(new_a[1].mean())
print(new_a[1].sum())