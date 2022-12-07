# giving explicit index and making series
import pandas as pd
data=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])# giving explicit index and making series
print(data)
print(data['a'])# series behaves as dictionary

# use dictiornary to examine value
print('a' in data)

# like dictinary
print(data.keys())
# it gives the item value in the tuples , as dictionary hai 
print(list(data.items()))