import pandas as pd
import numpy as np

list_dict = [{'points': 50, 'time': '5:00', 'year': 2010},
             {'points': 25, 'time': '6:00', 'month': "february"},
             {'points':90, 'time': '9:00', 'month': 'january'},
             {'points_h1':20, 'month': 'june'}]

def remove_element_on_list(element, object_list):
    if element in object_list:
        object_list.remove(element)

def remove_element_of_list(element, object_list):
    copied_list = object_list.copy()
    if element in copied_list:
        copied_list.remove(element)
    return copied_list


def list_of_dict_to_dataframe(df):
    return pd.DataFrame(df)

def get_list_of_columns_on_dataframe(df):
    return list(df.columns.values)

def delete_column_of_dataframe(df, column_name):
    return df.drop(column_name, 1)



def delete_column_on_dataframe(df, column_name):
    df.drop(column_name, axis=1, inplace=True)

def get_sub_dataframe(df, my_list):
    return df[my_list]

df = list_of_dict_to_dataframe(list_dict)

my_list = get_list_of_columns_on_dataframe(df)

my_list.reverse()

my_df = df[my_list]
remove_element_on_list('year', my_list)


sub_my_df = get_sub_dataframe(df, my_list)


df = pd.DataFrame({'a': np.arange(3), 'b': np.random.rand(3), 'c': np.random.rand(3)})

my_col_list = get_list_of_columns_on_dataframe(df)

def func(row):
    return row['a'] + row['b']

df.apply(func, axis=1)

print('end')