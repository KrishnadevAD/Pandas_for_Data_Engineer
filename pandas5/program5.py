import pandas as pd
x=pd.Series([1,2,3,4,5],index=[2,4,5,6,8])
print(x[4])# it print the index =4 th value that is 4 
print(x[2:4])
#  x[2:4] --->It prints the series from 2nd posititon to 3rd positon
# that means it includes initial 2 and final= 4 -1 =3 rd series elements 
# and prints the index of its series position that is  5 and 6 