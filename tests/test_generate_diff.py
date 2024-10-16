# flake8: noqa W291

from gendiff.gendiff import generate_diff


def test_generate_diff():  # noqa: W291

    test_cases = [
        (
            "tests/file1.json",
            "tests/file2.json",
            """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}""",
        ),
        (
            "tests/file1.yaml",
            "tests/file2.yaml",
            """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}""",
        ),
    ]
    for file1, file2, expected_diff in test_cases:
        result = generate_diff(file1, file2)
        assert result == expected_diff


def test_generate_diff_file_identical():  # noqa: W291

    test_cases = [
        (
            "tests/file1.json",
            "tests/file1.json",
            """{
    common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            doge: {
                wow: 
            }
            key: value
        }
    }
    group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
    group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}""",
        ),
        (
            "tests/file1.yaml",
            "tests/file1.yaml",
            """{
    common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            doge: {
                wow: 
            }
            key: value
        }
    }
    group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
    group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}""",
        ),
    ]
    for file1, file2, expected_diff in test_cases:
        result = generate_diff(file1, file2)
        assert result == expected_diff


def test_generate_diff_one_file_empty():  # noqa: W291
    test_cases = [
        (
            "tests/file1.json",
            "tests/file-empty.json",
            """{
  - common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            key: value
            doge: {
                wow: 
            }
        }
    }
  - group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}""",
        ),
        (
            "tests/file1.yaml",
            "tests/file-empty.yaml",
            """{
  - common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            key: value
            doge: {
                wow: 
            }
        }
    }
  - group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}""",
        ),
    ]

    for file1, file2, expected_diff_one_empty in test_cases:
        result = generate_diff(file1, file2)
        assert result == expected_diff_one_empty
