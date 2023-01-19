import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
x=[]
y=[]
df=pd.read_csv("COVID19_globaldata.csv")
df1=df.groupby(' Country')
df1=df1.sum().sort_values(by='Deaths',ascending=False).head(10)
df1=df1.loc[:,'Deaths']
df1.index=['USA','Brazil','India','Mexico','UK','Italy','Peru','Spain','France','Iran']
print(df1)
df1.plot(kind='bar',figsize=(9,9))
plt.xlabel('Countries')
plt.ylabel('no. of deaths')
plt.legend()
plt.show()
        

