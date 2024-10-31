from .stylish import make_stylish
from .plain import make_plain
from .json import make_json


def format_diff(diff, format_name):
    if format_name == 'stylish':
        result = make_stylish(diff)
    elif format_name == 'plain':
        result = make_plain(diff)
    elif format_name == 'json':
        result = make_json(diff)
    else:
        result = "Unsupported format."

    return result
