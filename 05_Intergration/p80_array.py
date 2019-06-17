import numpy as np

A = np.array([[1,2,3],[4,5,6]])
print(A.shape)

B = np.array([[1,2],[3,4],[5,6]])
print(B.shape)

print(np.dot(A,B))

'''
C = np.array([[1,2],[3,4]])
print(C.shape)
print(A.shape)
print(np.dot(A,C)) # A와 C의 배열 크기가 다르므로 내적 계산(행렬곱)을 할 수 없다.
'''
A = np.array([[1,2],[3,4],[5,6]])
print(A.shape)
B = np.array([7,8])
print(np.dot(A,B))


