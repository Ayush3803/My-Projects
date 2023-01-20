import pandas as pd
df=pd.read_csv("players.csv")
ser=pd.Series(df['PLAYER NAME'])
data=ser.head(10)
print(data)
