import pandas as pd
import numpy as np
#methos to handle null value ::::::
# isnull()--> null value ko chai boolen marks ,creates the null valur true 
# notnull()--> posite of is null
#dropna()---> it gives the null value dropped, drop gareko null value dinxa 
#fillna()----> rerurns the filltered version of data with null filled 
x=pd.Series([1,2,3,4,np.nan,None])
print(x)


y=x.dropna(inplace=True)# original file lai change gardain 
print(y)
print('**************************')
print(x)