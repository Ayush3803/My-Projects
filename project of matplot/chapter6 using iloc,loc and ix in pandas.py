import pandas as pd
import numpy as np
d={'Name':['Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine'],
   'Exam':['Semester1','Semester1','Semester1','Semester1','Semester1','Semester1','Semester2','Semester2','Semester2','Semester2','Semester2','Semester2'],
   'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science','Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
df=pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
print(df)
print(df['Name'])
print(df[['Name','Score']])
print(df[:2])
print(df[df['Score']>70])
print(df[(df['Score']>70)&(df['Score']<85)])
print(df.ix[:,'Score'])
print(df.ix[3,2])
print(df.iloc[:2])
print(df.iloc[2:5])
print(df.iloc[2:])
print(df.iloc[:,:2])
print(df.iloc[:,[0,3]])
print(df.loc[[1,2,3,4,5],['Name','Score']])
print(df.loc[1])
