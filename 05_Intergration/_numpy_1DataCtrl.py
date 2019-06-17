# 고급데이터 분석 및 수치계산 등의 기능 제공
# 수치계산을 효율적으로,
# 다차워 배열
# 고수준의 수학 함수 제공
import numpy as np

# 10개의 float32 자료형 데이터 생성
V = np.zeros(10,dtype=np.float32)
print(V,"float32 자료형 데이터 10개 생성")

# 연속된 10개의 unit64 자료형 데이터 생성
V = np.arange(10,dtype=np.uint64)
print(V,"unsigned int64 자료형 데이터 (연속된) 10개 생성")

#V값 3배하기
V *=3
print("V값의 3배 : ",V)

#V의 평균 구하기
print("V값의 평균 :",V.mean())
