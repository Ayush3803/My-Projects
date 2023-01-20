import pandas as pd
df=pd.read_csv("students.csv")
ser=pd.Series(df['NAME'])
data=ser.head(10)
print(data)
