import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')
print(data)
# 2)	For age replace the null values with average age
data1=pd.Series(data["age"])
print(data1)
avg=data1.mean()# taking the average 
print(avg)
data2=data1.fillna(avg)
print(data2)
