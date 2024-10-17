#!/usr/bin/env python3

from .fileparser import read_file
from .stylish import stylish
from .plain import plain


def generate_diff(file1, file2, format_name='stylish'):
    data1 = read_file(file1)
    data2 = read_file(file2)
    if data1 is None or data2 is None:
        return "Error in reading files."
    diff = build_diff(data1, data2)
    if format_name == 'stylish':
        return f"{{\n{stylish(diff)}\n}}"
    elif format_name == 'plain':
        return plain(diff)
    else:
        return "Unsupported format."


def build_diff(data1, data2):
    """Создает различия между двумя словарями."""
    diff = {}
    all_keys = sorted(data1.keys() | data2.keys())
    for key in all_keys:
        if key in data1 and key in data2:
            value1, value2 = data1[key], data2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff[key] = {
                    'type': 'nested',
                    'children': build_diff(value1, value2)
                }
            elif value1 == value2:
                diff[key] = {'type': 'unchanged', 'value': value1}
            else:
                diff[key] = {'type': 'changed', 'old_value': value1,
                                                'new_value': value2}
        elif key in data1:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        else:
            diff[key] = {'type': 'added', 'value': data2[key]}
    return diff
