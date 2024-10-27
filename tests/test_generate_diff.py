import pytest
from gendiff.diffgenerator import generate_diff


@pytest.mark.parametrize("file1, file2, expected, format_name", [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/test-stylish-diff-files',
     'stylish'),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/test-stylish-diff-files',
     'stylish'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/test-plain-diff',
     'plain'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/test-plain-diff',
     'plain'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/test-json-diff.json',
     'json'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/test-json-diff.json',
     'json'),
    # identical files
    ('tests/fixtures/file1.json',
     'tests/fixtures/file1.json',
     'tests/fixtures/test-stylish-identical',
     'stylish'),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file1.yaml',
     'tests/fixtures/test-stylish-identical',
     'stylish'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file1.json',
     'tests/fixtures/test-plain-identical',
     'plain'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file1.json',
     'tests/fixtures/test-plain-identical',
     'plain'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file1.json',
     'tests/fixtures/test-json-identical.json',
     'json'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file1.json',
     'tests/fixtures/test-json-identical.json',
     'json'),
    # empty file
    ('tests/fixtures/file1.json',
     'tests/fixtures/file-empty.json',
     'tests/fixtures/test-stylish-one-file-empty',
     'stylish'),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file-empty.yaml',
     'tests/fixtures/test-stylish-one-file-empty',
     'stylish'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file-empty.json',
     'tests/fixtures/test-plain-one-file-empty',
     'plain'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file-empty.json',
     'tests/fixtures/test-plain-one-file-empty',
     'plain'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file-empty.json',
     'tests/fixtures/test-json-one-empty.json',
     'json'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file-empty.json',
     'tests/fixtures/test-json-one-empty.json',
     'json'),
])
def test_generate_diff(file1, file2, expected, format_name):
    result = generate_diff(file1, file2, format_name)
    assert isinstance(result, str)
    with open(expected, 'r') as file:
        if format_name == 'json':
            import json
            result = json.loads(result)
            expected_output = json.load(file)
        else:
            expected_output = file.read()

    assert str(result) == str(expected_output)
