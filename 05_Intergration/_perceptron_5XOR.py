import numpy as np
# 세팅에서 인터프리터에서 추가해줘야 함
from  _perceptron_1AND import *
from _perceptron_4NAND import *
from _perceptron_5OR import *

def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <=theta:
        return 0
    elif tmp > theta:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])       ### numpy의 강점 : numpy 배열로 연산을 쉽고 빠르게?!
    w = np.array([0.5, 0.5])    # AND와는 가중치만 다르다
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y =AND(s1,s2)
    return y

if __name__ =="__main__":
    print(XOR(0, 0))
    print(XOR(1, 0))
    print(XOR(0, 1))
    print(XOR(1, 1))

