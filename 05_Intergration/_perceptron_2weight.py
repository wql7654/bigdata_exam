# theta 값을 -b로 .
# b는 편향이라고 부른다.
# -b를 치환한다.
# p.52 참고
'''
y = 0 (b + w1x1 = w2x2 <=0)
  = 1 (b + w1x1 + w2x2 > 0)
'''
import numpy as np
x = np.array([0,1])
y = np.array([0.5,0.5])
b = -0.7
w= np.array([0.,0.5])##################
print(np.sum(w*x))
print(np.sum(w*x)+b)
