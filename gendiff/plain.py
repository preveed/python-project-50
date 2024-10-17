#!/usr/bin/env python3

def plain(diff, path='', result=None):  # noqa: C901, E501
    if result is None:
        result = []

    path += '.' if path else ''
    for key, node in diff.items():
        if node['type'] == 'nested':
            plain(node['children'], path + key, result)
        elif node['type'] == 'added':
            value = format_value(node['value'])
            result.append(
                f"Property '{path}{key}' was added with value: {value}"
            )
        elif node['type'] == 'removed':
            result.append(f"Property '{path}{key}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            result.append(f"Property '{path}{key}' "
                          f"was updated. From {old_value} to {new_value}")

    return '\n'.join(result)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'  # Используем 'null' в стиле JavaScript
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return f"'{str(value)}'"
