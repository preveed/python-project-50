#!/usr/bin/env python3

import argparse
import json


def generate_diff(file1, file2):
    first_file = json.load(open(file1))
    second_file = json.load(open(file2))
    return f"Comparing {first_file} with {second_file}."
