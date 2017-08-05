import pandas as pd

list_dict = [{'points': 50, 'time': '5:00', 'year': 2010},
             {'points': 25, 'time': '6:00', 'month': "february"},
             {'points':90, 'time': '9:00', 'month': 'january'},
             {'points_h1':20, 'month': 'june'}]

def list_of_dict_to_dataframe(df):
    return pd.DataFrame(df)

df = list_of_dict_to_dataframe(list_dict)

print('end')