#!/usr/bin/env Python3

import argparse
from gendiff.gendiff import generate_diff



def main():
	parser = argparse.ArgumentParser(
    	description='Generate difference between two configuration files.'
	)
	parser.add_argument(
        	'file1',
        	type=str,
        	help='First configuration file'
	)
	parser.add_argument(
        	'file2',
        	type=str,
        	help='Second configuration file'
	)
    
	args = parser.parse_args()

    # Вызываем функцию генерации диффа
	result = generate_diff(args.file1, args.file2)
	print(result)


if __name__ == '__main__':
    main()