import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
x=[]
y=[]
df=pd.read_csv("COVID19_globaldata.csv")
df1=df.groupby(' Country')
df1=df1.sum().sort_values(by='Cases',ascending=False).head(5)
print(df1)
df1.plot(kind='pie',y='Cases',labels=df1.index,startangle=90,explode=(0.05,0.04,0.06,0.08,0.03))
plt.legend()
plt.title('Top 5 Countries')
plt.show()
        

