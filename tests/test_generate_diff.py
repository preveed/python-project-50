# flake8: noqa W291

from gendiff.gendiff import generate_diff


def test_generate_diff():  # noqa: W291

    test_cases = [
        (
            "tests/file1.json",
            "tests/file2.json",
            "tests/test-stylish-diff-files",
            "stylish"
        ),
        (
            "tests/file1.yaml",
            "tests/file2.yaml",
            "tests/test-stylish-diff-files",
            "stylish"
        ),
        (
            "tests/file1.json",
            "tests/file2.json",
            "tests/test-plain-diff",
            "plain"
        ),

    ]
    
    for file1, file2, diff, format_name in test_cases:
        result = generate_diff(file1, file2, format_name)
        with open(diff, 'r') as file:
            expected_diff = file.read()
        assert result == expected_diff



def test_generate_diff_file_identical():  # noqa: W291

    test_cases = [
        (
            "tests/file1.json",
            "tests/file1.json",
            "tests/test-stylish-identical",
            "stylish",
        ),
        (
            "tests/file1.yaml",
            "tests/file1.yaml",
            "tests/test-stylish-identical",
            "stylish",
        ),
        (
            "tests/file1.json",
            "tests/file1.json",
            "tests/test-plain-identical",
            "plain",
        ),
        (
            "tests/file1.yaml",
            "tests/file1.yaml",
            "tests/test-plain-identical",
            "plain",
        )
    ]
    for file1, file2, diff, format_name in test_cases:
        result = generate_diff(file1, file2, format_name)
        with open(diff, 'r') as file:
            expected_diff = file.read()
        assert result == expected_diff


def test_generate_diff_one_file_empty():  # noqa: W291

    test_cases = [
        (
            "tests/file1.json",
            "tests/file-empty.json",
            "tests/test-stylish-one-file-empty",
            "stylish",
        ),
        (
            "tests/file1.yaml",
            "tests/file-empty.yaml",
            "tests/test-stylish-one-file-empty",
            "stylish",
        ),
        (
            "tests/file1.json",
            "tests/file-empty.json",
            "tests/test-plain-one-file-empty",
            "plain",
        ),
        (
            "tests/file1.yaml",
            "tests/file-empty.yaml",
            "tests/test-plain-one-file-empty",
            "plain",
        ),
    ]
    for file1, file2, diff, format_name in test_cases:
        result = generate_diff(file1, file2, format_name)
        with open(diff, 'r') as file:
            expected_diff = file.read()
        assert result == expected_diff
