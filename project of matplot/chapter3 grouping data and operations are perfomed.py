import pandas as pd
data=pd.read_csv('imdb_top_1000.csv')
a=data.groupby('Director')[['IMDB_Rating']].mean().head()
print(a)
