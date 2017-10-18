from collections import defaultdict
from contextlib import contextmanager
import pickle

@contextmanager
def ignored(*exceptions):
    try:
        print('inside ignored')
        yield
    except exceptions as e:
        print('ignored')
        pass


@contextmanager
def process_error(*exceptions):
    try:
        print('inside process_error')
        yield
    except pickle.UnpicklingError as e:
        send_email()
        pass
    except (AttributeError, EOFError, ImportError, IndexError) as e:
        send_email()
        pass
    except Exception as e:
        send_email()
        pass

def send_email():
    print('sending email')
    pass

item = defaultdict(str)

obj = dict()
with ignored(Exception):
    print('first')
    item['a'] = obj.get(2).get(3)

print(item['a'])

obj[2] = dict()
obj[2][3] = 4

with ignored(Exception):
    print('second')
    item['a'] = obj.get(2).get(3)

print(item['a'])

obj = dict()
with process_error(Exception):
    print('third')
    item['a'] = obj.get(2).get(3)

obj[2] = dict()
obj[2][3] = 4
with process_error(Exception):
    print('four')
    item['a'] = obj.get(2).get(3)

print(item['a'])