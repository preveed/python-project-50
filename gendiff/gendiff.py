#!/usr/bin/env python3

from .fileparser import read_file


def generate_diff(file1, file2, format_name='stylish'):
    data1 = read_file(file1)
    data2 = read_file(file2)
    if data1 is None or data2 is None:
        return "Error in reading files."
    diff = build_diff(data1, data2)
    if format_name == 'stylish':
        return format_diff_with_braces(diff)
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


def stylish(diff, depth=0):
    indent = '    ' * depth
    lines = []
    for key, node in diff.items():
        if not isinstance(node, dict):
            raise ValueError(f"Unexpected node format: {node}")
        node_type = node['type']

        if node_type == "nested":
            lines.append(f"{indent}    {key}: {{")
            lines.append(stylish(node['children'], depth + 1))
            lines.append(f"{indent}    }}")  # Закрывающая скобка
        elif node_type == "added":
            lines.append(
                f"{indent}  + {key}: {format_value(node['value'], depth + 1)}")
        elif node_type == "removed":
            lines.append(
                f"{indent}  - {key}: {format_value(node['value'], depth + 1)}")
        elif node_type == "unchanged":
            lines.append(
                f"{indent}    {key}: {format_value(node['value'], depth + 1)}"
            )
        elif node_type == "changed":
            lines.append(
                f"{indent}  - {key}: {format_value(node['old_value'], depth + 1)}"
            )
            lines.append(
                f"{indent}  + {key}: {format_value(node['new_value'], depth + 1)}")

    return '\n'.join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = ['{']
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}")
        lines.append(f"{indent}}}")  # Закрывающая скобка для объекта
        return '\n'.join(lines)
    elif value is None:
        return 'null'  # Используем 'null' в стиле JavaScript
    elif isinstance(value, bool):
        return 'true' if value else 'false'  # Используем JavaScript-стиль для булевых значений
    else:
        return str(value)


def format_diff_with_braces(diff):
    """Функция оборачивает итоговый diff в фигурные скобки."""
    return f"{{\n{stylish(diff)}\n}}"
