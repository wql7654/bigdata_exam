# 기본 통계 항목 확인하기

import numpy as np
import pandas as pd

churn = pd.read_csv('churn.csv',sep=',',header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01']=np.where(churn['churn']=='True.',1.,0.)
print("~"*80)
print("print(churn.head())")
print("~"*80)
print(churn.head())

print("\n"+"="*80)
print("print(churn.describe())")
print(churn.describe())
