#indexes of the pandas array
import pandas as pd
ind=pd.Index([2,3,4,5,6,7])# we can make simply index of the dataframe in pandas
print(ind)
print(ind[0])
print(ind[3])
#TypeError: Index does not support mutable operations, below code gives an error
#ind[0]=4 # pandas index is immutable that is we cannot change the value of the pandas index value
print(ind.shape)
#pandas behaves like the series 
print(ind.ndim)
print(ind.size)
print(ind.dtype)

