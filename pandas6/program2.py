import pandas as pd
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day6\Building_Permits.csv')

# checking the first five rows of the csv file 
print(data.head())

# checking the first Three rows of the csv file 
print(data.head(3))

#checking the last five rows of the CSV file 
print(data.tail())


#checking the last five rows of the CSV file 
print(data.tail(3))

# taking the information about the  CSV file 
print(data.info())

# main kuraa in pandas
# how  handle the missing data  in pandas 