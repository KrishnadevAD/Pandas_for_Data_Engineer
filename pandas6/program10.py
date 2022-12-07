import pandas as pd
import numpy as np
df=pd.DataFrame([[1,np.nan,2],
    [2,4,5],
    [np.nan,4,5]])
print(df)
print('***********************')
ab=df.dropna()
print(ab)
print('***********************')
ac=df.dropna(axis=0)# rows lai matra udauxa/hatauxa 
print(ac)
print('***********************')
ad=df.dropna(axis=1)# columns lai udai dinxa  hai guys 
print(ad)

print('***********************')
print('***********************')
#alternatively we can drop in different axis: axis =1 columns,  axis = 0 rows
print("----------------------------")
ac = df.dropna(axis='columns')
print(ac)

print('***********************')
print('***********************')
#alternatively we can drop in different axis: axis =1 columns , axis = 0 rows
print("----------------------------")
ad = df.dropna(axis='rows')
print(ad)