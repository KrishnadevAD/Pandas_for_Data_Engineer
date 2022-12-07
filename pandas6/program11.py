import pandas as pd
import numpy as np
df=pd.DataFrame([[1,np.nan,2],
    [2,4,5],
    [np.nan,4,5]])
print(df)
#we can make use of how parameter to control the dropping even more
print("----------------------------")
df[3] = np.nan
print(df)
print("----------------------------")
#drops rows and columns that are all null values
ae = df.dropna(axis='columns',how='all')
print(ae)

