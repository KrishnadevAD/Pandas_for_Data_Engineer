import pandas as pd
import numpy as np
mydata=pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day9\president_heights_practice.csv')
print(mydata)

# name maa null bhako value hatako hai suru maa
mydata.dropna(subset=['name'],inplace=True)
print("my data ",mydata.size)

print(mydata['Measured Date'].dtype)
mydata['Measured Date']=pd.to_datetime(mydata['Measured Date'])
print(mydata['Measured Date'].dtype)
medianheight = np.nanmedian(mydata['height(cm)'])
print(medianheight)


# maxthreshold = 200
# minthreshold = 50
# for x in mydata.index:
#     if mydata.loc[([x,'height(cm)']>=maxthreshold) or (mydata.loc[x,'height(cm)']=<minthreshold)]:
#         mydata.loc[x,'height(cm)']=medianheight

# print(medianheight)
#changing height greater than 200 and less than median height
for x in mydata.index:
    if mydata.loc[x,"height(cm)"] >= 200 or mydata.loc[x,"height(cm)"] < 1:
        mydata.loc[x,"height(cm)"] = medianheight
print("changing height greater than 200 and less than median height",mydata['height(cm)'])

