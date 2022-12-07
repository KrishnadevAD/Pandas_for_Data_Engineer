# data frame as dictinary
import pandas as pd
# 2 ota series area r population banaune 
area = pd.Series({'California': 423967, 'Texas': 695662,
                   'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})
print("The data is :",data)
print("THe area is :",data.area)
print(" data area is ",data["area"])
print("data population is ",data.pop)
print(data['pop'])

# #we can also modify data
data['density'] = data['area']/data['pop']
print(data)
#
# #Transforming rows and columns
print(data.T)
#
#Data frame as 2d
print(data.area)
#
#tin oota row first two column
print(data.iloc[:3,:2])

#florida to pop
print(data.loc[:'Florida',:'pop'])