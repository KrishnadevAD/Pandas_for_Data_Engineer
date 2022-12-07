import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')
print(data)
# 4)	For weight replace the null values with median weight
data1=pd.Series(data["weight"])
print(data1)
avg=data1.median()# taking the average 
print("the median weight  is :",avg)
data2=data1.fillna(avg)
print("",data2)