import pandas as pd
# extraction - 추출

#키,몸무게, 유형 데이터 프레임 생성하기

Tbl = pd.DataFrame({"weight":[80.0, 70.4, 65.5, 45.9, 51.2],
                    "height":[170,180,155,143,154],
                    "type":["f","n","n","t","t"]})

# 몸무게 목록 추출하기
print("몸무게 목록")
print(Tbl["weight"])

#몸무게와 키 목록 추출하기
print("몸무게와 키 목록")
print(Tbl[["weight","height"]])
#print(Tbl[["weight","height","type"]])

# (0부터 셌을 때)2~3번째 데이터 출력
print("Tbl[2:4]\n",Tbl[2:4])

# (0부터 셌을 때)3번째 이후의 데이터 출력하기
print("Tbl[2:]\n",Tbl[2:])