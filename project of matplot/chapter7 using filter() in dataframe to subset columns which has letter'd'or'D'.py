import pandas as pd
data=pd.read_csv("nba.csv")
df=data.filter(regex='[dD]')
print(df)
