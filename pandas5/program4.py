import pandas as pd
x=pd.Series([1,2,3,4,5],index=[2,4,5,6,8]) #indexed explicitly passed 
y=pd.Series([1,2,3,4,5])# indexed implicitly passed 
print(x)
print(y)
print(x.values)# printing the values
print(y.values)
print(x.index)#printing the index
print(y.index)#RangeIndex(start=0, stop=5, step=1)