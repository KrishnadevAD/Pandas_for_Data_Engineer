import pandas as pd
#pandas as a dictionary
kri_dictionary = {'Krishna Dev':'July1',
                  'Adhikari ':'June1',
                  'Danuwar':'Dec1'}

print(kri_dictionary)
#creating a dictionary with that series
#While creating dictionary with series keys become index
myNewDictSeries = pd.Series(kri_dictionary)
print(" the new dictionary is  ",myNewDictSeries)
print(" the new index value is :",myNewDictSeries.index)