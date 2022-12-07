import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')
print(data.head())
print(data.head(3))
print(data.tail())
print(data.tail(3))
print(data.info())

# task 4 
# 1)	Drop all those rows that has more than two null values ignore the name column
# 2)	For age replace the null values with average age
# 3)	For height replace the null values with median height
# 4)	For weight replace the null values with median weight
# 5)	Calculate the BMI
# 6)	Print the final output your file should contain following headers
