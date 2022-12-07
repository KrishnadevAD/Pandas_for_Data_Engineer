import pandas as pd
import numpy as np
dataframe=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day8\BL-Flickr-Images-Book.csv')

# taking data samples 
# print(dataframe.sample(5).to_string())
# print(dataframe.info())


# we are going to take the book information
 # to drop array 
toDrop =['Edition Statement','Contributors','Corporate Author','Corporate Contributors',
'Former owner','Engraver','Issuance type','Shelfmarks','Flickr URL']
dataframe.drop(columns=toDrop,inplace=True)
print(dataframe.sample(5).to_string())

# checking if the identifier is unique\
print(dataframe['Identifier'].is_unique)# the identifier is unique so its true ,
# than we can make the identifier as index 
# transforming identifier as a index
dataframe.set_index('Identifier',inplace=True)
print(dataframe.sample(5).to_string)# .to_string is done , because ther will not come the coclumns 

# usning lock find the value of 206
## loc[] allows us to to label-based indexing 
# (labeling of a row regardless of its position),
print(dataframe.loc[206]) # it fund the value of the information

# getting the information of data 
print(dataframe.info())
# it gives the inconsistents data like below  
print(dataframe['Date of Publication'].head(15))

# usig regex to clean the data 
re=r'^(\d{4})'
staisfielldData = dataframe['Place of Publication'].str.extract(re,expand=False)
print(staisfielldData.head(15))

#changing the original data to needed datatype
dataframe['Date of Publication']=pd.to_numeric(staisfielldData)

# finding the null value ism
print(dataframe['Date of Publication'].isnull().sum())

# taking the precentage  with respect  to the date of the  publication 
print(dataframe['Date of Publication'].isnull().sum()/len(dataframe['Date of Publication']))


publication = dataframe['Place of Publication']# publication lai matra pahilaa isolate garne 
print(publication.head(15)) # erro comes so fixed in publication cities



 # cities mixed with something 
 # isolate the london
 # .str.contains('london') ma london ko bhako tanyou 
london = publication.str.contains('london')# it isolate london, if there is missing with any 
# string in the london 
print(london)# london maa True halxa  and aro maa chai False aauxa 
# chechking london maa true aaux ki nai , london = True aro False aauxa 
print("#########################################")
# yehaa false xa so , Value false aauxa i.e other than london 
print(dataframe.loc[4158128,'Place of Publication'])
# yehaa True xa so , value True aauxa i.e  value = London aauxa 
print("#########################################")
print(dataframe.loc[4158088,'Place of Publication'])


oxford = publication.str.contains('Oxford')
print(oxford) # boolean aauxa i.e True | False , True for Oxford and False for others 


#(np.where)--->  le chai simply if , elif ko kaam garxa 
#(london,'London')---> london bhako thau ma London rakhdinxa 
#(oxford,'oxford')---> oxford bhako thau ma oxford rakhdinxa 
# otherwise , publication.str.replace("-"," ") ---> publication ko sabai lai str ma convert garyou r replace garyou "-" lai " " maa
dataframe['Place of Publication']=np.where(
    london,'London',np.where(
    oxford,'oxford',publication.str.replace("-"," ")
    )
)
print(dataframe.loc[4157862])