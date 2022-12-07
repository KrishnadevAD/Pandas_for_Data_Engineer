import pandas as pd
import numpy as np
data=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day7a\Building_Permits.csv')
print(data.head())
#print(data.sample(10).to_string())# it gives all the data name in the stirng randaomly 
print("The shape of the data is :",data.shape)# shape diyou 
totalcells=np.product(data.shape)
print(" The total cells is ",totalcells) # total cells kati ota xa 


# missing values sum
missingcount=data.isnull().sum()
print(" THe miss count is :",missingcount)# it gives in columns 

# total, missing count in all data 
totalmissingValues=missingcount.sum()
print("THe total number of the missing count is :",totalmissingValues)

print("**************************")
missingPrecentage =(totalmissingValues/totalcells)*100
print("The missing  percentage of the data :",missingPrecentage) 



#  WORKING ON :
#  Street Number Suffix                      
# Zipcode 
print("**************************")
print(missingcount[['Street Number Suffix','Zipcode']])

print((missingcount['Street Number Suffix']/data.shape[0])*100)
print((missingcount['Zipcode']/data.shape[0])*100)