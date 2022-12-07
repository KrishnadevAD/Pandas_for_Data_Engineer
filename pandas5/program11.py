# index ko powerfull kuraa hai guys
# pandas index can be used as ordered set and 
# can perfom many operation
import pandas as pd
indA=pd.Index([1,2,3,4,5])
indB=pd.Index([4,5,6,7,8])
# we can use the aggregate function
print(indA&indB)# intersection
print(indA|indB)#union
print(indA^indB)
print(indB^indA)