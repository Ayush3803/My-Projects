import pandas as pd
df=pd.read_csv("a.csv")
ser=pd.Series(df['Name'])
data=ser.head(10)
data
