import pandas as pd

'''
    A B C
    D E F
    G H I
    이렇게 있다면 A E I를 기준으로 대칭되는 행렬의 위치를 반전
'''

Tbl = pd.DataFrame([["A","B","C"],["D","E","F"],["G","H","I"]])

print(Tbl)
print("---")
print(Tbl.T)

print("\n\n")
Tbl2 = pd.DataFrame([["1","2","3","4","5"],
                    ["6","7","8","9","10"],
                    ["11","12","13","14","15"],
                    ["16","17","18","19","20"],
                    ["21","22","23","24","25"]])

print(Tbl2)
print("---")
print(Tbl2.T)