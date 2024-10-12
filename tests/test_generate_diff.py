from gendiff.gendiff import generate_diff


def test_generate_diff():

    test_cases = [
        (
            "tests/file1.json",
            "tests/file2.json",
            """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}""",
        ),
        (
            "tests/file1.yaml",
            "tests/file2.yaml",
            """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}""",
        ),
    ]

    for file1, file2, expected_diff in test_cases:
        result = generate_diff(file1, file2).strip()
        assert result == expected_diff.strip()


def test_generate_diff_file_identical():

    test_cases = [
        (
            "tests/file1.json",
            "tests/file1.json",
            """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}""",
        ),
        (
            "tests/file1.yaml",
            "tests/file1.yaml",
            """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}""",
        ),
    ]
    for file1, file2, expected_diff_identical in test_cases:
        result = generate_diff(file1, file2).strip()
        assert result == expected_diff_identical.strip()


def test_generate_diff_one_file_empty():
    test_cases = [
        (
            "tests/file1.json",
            "tests/file-empty.json",
            """{
  - follow: False
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}""",
        ),
        (
            "tests/file1.yaml",
            "tests/empty-file.yaml",
            """{
  - follow: False
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}""",
        ),
    ]

    for file1, file2, expected_diff_one_empty in test_cases:
        result = generate_diff(file1, file2).strip()
        assert result == expected_diff_one_empty.strip()
