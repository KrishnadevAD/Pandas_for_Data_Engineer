# giving explicit index and making series
import pandas as pd
# giving explicit index and making series
myseries=pd.Series(['a','b','c','d','e'],index=[1,2,3,4,5])
print("my series is",myseries)
#Explicit indexing 
print(myseries[3])
# impicit indexing 
print(myseries[1:3])
print("**************************************")
# to change this we use loc

print(myseries.loc[3])#explicitly 
print(myseries.iloc[3])#implicitly
# print("**************************************")
# this uses explicit index
print(myseries.loc[3]) #explicitly 
print(myseries.loc[1:3])
# print("**************************************")

# this uses implicit index
print(myseries.iloc[3])# implicitly 
print(myseries.iloc[1:3])