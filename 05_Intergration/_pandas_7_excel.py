import pandas as pd

mysource = {'시도':['서울','경기','인천','부산','대전'],
            '구분':['특별시','도','광역시','광역시','광역시'],
            '인수':['990만명','1300만명','350만명','300만명','150만명'],
            '면적':[605.2,"10,717","1,029",767.4, 539.8]}
# print(mysource)

df = pd.DataFrame(mysource)
print(df)

df.to_csv('sample0625.csv', encoding="ms949")