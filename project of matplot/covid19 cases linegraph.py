import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
x=[]
y=[]
df=pd.read_csv("COVID19_globaldata.csv")
df1=df.set_index(' Country')
case=[]
for index,row in df1.iterrows():
    if index=='India':
        case.append(row['Cases'])
days=list(range(1,279))        
plt.plot(days,case)
plt.title('India')
plt.xlabel('No. of days')
plt.ylabel('no. of cases')
plt.legend()
plt.show()
        

