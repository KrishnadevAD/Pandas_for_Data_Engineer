import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')
print(data)

# 1)	Drop all those rows that has more than two null values ignore the name column
y=data.dropna(axis = 0,thresh = 2,inplace=True)
print(y)