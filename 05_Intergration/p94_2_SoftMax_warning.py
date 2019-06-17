import numpy as np

def softmax(a):             # p92 softmax 함수와 조금 다름
    c = np.max(a)           # 이 부분
    exp_a = np.exp(a - c)   # 오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([1010, 1000,990])
# print(np.exp(a) / np.sum(np.exp(a)))
print(softmax(a))

c = np.max(a)
print(a-c)

print(np.exp(a-c) / np.sum(np.exp(a-c)))

#a = np.array([0.3, 2.9,4.0])
a = np.array([7.7,5.5,2.2])
y = softmax(a)
print(y)        # 이 값들이 맞다는 개념보다 확률을 기반으로 접근함. 확률이 높을 것 같은 값을 보여줌
# 10개면 10개, 9개면 9개 값이 나온다.
print(np.sum(y))