def make_json(diff, depth=0):
    lines = ['{']
    indent = '    ' * depth

    for idx, (key, node) in enumerate(diff.items()):
        node_type = node['type']
        inner_indent = '    ' * (depth + 1)

        if node_type == 'nested':
            children = node['children']
            lines.append(f'{inner_indent}"{key}": {{')
            lines.append(f'{inner_indent}    "type": "{node_type}",')
            lines.append(
                f'{inner_indent}    "children": '
                f'{make_json(children, depth + 2)}')
            lines.append(f'{inner_indent}}}')
        elif node_type in ('added', 'unchanged', 'removed'):
            value = node['value']
            lines.append(f'{inner_indent}"{key}": {{')
            lines.append(f'{inner_indent}    "type": "{node_type}",')
            lines.append(
                f'{inner_indent}    "value": {format_value(value, depth + 1)}')
            lines.append(f'{inner_indent}}}')
        elif node_type == 'changed':
            old_value = node['old_value']
            new_value = node['new_value']
            lines.append(f'{inner_indent}"{key}": {{')
            lines.append(f'{inner_indent}    "type": "{node_type}",')
            lines.append(
                f'{inner_indent}    "old_value": '
                f'{format_value(old_value, depth + 1)},')
            lines.append(
                f'{inner_indent}    "new_value": '
                f'{format_value(new_value, depth + 1)}')
            lines.append(f'{inner_indent}}}')

        if idx < len(diff) - 1:
            lines[-1] += ','

    lines.append(f'{indent}}}')
    return '\n'.join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth)
    elif value is None:
        return format_null()
    elif isinstance(value, bool):
        return format_bool(value)
    elif isinstance(value, (int, float)):
        return format_number(value)
    else:
        return format_string(value)


def format_dict(value, depth):
    indent = '    ' * depth
    lines = ['{']
    for idx, (key, val) in enumerate(value.items()):
        lines.append(f'{indent}    "{key}": {format_value(val, depth + 1)}')
        if idx < len(value) - 1:
            lines[-1] += ','
    lines.append(f'{indent}}}')
    return '\n'.join(lines)


def format_null():
    return 'null'


def format_bool(value):
    return 'true' if value else 'false'


def format_number(value):
    return str(value)


def format_string(value):
    return f'"{str(value)}"'
