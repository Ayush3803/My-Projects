import pandas as pd
import numpy as np
data=pd.DataFrame({'name':['jane','john','ashley','mike','emily','jack','catlin'],
                   'ctg':['A','A','C','B','B','C','B'],
                   'val':np.random.random(7).round(2),
                   'val2':np.random.randint(1,10,size=7)})
print(data[data.val>0.5])
print("\n")
print(data[data.name>'jane'])
print("\n")
print(data[(data.val>0.5)&(data.val2==1)])
print("\n")
print(data[(data.val<0.5)&(data.val2==7)])

