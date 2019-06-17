import numpy as np

def softmax(a):                 # 오버플로 대책이 없음. p.92~94 참고
    exp_a = np.exp(a)           # exponential function(지수 함수, p.91)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

if __name__ == "__main__":
    a = np.array([0.3, 2.9, 4.0])

    exp_a = np.exp(a) # 지수 함수
    print(exp_a)

    sum_exp_a = np.sum(exp_a) # 지수 함수의 합
    print(sum_exp_a)

    y = exp_a / sum_exp_a
    print(y)