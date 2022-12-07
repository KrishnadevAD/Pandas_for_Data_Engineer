#we can pass explicitly data 
import pandas as pd
x=pd.Series([1,2,3,4,5],index=[2,3,4,5,6])
print("The value of x are in series :\n",x)
# hami sanga , x[3] index bhaneko chai uta 2 hunxa 
print("The index value of the 3 is in series:",x[3])
print("The values of the x ",x.values)
print("The index values of the x is :",x.index)