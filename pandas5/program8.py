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