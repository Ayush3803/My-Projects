import pandas as pd
ddf=pd.read_csv("marksheet of students.csv")
ser=pd.Series(df['SNO,NAME,ROLLNO,CLASS,CITY,MATHS,ENGLISH,ACCOUNTS,ECONOMICS,TOTAL MARKS,PERCENTAGE'])
data=ser.head(13)
print(data)
