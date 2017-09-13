import pandas as pd
import numpy as np

raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [20, 19, 22, 21],
            'favorite_color': ['blue', 'red', 'yellow', "green"],
            'grade': [88, 92, 95, 70]}
df = pd.DataFrame(raw_data, index=['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])

df.drop(['Willard Morris', 'Spencer McDaniel'])

df.drop(df.index[0], inplace=True)



df.drop(df.index[:2], inplace=True)

df.drop(['age'], axis=1, inplace=True)
print('End Application')
