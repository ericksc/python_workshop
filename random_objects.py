import random
import string
import pandas as pd
import numpy as np

class RandomString(str):
    low = 1
    high = 10
    def __init__(self, size = None):
        if size is None:
            self.size =  random.randint(self.low, self.high)
        else:
            self.size = size
    def __str__(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(self.size))
    def __repr__(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(self.size))


class RandomList(str):
    low = 1
    high = 10
    def __init__(self, size = None):
        self.my_list = []
        if size is None:
            self.size =  random.randint(self.low, self.high)
        else:
            self.size = size

    def __repr__(self):
        return (self.my_list.append(RandomString) for _ in range(self.size))

class RandomDataFrame(str):
    def bla(self):
        df = pd.DataFrame({'a': np.arange(3),
                           'b': np.random.rand(3)})

