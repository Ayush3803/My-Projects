import pandas as pd
url = 'https://github.com/chrisalbon/sim_data/blob/005baa2a389458261276cf7bb13ff5fec56d84ac/data.json'
url1='json.json'
df=pd.read_json(url1,orient='integer')
a=df.head(10)
print(a)
