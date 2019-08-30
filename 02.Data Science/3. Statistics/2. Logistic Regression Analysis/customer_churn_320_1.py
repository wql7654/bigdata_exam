#total charge를 기준으로 1,2,3,4 분위중 어디에 포함되는지에 대한 정보를 2진형 데이터 열로 추가

# import numpy as np
import pandas as pd


 # Read the data set into a pandas Dataframe
churn = pd.read_csv('churn.csv', sep = ',', header = 0)

churn.columns = [heading.lower() for heading in \
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                            churn['night_charge'] + churn['intl_charge']

qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix = 'total_charges')
churn_with_dummies = churn.join(dummies)
print(churn_with_dummies.head())
pass