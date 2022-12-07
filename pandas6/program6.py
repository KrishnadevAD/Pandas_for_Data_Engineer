import pandas as pd
import numpy as np
#methos to handle null value ::::::
# isnull()--> null value ko chai boolen marks ,creates the null value true 
# notnull()--> Opposite of isnull() create a boolean mask of not null values
#dropna()---> it gives the null value dropped, drop gareko null value dinxa 
            # Returns the filtered version of data with null values dropped
#fillna()----> rerurns the filltered version of data with null filled 
            #Returns the filtered version of data with null values filled 
x=pd.Series([1,2,3,4,np.nan,None])
print(x)

# printing boolean mask
print(x.isnull()) # jaa null values xa tya true value dinxa ,only boolean

# printing null vlaues
print(x[x.isnull()])# value nai dine bhayou 
print('**************************')

# printing not boolean mask

print(x.notnull())#  ja null value xen tyslai True gardinxa ,only boolean

# printing not null values
print(x[x.notnull()])
print('**************************')

# dropping null values doesn't change orginial data

 # dropna le original value lai change gardaina hai 
y=x.dropna(inplace=True)# original file lai change gardain 
print(y)
print('**************************')

print(x)

print('**************************')
y=x.fillna(23)
print(y)

print('**************************')
print(x)