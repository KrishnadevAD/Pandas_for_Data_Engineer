import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7a\Building_Permits.csv')

# getting sample of data and changing to string for easy viewing
print(data.sample(10).to_string())
print("==================")

#getting the shape of data
print( " THe shape of the data is : ",data.shape)
print("========PRODUCT==========")

#finding the total cells i.e rows X Columns
totalCells = np.product(data.shape)
print(" The Total Cells is : ",totalCells)

#checking the total amount of data in rows and columns
missingCount = data.isnull().sum()
print("=======Missing Count===========")
print("The missing count is : ",missingCount)

#getting all total missing values
totalMissingValues = missingCount.sum()
print("=======Missing Count In All Data===========")
print("The missing Values is : ",totalMissingValues)

#getting total percentage of missing values
missingPercentage =(totalMissingValues/totalCells)* 100
print("===================Missing Percentage==========")
print("The missing Percentage is :",missingPercentage)
print("=============================")

#getting missing values in two fields
print("getting missing values in two fields",missingCount[['Street Number Suffix','Zipcode']])
print("===================#############==========")
#getting percentage of missing values in Street Number
print("getting percentage of missing values in Street Number",(missingCount['Street Number Suffix']/data.shape[0])*100)
print("===================#############==========")
#getting percentage of missing values in zipcode
print("getting percentage of missing values in zipcode : \n",(missingCount['Zipcode']/data.shape[0])*100)