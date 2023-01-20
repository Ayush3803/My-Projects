import pandas as pd
height=pd.Series([5.3,6.2,5.8,5.0,5.5],index=['person1','person2','person3','person4','person5'])
weight=pd.Series([65,89,75,60,59],index=['person1','person2','person3','person4','person5'])
df_person=pd.DataFrame({'height':height,'weight':weight})
print("the person table datails are:\n",df_person)
