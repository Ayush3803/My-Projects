import pandas as pd
df=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']}
                ,index=[0,1,2,3])
print(df)
s=pd.Series(['X0','X1','X2','X3'],index=['A','B','C','D'])
result=df.append(s,ignore_index=True)
print(result)
dicts=[{'A':1,'B':2,'C':3,'X':4},
       {'A':5,'B':6,'C':7,'Y':8}]
result=df.append(dicts,ignore_index=True)
print(result)
