import pandas as pd
data=pd.read_csv('imdb_top_1000.csv')
data_indexed=pd.read_csv('imdb_top_1000.csv',index_col="Genre")
a=data.head()
print(a)
