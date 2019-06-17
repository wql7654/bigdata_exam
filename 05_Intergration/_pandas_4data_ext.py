import pandas as pd
# extraction - 추출

#키,몸무게, 유형 데이터 프레임 생성하기

Tbl = pd.DataFrame({"weight":[80.0, 70.4, 65.5, 45.9, 51.2,72.5],
                    "height":[170,180,155,143,154,160],
                    "gender":["f","m","m","f","f","m"]})

print("--- height가 160이상인 것")
print(Tbl[Tbl.height >= 160])
print("---gender가 m인 것")
print(Tbl[Tbl.gender == "m"])
