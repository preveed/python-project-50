#!/usr/bin/env python3

import argparse
import json


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON.")
        return None
        


def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)
    if data1 is None or data2 is None:
        return "Error in reading files."
    
    diff_result = []
    
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))

    for key in all_keys:
        if key not in data2:
            diff_result.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            diff_result.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff_result.append(f"  - {key}: {data1[key]}")
            diff_result.append(f"  + {key}: {data2[key]}")
        else:
            diff_result.append(f"    {key}: {data1[key]}")

    return "{\n" + "\n".join(diff_result) + "\n}"
