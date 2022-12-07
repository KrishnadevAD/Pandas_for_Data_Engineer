#we can pass explicitly data 
import pandas as pd
x=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])# explicitly passing the index values
print(x)# it prints all the series of x 
print(x[0]) # it can be taken by index value it prints out the zeroth index value that is  1