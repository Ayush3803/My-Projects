import pandas as pd
data=pd.read_csv('imdb_top_1000.csv')
a=[data.dropna(axis=1),
   data.dropna(axis=0,thresh=6)]
print(a)

