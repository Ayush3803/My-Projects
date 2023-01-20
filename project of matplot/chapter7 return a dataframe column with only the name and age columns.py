import pandas as pd
data={"Name":['Sally','Mary','John'],
      "Age":[50,40,30],
      "Qualified":[True,False,False]}
df=pd.DataFrame(data)
df1=df.filter(items=["Name","Age"])
print(df1)
