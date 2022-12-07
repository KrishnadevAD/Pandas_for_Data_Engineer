import pandas as pd
import numpy as np
df=pd.DataFrame([[1,np.nan,2],
    [2,4,5],
    [np.nan,4,5]])
print(df)

#we can use thresold to have control over how many not null elements to keep in rows or column
print("----------------------------")
y = df.dropna(axis='rows',thresh=3)
#rows with more than one null values are gone
print(y)