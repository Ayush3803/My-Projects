import pandas as pd
import numpy as np
data={'name':['Jason','Molly','Tina','Jake','Amy'],
      'age':[42,52,36,24,73],
      'preTestScore':[4,24,31,2,3],
      'postTestScore':[25,94,57,62,70]}

df=pd.DataFrame(data,columns=['name','age','preTestScore','postTestScore'])
print(df)
df['elderly']=np.where(df['age']>=50,'yes','no')
print(df)
