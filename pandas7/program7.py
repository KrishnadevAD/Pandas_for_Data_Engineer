import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')
print(data)
# 6)	Print the final output your file should contain following headers
#   name    age  height  weight BMI 
# 1)	Drop all those rows that has more than two null values ignore the name column
y=data.dropna(inplace=True)
print(y)
# 2)	For age replace the null values with average age
data1=pd.Series(data["age"])
print(data1)
avg=data1.mean()# taking the average 
print(avg)
data2=data1.fillna(avg)
print(data2)

# 3)	For height replace the null values with median height
data1=pd.Series(data["height"])
print(data1)
avg=data1.median()# taking the average 
print("the median height is :",avg)
data2=data1.fillna(avg)
print(data2)
# 4)	For weight replace the null values with median weight
data1=pd.Series(data["weight"])
print(data1)
avg=data1.median()# taking the average 
print("the median weight  is :",avg)
data2=data1.fillna(avg)
print("",data2)
# 5)	Calculate the BMI
data1=pd.Series(data["weight"])
print(data1)
total=data1.sum()
data2=pd.Series(data["height"])
print(data2)
total1=data2.sum()
Bmi=total/total1
print("the BMI is :",Bmi)


