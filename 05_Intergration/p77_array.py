import numpy as np
A = np.array([1,2,3,4])
print(A) # 배열 그대로 출력

np.ndim(A)
print(A.shape[0], "띠용") # 배열 A의 모양(길이, 크기,요소 개수(1차원이라서 열의 갯수를 셈))

B = np.array([[1,2],[3,4],[5,6]])
print(B)

np.ndim(B) # 차원 수
print(B.shape) # 배열 B의 전체 출력

print(B.shape[0]) # 배열 B의 행 모양(길이, 크기, (행)요소 개수)
print(B.shape[1]) # 배열 B의 열 모양(길이, 크기, (열)요소 개수)