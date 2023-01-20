import pandas as pd
import numpy as np
df=pd.DataFrame()
raw_data={'student_name':['Miller','Jacobson','Ali','Milner','Cooze','Jacon','Ryaner','Sone','Slone','Piger','Riana','Ali'],
          'test_score':[76,88,84,67,53,96,64,91,77,73,52,np.NaN]}
df=pd.DataFrame(raw_data,columns=['student_name','test_score'])
grades=[]
for row in df['test_score']:
    if row>95:
        grades.append('A')
    elif row>90:
        grades.append('A-')
    elif row>85:
        grades.append('B')
    elif row>80:
        grades.append('B-')
    elif row>75:
        grades.append('C')
    elif row>70:
        grades.append('C-')
    elif row>65:
         grades.append('D')
    elif row>60:
         grades.append('D-')
    else:
        grades.append('Failed')
df['grades']=grades
print(df)
