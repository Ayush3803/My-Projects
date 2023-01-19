import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("COVID19_globaldata.csv")
df1=df.set_index(" Country")
df1_india=df1.loc["India"]
df1_usa=df1.loc['United States of America']
df1_brazil=df1.loc['Brazil']
df1_russia=df1.loc['Russian Federation']
days=list(range(1,279))
days1=list(range(1,278))
print(df1_india)
print(df1_brazil)
print(df1_usa)
print(df1_russia)
plt.plot(days,df1_india['Cases'],label='India')
plt.plot(days,df1_brazil['Cases'],label='Brazil')
plt.plot(days1,df1_russia['Cases'],label='Russia')
plt.plot(days,df1_usa['Cases'],label='USA')
plt.legend()
plt.title("Top 4 countries")
plt.xlabel("Time period(days)")
plt.ylabel("No. of cases")
plt.show()
