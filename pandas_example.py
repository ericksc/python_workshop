import pandas as pd

list_dict = [{'points': 50, 'time': '5:00', 'year': 2010},
             {'points': 25, 'time': '6:00', 'month': "february"},
             {'points':90, 'time': '9:00', 'month': 'january'},
             {'points_h1':20, 'month': 'june'}]

def list_of_dict_to_dataframe(df):
    return pd.DataFrame(df)

def get_list_of_columns_on_dataframe(df):
    return list(df.columns.values)

df = list_of_dict_to_dataframe(list_dict)

my_list = get_list_of_columns_on_dataframe(df)

my_list.reverse()

sub_list = ['year', 'time', 'points_h1', 'points']

my_df = df[my_list]
sub_my_df = df[sub_list]

print('end')