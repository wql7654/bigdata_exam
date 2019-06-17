import numpy as np

def OR(x1,x2):
    x = np.array([x1,x2])       ### numpy의 강점 : numpy 배열로 연산을 쉽고 빠르게?!
    w = np.array([0.5, 0.5])    # AND와는 가중치만 다르다
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
if __name__ == "__main__":
    print(OR(0,0))
    print(OR(1,0))
    print(OR(0,1))
    print(OR(1,1))