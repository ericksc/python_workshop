

my_list = [
    'hugo',
    'paco',
    'luis'
]


full_list = [
    'jeff',
    'luis',
    'adam',
    'tom',
    'hugo',
    'john',
    'paco',
    'sam'
]


empty_list = [None for i in range(len(my_list))]

for index, item in enumerate(my_list):
    empty_list[index] = full_list.index(item)


empty_list.sort()

for index, item in enumerate(empty_list):
    my_list[index] = full_list[item]

print('end')