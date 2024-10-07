#!/usr/bin/env python3

import argparse


def generate_diff(file1, file2):
	return f"Comparing {file1} with {file2}."
 
 
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

if __name__ == "__main__":
	main()