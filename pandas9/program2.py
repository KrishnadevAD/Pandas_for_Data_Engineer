import numpy as np
import pandas as pd

#filter the data of president heights

myDataframe = pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day9\president_heights_practice.csv')
print("MyDataFrame Original\n",myDataframe)

# removing null data where column is null
myDataframe.dropna(subset=['name'], inplace=True)
print("MyDataFrame Removed\n",myDataframe)

myDataframe['Measured Date'] = pd.to_datetime(myDataframe['Measured Date'])
print("DataFrame Dtype",myDataframe['Measured Date'].dtype)


# removing null value to 0 in height
myDataframe['height(cm)'].fillna(0,inplace=True)

# Changing height grater than 200
#converting to np array
myArray = np.array(myDataframe['height(cm)'])

#getting data where height is greater than 200
resultArray = np.where(myArray > 200)
print("resultArray",resultArray)

#deleteing outliers args ( orginal array, result Array )
np.delete(myArray, resultArray)

#calculating median
median = np.median(myArray)

###getting height of row 2
print("---",myDataframe.loc[2,"height(cm)"])

#changing height greater than 200 and less than median height
for x in myDataframe.index:
    if myDataframe.loc[x,"height(cm)"] >= 200 or myDataframe.loc[x,"height(cm)"] < 1:
        myDataframe.loc[x,"height(cm)"] = median
print("changing height greater than 200 and less than median height",myDataframe['height(cm)'])