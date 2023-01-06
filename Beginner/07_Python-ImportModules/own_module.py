print('Imported my own_module...')

test = 'Test String'


def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


import sys

print(sys.path)