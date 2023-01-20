import pandas as pd
data=pd.read_csv('imdb_top_1000.csv')
a=data.drop('Runtime',axis=1).head()
print(a)
