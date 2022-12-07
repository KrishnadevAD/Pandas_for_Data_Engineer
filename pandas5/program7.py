# from Dictionary 
import pandas as pd
area_dict={'kathmandu':43345,'lalitpur':9982,'Bhaktapur':33344}
population_dict={'kathmandu':222143345,'lalitpur':213983,'Bhaktapur':33344}
areaSeries= pd.Series(area_dict)
populationSeries=pd.Series(population_dict) 
print(areaSeries)
print("***********")
print(populationSeries)
print("***********")
district=pd.DataFrame({'population':populationSeries,'area':areaSeries})
print(district)
