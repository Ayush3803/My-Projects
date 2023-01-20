import pandas as pd
import numpy as np
data=np.array(['q','g','e','t','r','a','s','w','o','i','p','u','y'])
ser=pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
print(ser[16])
