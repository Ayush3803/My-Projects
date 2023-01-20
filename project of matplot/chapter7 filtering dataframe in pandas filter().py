import pandas as pd
data=pd.read_csv("nba.csv")
df=data.filter(['Name','Age','College'])
print(df)
