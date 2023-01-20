import pandas as pd
import numpy as np
d={'Name':pd.Series(['Alisa','Bobby','Catherine','Madonna','Rocky','Sebastian','Jaqluine','Rahul','David','Andrew','Ajay','Teresa']),
   'Age':pd.Series([26,27,25,24,3127,25,33,42,32,51,47]),
   'Score':pd.Series([89,87,67,55,47,72,76,79,44,92,99,69])}
df=pd.DataFrame(d)
print(df)
print(df.mode())
print(df.mode(axis=0))
print(df.loc[:,"Score"].mode())

