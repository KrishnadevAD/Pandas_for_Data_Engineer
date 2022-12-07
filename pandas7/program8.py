#alternative ::::::::::::::::::::


# task 4 
# 1)	Drop all those rows that has more than two null values ignore the name column
# 2)	For age replace the null values with average age
# 3)	For height replace the null values with median height
# 4)	For weight replace the null values with median weight
# 5)	Calculate the BMI
# 6)	Print the final output your file should contain following headers

import pandas as pd
import numpy as np

#reading the dataset
data = pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7\DataSetPractice.csv')

#getting the info of data
print(data.info)

#extracting the name column
nameColumn = data['name']
print(nameColumn)

#dropping the name from the data for extracting rows other than names
newData = data.drop('name',axis=1)
print("=============================")
print(newData)

#Dropping all the values using thresh i.e dropping null values from rows if row contains two null valeues
newData.dropna(axis = 0,thresh = 2,inplace=True)
print("=============================")
print(newData)

#creating np array of age height and weight for easy calculation of mean and median
age = np.array([newData['age']])
height = np.array([newData['height']])
weight = np.array([newData['weight']])
meanAge = np.nanmean(age)
medianHeight = np.nanmedian(height)
meanWeight = np.nanmean(weight)


#filling null values of age column , height column with mean
newData['age'].fillna(np.round(meanAge),inplace=True)
newData['height'].fillna(np.round(medianHeight),inplace=True)
newData['weight'].fillna(np.round(meanWeight),inplace=True)
print("=============================")
print(newData)

#calculation of BMI
newData['bmi'] = newData['height']/newData['weight']
newData['name'] = nameColumn


print("=============================")
print(newData)