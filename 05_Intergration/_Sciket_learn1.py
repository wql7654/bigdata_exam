# sciket-learn을 이용한 분류(Classification)
from sklearn import svm

xor_data = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]

training_data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    res=row[2]
    training_data.append([p,q])
    label.append([res])

clf = svm.SVC() # classification  을 도와주는 method
clf.fit(training_data, label)
pre = clf.predict(training_data)
print("예측결과:",pre)

ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok+=1
    total+=1
print("정확도: ",ok,"/",total, "=", ok/total)