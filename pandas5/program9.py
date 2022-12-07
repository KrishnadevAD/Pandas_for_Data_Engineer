import pandas as pd
area_dict={'kathmandu':43345,'lalitpur':9982,'Bhaktapur':33344}# making colums 
population_dict={'kathmandu':222143345,'lalitpur':213983,'Bhaktapurs':33344}# changing Bhaktapurs 
areaSeries= pd.Series(area_dict)
populationSeries=pd.Series(population_dict) 
print(areaSeries)
print("***********")
print(populationSeries)
print("***********")
district=pd.DataFrame({'population':populationSeries,'area':areaSeries})# making colums new 
print(district)
print(district.columns)# its an attribute so not columns()
print(district.head())
print(district.head(2))
print(district.tail())
print(district.tail(2))
print(district.info())# all the information of the dataframe
print(district.shape)


