import numpy as np 
import pandas as pd 
import os
universityTown=[]
filepath=os.path.join(os.getcwd(),r"C:\Users\DELL\Desktop\data science DWIT\day11\university_towns.txt")
fileOpen=open(filepath,"r")
fileRead=fileOpen.readlines()

for lines in fileRead:
    print(lines)
for lines in fileRead:
    if '[edit]' in lines:
        print(lines)
    print(lines)
