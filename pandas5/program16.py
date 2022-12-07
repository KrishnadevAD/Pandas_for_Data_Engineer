import pandas as pd 
dataframe=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(dataframe)
print("******************************")
daraframe2=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(daraframe2)
print("******************************")
dataframe3=pd.DataFrame({'Krishnadev adhaikari ': ['I liked it.', 'It was awful.'], 
              'ashmita adhikari ': ['Pretty good.', 'Beautiful ']},
             index=['code 1 ', 'code 2 '])
print(dataframe3)