#!/usr/bin/env python3

def stylish(diff, depth=0):  # noqa: C901, E501
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
                f"{indent}  + {key}: {format_value(node['value'], depth+1)}")
        elif node_type == "removed":
            lines.append(
                f"{indent}  - {key}: {format_value(node['value'], depth+1)}")
        elif node_type == "unchanged":
            lines.append(
                f"{indent}    {key}: {format_value(node['value'], depth+1)}"
            )
        elif node_type == "changed":
            lines.append(
                f"{indent}  - {key}: {format_value(node['old_value'], depth+1)}"
            )
            lines.append(
                f"{indent}  + {key}: {format_value(node['new_value'], depth+1)}"
            )

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
        return 'true' if value else 'false'
    else:
        return str(value)
