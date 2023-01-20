import pandas as pd
import numpy as np
data=pd.DataFrame({'name':['jane','john','ashley','mike','emily','jack','catlin'],
                   'ctg':['A','A','C','B','B','C','B'],
                   'val':np.random.random(7).round(2),
                   'val2':np.random.randint(1,10,size=7)})
names=['john','jane','catlin','mike']
print(data[data.name.isin(names)])
