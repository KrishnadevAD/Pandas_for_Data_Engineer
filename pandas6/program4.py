import pandas as pd
import numpy as np
x=pd.Series([1,2,3,4,5,np.nan,None])
print("The sum is : ",x.sum())

#Pandas treatment on NAN and None
#consider the following series
#treats None and Nan as same
x = pd.Series([1,2,np.nan,None])
# it prints the cvalue have NaN as it is  !!!
print(x)