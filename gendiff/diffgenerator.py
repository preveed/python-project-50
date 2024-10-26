from .fileparser import load_and_parse_file
from .formatters.stylish import make_stylish
from .formatters.plain import make_plain
from .formatters.json import make_json


def generate_diff(file1, file2, format_name='stylish'):
    data1 = load_and_parse_file(file1)
    data2 = load_and_parse_file(file2)
    if data1 is None or data2 is None:
        return "Error in reading files."

    diff = build_diff(data1, data2)
    return format_diff(diff, format_name)


def format_diff(diff, format_name):
    if format_name == 'stylish':
        result = f"{{\n{make_stylish(diff)}\n}}"
    elif format_name == 'plain':
        result = make_plain(diff)
    elif format_name == 'json':
        result = make_json(diff)
    else:
        result = "Unsupported format."

    return result


def build_diff(data1, data2):
    diff = {}
    all_keys = sorted(data1.keys() | data2.keys())
    for key in all_keys:
        diff[key] = get_diff_entry(key, data1, data2)

    return diff


def get_diff_entry(key, data1, data2):
    if key in data1 and key in data2:
        return handle_in_both(key, data1, data2)
    elif key in data1:
        return handle_removed(key, data1)
    else:
        return handle_added(key, data2)


def handle_in_both(key, data1, data2):
    value1, value2 = data1[key], data2[key]
    if isinstance(value1, dict) and isinstance(value2, dict):
        return {'type': 'nested',
                'children': build_diff(value1, value2)
                }
    elif value1 == value2:
        return {'type': 'unchanged', 'value': value1}
    else:
        return {'type': 'changed', 'old_value': value1, 'new_value': value2}


def handle_removed(key, data1):
    return {'type': 'removed', 'value': data1[key]}


def handle_added(key, data2):
    return {'type': 'added', 'value': data2[key]}
