import pandas as pd
import numpy as np

df1 = pd.read_csv("file1.csv")
df1_orig = df1.copy()

df1 = pd.read_csv("file1.csv", dtype={"Id": 'int', "attr2": 'str'})


columns_list = list(df1_orig.columns.values)
df_zero = pd.DataFrame()
for item in columns_list:
    df_zero[item] = pd.Series([], dtype=object)

#df_zero.loc[0] = [1, 1, 1 , 1, 1]
for item in range(len(df1_orig.index)):
    df_zero.loc[item] = df1_orig.loc[item].astype(object)

list_dict = df1_orig.T.to_dict().values()

# Create a list to place the dictionary values in
list_dictionary = []

# For each key in the dictionary's Values,
for x in list_dict:
    # add the key to dictionaryValues
    list_dictionary.append(x)


my_list = ["Id","attr2"]
#df1_orig[my_list] = df1_orig[my_list].astype(object)
### :( :( :( :(
df1_edited = pd.DataFrame(list_dictionary, dtype=[("Id", int), ("attr2", object)])
print('end')

#[("Id", np.uint8), ("attr2", np.uint8)])len(df1_orig.index)