# Data cleaning 
# Births csv
import pandas as pd
import numpy as np
mydata=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day10\births.csv')
print(mydata)
print(mydata.head())


# Questions ::::
#  1.) Extract the  data of only the Year == 1969 
#  2.) Find maximum  birth of the Male in 1969 
#  3.) Find maximum birth of the Femalle in 1969 
#  4.) Find the maximum  number of birth  in 1969  


#(SIMPLE way )== सजिलो तरिका
print("#########################################")
# find MAXIMUM BIRTH in 1969 

data1=mydata.loc[(mydata["year"]==1969)]
print(data1)


# Male 
# #print(" the maximum birth  is  :",data1.max())
print("#########################################")
data2=data1.loc[(data1['gender']=='M')]
print(data2)
print("#########################################")
data21=pd.Series(data2["births"])
print(data21) 
max1=data21.max()
print(" the max birth of male in 1969 is ",max1)


# female 
print("#########################################")
data3=data1.loc[(data1['gender']=='F')]
print(data3)
data31=pd.Series(data3["births"])
print(data31)
max2=data31.max()
print(" the max birth of Female in 1969 is ",max2)

total= max1+max2
print(" the maximum bith in 1969 is ",total)