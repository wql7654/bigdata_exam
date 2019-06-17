import numpy as np
import matplotlib.pylab as plt

def sigmoid(x): # 시그모이드 함수
    return 1 / (1 + np.exp(-x))

def relu(x): # 렐루라고 부름. p.76 ReLU
    return np.maximum(0, x)

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)

x = np.arage(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
#plt.show()
# 정교한 값이 필요하여 계단함수보다 시그모이드 함수를 좀 더 많이 사용함(현재)
