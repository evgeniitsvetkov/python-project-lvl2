#!/usr/bin/env python
from gendiff import parser


def make_tree(data1, data2):
    diff = []
    diff_keys = list(data1.keys() | data2.keys())
    diff_keys.sort()

    for key in diff_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        diff.append((key, value1, value2))

    return diff


def stylish(tree):
    diff = ['{']

    for node in tree:
        key, value1, value2 = node
        if value1 is None:
            diff.append('  + {}: {}'.format(key, value2))
        elif value2 is None:
            diff.append('  - {}: {}'.format(key, value1))
        elif value1 == value2:
            diff.append('    {}: {}'.format(key, value1))
        else:
            diff.append('  - {}: {}'.format(key, value1))
            diff.append('  + {}: {}'.format(key, value2))

    diff.append('}')

    return '\n'.join(diff)


def generate_diff(file_path1, file_path2):
    data1 = parser.load_data(file_path1)
    data2 = parser.load_data(file_path2)

    tree = make_tree(data1, data2)
    tree = stylish(tree)
    return tree
