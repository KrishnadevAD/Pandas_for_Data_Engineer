import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')
print(data)
# 3)	For height replace the null values with median height
data1=pd.Series(data["height"])
print(data1)
avg=data1.median()# taking the average 
print("the median height is :",avg)
data2=data1.fillna(avg)
print(data2)