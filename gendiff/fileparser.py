import json
import yaml


def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def parse_content(content, file_extension):
    if file_extension == 'json':
        return json.loads(content)
    elif file_extension in {'yaml', 'yml'}:
        return yaml.safe_load(content)
    else:
        raise ValueError("Unsupported file format")


def load_and_parse_file(file_path):
    content = load_file(file_path)
    file_extension = file_path.split('.')[-1]

    return parse_content(content, file_extension)
