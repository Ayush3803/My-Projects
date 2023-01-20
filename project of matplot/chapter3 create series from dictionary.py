import pandas as pd
dict_fruits={'orange':80,
             'apples':210,
             'bananas':50,
             'grapes':90,
             'watermelon':70}
fruits=pd.Series(dict_fruits)
print("fruits and prices:\n",fruits)
