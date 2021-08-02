#!/usr/bin/env python
import json


def load_data_from_json(path_to_file):
    with open(path_to_file) as f:
        data = json.load(f)
        return data


def generate_diff(file_path1, file_path2):
    data1 = load_data_from_json(file_path1)
    data2 = load_data_from_json(file_path2)

    diff = ['{']
    diff_keys = list(data1.keys() | data2.keys())
    diff_keys.sort()
    for key in diff_keys:
        if key not in data1:
            diff.append('  + {}: {}'.format(key, data2[key]))
        elif key not in data2:
            diff.append('  - {}: {}'.format(key, data1[key]))
        elif data1[key] == data2[key]:
            diff.append('    {}: {}'.format(key, data1[key]))
        else:
            diff.append('  - {}: {}'.format(key, data1[key]))
            diff.append('  + {}: {}'.format(key, data2[key]))
    diff.append('}')
    return '\n'.join(diff)
