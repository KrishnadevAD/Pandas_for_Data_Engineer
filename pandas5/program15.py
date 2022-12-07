import pandas as pd
area_dict={'kathmandu':43345,'lalitpur':9982,'Bhaktapur':33344}# making colums 
population_dict={'kathmandu':222143345,'lalitpur':213983,'Bhaktapurs':33344}# changing Bhaktapurs 
area= pd.Series(area_dict)
pop=pd.Series(population_dict) 
print(area)
print("***********")
print(pop)
print("***********")
district=pd.DataFrame({'pop':pop,'area':area})# making colums new 
print(district)
print(district.area)# column excess garda chai area gareko jastai garne na bhaye problem aauxa hai 
print(district['area'])# mathi pop lee error aauna sakxa so acces like this --> ['area']
# modify  dict
district['density']=district['pop']/district['area']
print(district)
print(district.iloc[:2,:1]) #by index 
print(district.loc['lalitpur':'Bhaktapur','density':])
