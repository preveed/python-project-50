def make_stylish(diff, depth=0):
    indent = '    ' * depth
    lines = []
    for key, node in diff.items():
        lines.append(process_node(key, node, indent, depth))

    return '\n'.join(lines)


def process_node(key, node, indent, depth):
    node_type = node.get('type')
    if not node_type:
        raise ValueError(f"Node type is missing: {node}")

    node_processors = {
        "nested": process_nested,
        "added": process_added,
        "removed": process_removed,
        "unchanged": process_unchanged,
        "changed": process_changed,
    }

    return node_processors[node_type](key, node, indent, depth)


def process_nested(key, node, indent, depth):
    lines = []
    lines.append(f"{indent}    {key}: {{")
    lines.append(make_stylish(node['children'], depth + 1))
    lines.append(f"{indent}    }}")

    return '\n'.join(lines)


def process_added(key, node, indent, depth):
    return f"{indent}  + {key}: {format_value(node['value'], depth + 1)}"


def process_removed(key, node, indent, depth):
    return f"{indent}  - {key}: {format_value(node['value'], depth + 1)}"


def process_unchanged(key, node, indent, depth):
    return f"{indent}    {key}: {format_value(node['value'], depth + 1)}"


def process_changed(key, node, indent, depth):
    lines = []
    lines.append(
        f"{indent}  - {key}: {format_value(node['old_value'], depth + 1)}"
    )
    lines.append(
        f"{indent}  + {key}: {format_value(node['new_value'], depth + 1)}"
    )

    return '\n'.join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth)
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'

    return str(value)


def format_dict(value, depth):
    indent = '    ' * depth
    lines = ['{']
    for key, val in value.items():
        lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}")
    lines.append(f"{indent}}}")

    return '\n'.join(lines)
