import pandas as pd
import numpy as np

myDataFrame = pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day8\BL-Flickr-Images-Book.csv')

## Dropping unnecessary columns
## We can see some columns provide ancillary information that would be useful for the library
## but aren't very descriptive of the books
## I'll drop those columns to have just the information about the books
# list of columns to be dropped

toDrop = ['Edition Statement', 'Contributors', 'Corporate Author'
    , 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Shelfmarks']

myDataFrame.drop(columns=toDrop,inplace=True)

## Setting the Identifier column = index
## We can assume that when someone wants to access the information about a particular book
## they'd look up using some unique identifier

#checking if identifier is unique
print(myDataFrame['Identifier'].is_unique)

#setting index as indentifier
myDataFrame.set_index('Identifier',inplace=True)
print(myDataFrame.head().to_string())

# loc[] allows us to to label-based indexing (labeling of a row regardless of its position),
## so why not use the 'Identifier' column as index so it's easier just to look up all the records
## using their index which -after update- will be the same as their identifier

## we notice that the index or our 1st record has been updated from being 0 to being 206
## which is the same as its identifier
#printing the index using identifier
print(myDataFrame.loc[206])

#getting info of data frame
print("getting info of data frame",myDataFrame.info())

## Cleaning fields in the data (dtypes and data inconsistencies)

## it's important to get specific columns like date to a uniform format for better understanding
## and enforce consistency
## let's first check the different datatypes we have in our dataset
#------->>>>myDataFrame.get_dtype_counts() #.get_dtype_counts() is deprecated since 0.25.0,
myDataFrame.dtypes.value_counts()
print("The data type value count is : ",myDataFrame.dtypes.value_counts())


myDataFrame.dtypes
print("THE data type is : ",myDataFrame.dtypes)


## all of the datatypes are currently 'object' ~ str in native Ptyhon
## 'Date of Publication' is one column where it makes sense to enforce a numeric value so calculations
## can be performed later on
# let's check a few values first
myDataFrame['Date of Publication'].head(15)

## we can notice a few issues here:
## 1. extra dates in []: 1879 [1868]
## 2. date ranges: 1839, 38-54
## 3. NaNs
## we can fix these with regex as we notice that we only need the first 4 digits to get our year correct

#generating regex

regex = r'^(\d{4})'

#extracting satisfied data
#.str is used to apply native python string operations
#.extract is used to extract something from a string
#expand = true returns a dataframe object, false returns a string
satisfiedData = myDataFrame['Date of Publication'].str.extract(regex,expand = False)
print(satisfiedData.head())


#changing the original data fram
myDataFrame['Date of Publication'] = pd.to_numeric(satisfiedData)
print("date of the pulication ",myDataFrame['Date of Publication'])
print(myDataFrame['Date of Publication'].dtype)

#CHecking null data
print(myDataFrame['Date of Publication'].isnull())

#checking is null values are 15%
print(myDataFrame['Date of Publication'].isnull().sum()/len(myDataFrame['Date of Publication']))