def json(diff, depth=0):  # noqa: C901, E501
    lines = ['{']
    indent = '    ' * depth
    
    for idx, (key, node) in enumerate(diff.items()):
        node_type = node['type']
        inner_indent = '    ' * (depth + 1)
        
        if node_type == 'nested':
            children = node['children']
            lines.append(f'{inner_indent}"{key}": {{')
            lines.append(f'{inner_indent}    "type": "{node_type}",')
            lines.append(f'{inner_indent}    "children": {json(children, depth + 2)}')
            lines.append(f'{inner_indent}}}')
        elif node_type in ('added', 'unchanged', 'removed'):
            value = node['value']
            lines.append(f'{inner_indent}"{key}": {{')
            lines.append(f'{inner_indent}    "type": "{node_type}",')
            lines.append(f'{inner_indent}    "value": {format_value(value, depth + 1)}')
            lines.append(f'{inner_indent}}}')
        elif node_type == 'changed':
            old_value = node['old_value']
            new_value = node['new_value']
            lines.append(f'{inner_indent}"{key}": {{')
            lines.append(f'{inner_indent}    "type": "{node_type}",')
            lines.append(f'{inner_indent}    "old_value": {format_value(old_value, depth + 1)},')
            lines.append(f'{inner_indent}    "new_value": {format_value(new_value, depth + 1)}')
            lines.append(f'{inner_indent}}}')
        
        # Добавляем запятую, если это не последний элемент
        if idx < len(diff) - 1:
            lines[-1] += ','

    lines.append(f'{indent}}}')
    return '\n'.join(lines)

def format_value(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        lines = ['{']
        for idx, (key, val) in enumerate(value.items()):
            lines.append(f'{indent}    "{key}": {format_value(val, depth + 1)}')
            if idx < len(value) - 1:
                lines[-1] += ','  # Добавляем запятую между элементами
        lines.append(f'{indent}}}')
        return '\n'.join(lines)
    elif value is None:
        return 'null'  # Используем 'null' в стиле JavaScript
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return f'"{str(value)}"'
