import time

def speed_test(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        for x in range(5000):
            results = func(*args, **kwargs)
        t2 = time.time()
        print('{} took {} ms'.format(func.__name__, (t2-t1)*1000.0))
        return results
    return wrapper

@speed_test
def compare_bitwise(x, y):
    set_x = frozenset(x)
    set_y = frozenset(y)
    return set_x & set_y

@speed_test
def compare_listcomp(x, y):
    return [i for i, j in zip(x, y) if i == j]

@speed_test
def compare_intersect(x, y):
    return frozenset(x).intersection(y)

@speed_test
def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]

# Comparing short lists
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
compare_bitwise(a, b)
compare_listcomp(a, b)
compare_intersect(a, b)
returnNotMatches(a, b)

# Comparing longer lists
import random
a = random.sample(range(100000), 10000)
b = random.sample(range(100000), 10000)
compare_bitwise(a, b)
compare_listcomp(a, b)
compare_intersect(a, b)
returnNotMatches(a, b)

print('end')