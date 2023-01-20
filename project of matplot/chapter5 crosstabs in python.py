import pandas as pd
import numpy as np
d={'name':['Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine','Alisa','Bobby','Catherine'],
   'Exam':['Semester1','Semester1','Semester1','Semester1','Semester1','Semester1','Semester2','Semester2','Semester2','Semester2','Semester2','Semester2'],
   'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science','Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Result':['Pass','pass','fail','pass','fail','pass','pass','fail','fail','pass','pass','fail']}
df=pd.DataFrame(d,columns=['name','Exam','Subject','Result'])
print(df)
print("using 2 way cross table in pyton pandas:")
print(pd.crosstab(df.Subject,df.Result,margins=True))
print("using 3 way crosstab in python pandas:")
print(pd.crosstab([df.Subject,df.Exam],df.Result,margins=True))
