def make_plain(diff, path='', result=None):
    if result is None:
        result = []
    path += '.' if path else ''
    for key, node in diff.items():
        result.append(
            process_node(key, node, path)) if process_node(
                key, node, path) else None

    return '\n'.join(result)


def process_node(key, node, path):
    node_type = node.get('type')
    result = []
    if node_type == 'nested':
        result = process_nested(key, node, path)
    elif node_type == 'added':
        result = process_added(key, node, path)
    elif node_type == 'removed':
        result = process_removed(key, path)
    elif node_type == 'changed':
        result = process_changed(key, node, path)
    elif node_type == 'unchanged':
        result = None
    else:
        raise ValueError(f"Unexpected node type: {node_type}")

    return result


def process_nested(key, node, path):
    return make_plain(node['children'], path + key)


def process_added(key, node, path):
    value = format_value(node['value'])

    return f"Property '{path}{key}' was added with value: {value}"


def process_removed(key, path):
    return (f"Property '{path}{key}' was removed")


def process_changed(key, node, path):
    old_value = format_value(node['old_value'])
    new_value = format_value(node['new_value'])
    return (f"Property '{path}{key}' "
            f"was updated. From {old_value} to {new_value}")


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return f"'{str(value)}'"
