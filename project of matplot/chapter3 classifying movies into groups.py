import pandas as pd
data=pd.read_csv('imdb_top_1000.csv')
def rating_group(rating):
    if rating>=7.5:
        return('Good')
    elif rating>=6.0:
        return('Average')
    else:
        return('Bad')
data['Rating']=data['IMDB_Rating'].apply(rating_group)
print(data['Rating'])
