#!/usr/bin/env Python3

import json
import yaml
import argparse
from gendiff.diff_generator import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        type=str,
        help='First configuration file')
    parser.add_argument(
        'second_file',
        type=str,
        help='Second configuration file')
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='Set format of output',
        default='stylish')

    args = parser.parse_args()
    first_data = args.first_file
    second_data = args.second_file

    try:
        result = generate_diff(first_data, second_data, args.format)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Error: Invalid file format. {e}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(result)


if __name__ == '__main__':
    main()
