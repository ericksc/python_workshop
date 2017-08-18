

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

def re_org_list_based_on_list(my_list, reference_list):
    list_copied = my_list.copy()
    empty_list = [None for i in range(len(list_copied))]

    for index, item in enumerate(list_copied):
        empty_list[index] = reference_list.index(item)

    empty_list.sort()

    for index, item in enumerate(empty_list):
        list_copied[index] = reference_list[item]
    return list_copied

print('end')