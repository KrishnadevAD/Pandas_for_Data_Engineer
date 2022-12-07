import pandas as pd
import numpy as np

df=pd.DataFrame([[1,np.nan,2],
    [2,4,5],
    [np.nan,4,5]])
# printing the pandas series made above 
print(df)

print("###########################")
# dropping null valuues in dataframe
# print all the rows without null values 
ab=df.dropna()
print(ab)