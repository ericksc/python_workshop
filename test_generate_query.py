from unittest import TestCase
import pandas as pd
import numpy as np
from random_objects import RandomString

import csv
import os

import re


class TestDBExecution(TestCase):


    def setUp(self):
        self.df = pd.DataFrame({'a': np.arange(3),
                           'b': RandomString(),
                           'c': RandomString()})
        pass

    def func(self, row):
        query = 'INSERT INTO TABLE VALUES ('
        values_list = []
        for name, values in row.iteritems():
            values_list.append(str(values))
        values = ', '.join(values_list)
        query += values + ')'
        return query

    def in_qoutes(self, input_string, quote_custom):
        return quote_custom + input_string + quote_custom

    def test_generate_insert_query(self):

        table_info_dict = {
            0: {'column_name': 'col_0', 'quote': "'"},
            1: {'column_name': 'col_1', 'quote': ""},
        }
        query_df = self.df.apply(self.func, axis=1)
        pass
