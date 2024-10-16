#!/usr/bin/env Python3

import argparse

from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        type=str,
        help='First configuration file'
    )
    parser.add_argument(
        'second_file',
        type=str,
        help='Second configuration file'
    )
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output',
        default='stylish'
    )

    args = parser.parse_args()

    # Вызываем функцию генерации диффа
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
