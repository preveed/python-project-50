import json
from gendiff.gendiff import generate_diff


def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def test_generate_diff():
    file1 = 'tests/file1.json'
    file2 = 'tests/file2.json'

    expected_diff = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

    result = generate_diff(file1, file2)

    assert result == expected_diff


def test_generate_diff_file_identical():
    file1 = 'tests/file1.json'
    file2 = 'tests/file1.json'

    expected_diff_identical = '''{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''

    result = generate_diff(file1, file2)

    assert result == expected_diff_identical


def test_generate_diff_one_file_empty():
    file1 = 'tests/file1.json'
    file2 = 'tests/file-empty.json'

    expected_diff_one_empty = '''{
  - follow: False
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''

    result = generate_diff(file1, file2)

    assert result == expected_diff_one_empty
