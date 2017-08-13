import pandas as pd
import numpy as np

list_dict = [{'points': '50', 'time': '5:00', 'year': '2010'},
             {'points': '25', 'time': '6:00', 'month': "february"},
             {'points': '90', 'time': '9:00', 'month': None},
             {'points_h1':'20', 'month': 'june'}]

df_1 = pd.DataFrame(list_dict)


df_1.app

df_2 = pd.DataFrame()
df_2["str_1"] = pd.Series([], dtype=str)
df_2["str"] = pd.Series([], dtype=str)
df_2.loc[0] = ['0', "zero"]
print(df_2)

df_2.loc[1] = [1, None]
print(df_2)

print('end')

