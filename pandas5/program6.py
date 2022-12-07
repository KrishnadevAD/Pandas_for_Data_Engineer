#dataframe in the pandas 
# df bhanne bitikai hamle , pandas ko euta  column bhanne bujhne hai  guys 
import pandas as pd
# it takes the 1 st and 2nd columns of dict
# it prints the key of a & b but in c & d there is no 
# value in the first row so there will be NaN vlaue 
dataNew=pd.DataFrame([{'a':1,'b':2},{'c':3,'d':5}])
 # here in both the  row value of a & b columnn 
 # are given so the series will be without the NaN value 
dataNew2=pd.DataFrame([{'a':1,'b':2},{'a':3,'b':5}])
print(dataNew)
print(dataNew2)
dataNew3=pd.DataFrame([{'a':1,'b':2,'c':3,'d':5},{'a':1,'b':2,'c':3,'d':5}])
print(dataNew3)