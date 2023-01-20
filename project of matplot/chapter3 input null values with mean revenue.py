import pandas as pd
data=pd.read_csv('imdb_top_1000.csv')
a=data['No of Votes'].mean()
b=data['No of Votes'].fillna(a,inplace=True)
print(b)
