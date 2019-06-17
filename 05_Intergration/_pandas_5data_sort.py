import pandas as pd
# extraction - 추출

#키,몸무게, 유형 데이터 프레임 생성하기

Tbl = pd.DataFrame({"weight":[80.0, 70.4, 65.5, 45.9, 51.2,72.5],
                    "height":[170,180,155,143,154,160],
                    "gender":["f","m","m","f","f","m"]})

print("--- 키로 정렬")
print(Tbl.sort_values(by="height"))
print("--- 몸무게로 정렬")
print(Tbl.sort_values(by="weight",ascending=False))
#ascending - 오름차순 정렬, 옵션을 거짓으로 바꿨으니 -> 내림차순