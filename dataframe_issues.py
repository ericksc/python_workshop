import pandas as pd
import numpy as np

list_dict = [{'points': 50, 'time': '5:00', 'year': 2010},
             {'points': 25, 'time': '6:00', 'month': "february"},
             {'points':90, 'time': '9:00', 'month': 'january'},
             {'points':None, 'points_h1':20, 'month': 'june'}]


df = pd.DataFrame(list_dict)

df_zero = pd.DataFrame()
df_zero['month'] = pd.Series([], dtype=object)
df_zero['points'] = pd.Series([], dtype=object)
df_zero['points_h1'] = pd.Series([], dtype=object)
df_zero['time'] = pd.Series([], dtype=object)
df_zero['year'] = pd.Series([], dtype=object)
df_zero.loc[0] = [1, 1, 1 , 1, 1]
df_zero.loc[1] = [1, "one", None, None, None]
df_zero.loc[2] = [1, None, "one", None, None]
df_zero.loc[3] = [1, None, None, "one", None]
df_zero.loc[4] = ["one", None, None,  None, None]

df_one = pd.DataFrame()
df_one['month'] = pd.Series([], dtype=object)
df_one['points'] = pd.Series([], dtype=object)
df_one['points_h1'] = pd.Series([], dtype=object)
df_one['time'] = pd.Series([], dtype=object)
df_one['year'] = pd.Series([], dtype=object)

df_one = df_one.append(list_dict)


list_col =  ['month', 'points', 'points_h1', 'time', 'year']

print('end')