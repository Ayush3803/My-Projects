import pandas as pd
import numpy as np
d={'Name':['Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine'],
   'Exam':['Semester1','Semester1','Semester1','Semester1','Semester1','Semester1','Semester2','Semester2','Semester2','Semester2','Semester2','Semester2'],
   'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science','Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
df=pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
a=df[['Name','Score']]
print(a)
b=df[:2]
print(b)
c=df[df['Score']>70]
print(c)
d=df[(df['Score']>70)&(df['Score']<85)]
print(d)
