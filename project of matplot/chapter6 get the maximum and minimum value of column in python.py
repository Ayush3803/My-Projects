import pandas as pd
import numpy as np
d={'Name':['Alisa','Bobby','Jodha','Jack','Raghu','Catherine','Alisa','Bobby','Kumar','Alisa','Alex','Catherine'],
   'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
   'Score':[85,63,55,74,31,77,85,63,42,62,89,77]}
df=pd.DataFrame(d,columns=['Name','Age','Score'])
print(df)
print(df['Age'].max())
print(df['Name'].max())
print(df.min())
print(df['Age'].min())
print(df['Name'].min())
