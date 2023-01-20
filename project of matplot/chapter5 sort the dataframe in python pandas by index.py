import pandas as pd
import numpy as np
d={'Name':['Alisa','Bobby','Catherine','Madonna','Rocky','Sebastian','Jaqluine','Rahul','David','Andrew','Ajay','Teresa'],
   'Age':[26,27,25,24,31,27,25,33,42,32,51,47],
   'Score':[89,87,67,55,47,72,76,79,44,92,99,69]}
df=pd.DataFrame(d)
df=df.reindex([1,4,6,2,3,5,9,8,0,7,11,10])
print(df)
df1=df.sort_index()
print(df1)
df2=df.sort_index(ascending=0)
print(df2)
