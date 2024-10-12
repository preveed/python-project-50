#!/usr/bin/env python3

from .fileparser import read_file


def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)
    if data1 is None or data2 is None:
        return "Error in reading files."
    return build_diff(data1, data2)


def handle_reading_error(data1, data2):
    if data1 is None or data2 is None:
        return "Error in reading files."
    elif data1 is None:
        return "Error in reading file first file."
    else:
        return "Error in reading file second file."


def build_diff(data1, data2):
    """Создает различия между двумя словарями."""
    diff = []
    all_keys = sorted(data1.keys() | data2.keys())

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"    {key}: {data1[key]}")
            else:
                diff.append(f"  - {key}: {data1[key]}")
                diff.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            diff.append(f"  - {key}: {data1[key]}")
        else:
            diff.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff) + "\n}"
