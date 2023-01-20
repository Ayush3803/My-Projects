import pandas as pd
import numpy as np
d={'Name':['Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine'],
   'Exam':['Semester1','Semester1','Semester1','Semester1','Semester1','Semester1','Semester2','Semester2','Semester2','Semester2','Semester2','Semester2'],
   'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science','Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
df=pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
print(df)
df1=df.set_index(['Exam','Subject'])
print(df1)
print(df1.swaplevel('Subject','Exam'))
df1=df.set_index(['Exam','Subject'],drop=False)
print(df1)
