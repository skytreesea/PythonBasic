import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 합계
print(np.sum(arr))

# 평균
print(np.mean(arr))

# 최댓값
print(np.max(arr))

# 최솟값
print(np.min(arr))

# 표준편차
print(np.std(arr))

# 0부터 1 사이의 랜덤한 값을 가진 2x3 배열 생성
random_arr = np.random.random((2, 3))
print(random_arr)   

# 행렬 생성
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

# 행렬 곱셈
mat_product = np.dot(mat1, mat2)
print(mat_product)

# 전치 행렬
mat_transpose = np.transpose(mat1)
print(mat_transpose)