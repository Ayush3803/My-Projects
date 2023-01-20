import pandas as pd
data=pd.read_csv('imdb_top_1000.csv')
a=data.dropna()
print(a)
