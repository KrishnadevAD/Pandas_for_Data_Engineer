import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')
print(data)
# 5)	Calculate the BMI
data1=pd.Series(data["weight"])
print(data1)
total=data1.sum()
data2=pd.Series(data["height"])
print(data2)
total1=data2.sum()
Bmi=total/total1
print("the BMI is :",Bmi)