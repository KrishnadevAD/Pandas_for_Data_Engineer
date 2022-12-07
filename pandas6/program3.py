import pandas as pd
import numpy as np
#data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day6\Building_Permits.csv')
# data1=np.array([1,2,3,4,5,None]) # 3e cannot use aggregate function 
# print(data1)
# print(data1.dtype)
# print(data1.sum()) # type error 

# handling missing data 
#  python missing data 
data2=np.array([1,2,3,4,5,np.nan])# BY Defult it print float type 
print(data2)# nan is oly the float type 
print(data2.dtype)
print("###########################################")
#nan is like a virues anything 
#it touches changes to nan for examole
print(1*np.nan)
print(1+np.nan)
#
# #array aggregate are defined
print("###########################################")
print(data2.sum())
print(data2.min())
print(data2.max())
print(data2.sum())
#
print("###########################################")
# #To solve this use np.nansum()
# #note that nan is specifically float
print(np.nansum(data2))

print(data2.sum())# it donot send the error hai 
# we prefer NaN so it prints oly on float
print(np.nansum(data2)) # it gives in float
