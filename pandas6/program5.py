import pandas as pd
import numpy as np
#How pandas upscales none
y=pd.Series(range(3),dtype=int)
print(y)
y[0]=None
print(y)