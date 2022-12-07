import numpy as np
import pandas as pd


#births CSV file

myDataFrame = pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day10\births.csv')

# Questions ::::
#  1.) Extract the  data of only the Year == 1979 
#  2.) Find maximum  birth of the Male in 1979 
#  3.) Find maximum birth of the Female in 1979 
#  4.) Find the maximum  number of birth  in 1979  


#getting data only of 1969 and storing in data frame 
df1979= myDataFrame.loc[(myDataFrame['year'] == 1979 )]

a1979 = np.array(df1979)
print(len(a1979))

#getting only male births data of 1969 and storing in array
array1979BMale = np.array(df1979.loc[myDataFrame['gender'] == 'M']['births'])
print("Male Birth", len(array1979BMale))

#getting only Female births data of 1969 and storing in array
array1979BFemale = np.array(df1979.loc[myDataFrame['gender'] == 'F']['births'])

# Example 1: Use numpy.append() function
#arr = np.array([[0,2,4],[6,8,10]]) 
# app_arr = np.append(array1979BFemale, [13,15,17]) 

print("Female Birth", len(array1979BFemale))

#getting Total Birth of 1979

arraytotal = np.add(array1979BMale,array1979BFemale)
print("Total Birth",len(arraytotal))

#getting maxBirthData
maxBirth = np.max(arraytotal)
print("max Birth",maxBirth)

#Max Male and Female
maxMale = np.max(array1979BMale)
maxFeMale = np.max(array1979BFemale)
print("Max Male Birth",maxMale )
print("Max Female Birth", maxFeMale)

# male bith ko index value nikaleko 
maxMaleBirthIndex = np.where(array1979BMale == maxMale)[0][0]
print("Max Male Birth Index",maxMaleBirthIndex)

# Female bith ko index value nikaleko 
maxFeMaleBirthIndex = np.where(array1979BFemale == maxFeMale)[0][0]
print("Max Female Birth Index",maxFeMaleBirthIndex)

# total birth in 1969 ko index nikaleko 
maxBirthIndex = np.where(arraytotal ==maxBirth)[0][0]
print("Max Birth Index Total",maxBirthIndex)

#  Total male ko value kati xa , nikaleko 
valueofMale = array1979BMale[maxBirthIndex]
print("Value of Male ",valueofMale)

# Total Female ko value kati xa , nikaleko 
valueofFemale = array1979BFemale[maxBirthIndex]
print("Value of Female",valueofFemale)

mainarrayIndexMale = np.where(a1979 == valueofMale)[0][0]
print("Main Array Index Male :",mainarrayIndexMale)
maxBirthRowMale = df1979.loc[mainarrayIndexMale]
print("Max Birth Row Male :\n",maxBirthRowMale)

mainarrayIndexFeMale = np.where(a1979 == valueofFemale)[0][0]
print("Main Array Index Female :",mainarrayIndexFeMale)
maxBirthRowFeMale = df1979.loc[mainarrayIndexFeMale]
print("Max Birth Row Female :\n",mainarrayIndexFeMale)
print(f'The maximum number of Female birth in 1969 is {maxFeMale} in date {maxBirthRowFeMale["year"]}/ {maxBirthRowFeMale["month"]}/ {round(maxBirthRowFeMale["day"])}')
print("====================================")
print(f'The maximum number of male birth in 1969 is {maxMale} in date {maxBirthRowMale["year"]}/ {maxBirthRowMale["month"]}/ {round(maxBirthRowMale["day"])}')
print("====================================")
print(f'The maximum number of total birth in 1969 is {maxBirth} in date {maxBirthRowMale["year"]}/ {maxBirthRowMale["month"]}/ {round(maxBirthRowMale["day"])}')

# array1969gender = np.array(myDataFrame.loc[myDataFrame['year'] == 1969]['births'])


# array1979 = np.array(myDataFrame.loc[myDataFrame['year'] == 1979]['births'])
# array1989 = np.array(myDataFrame.loc[myDataFrame['year'] == 1989]['births'])
# array1999 = np.array(myDataFrame.loc[myDataFrame['year'] == 1999]['births'])
# array2008 = np.array(myDataFrame.loc[myDataFrame['year'] == 2008]['births'])