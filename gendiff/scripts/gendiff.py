#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    # Если параметр --format указали явно или не указали вовсе:
    if args.format == 'stylish' or not args.format:
        print(generate_diff(args.first_file, args.second_file))
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, 'plain'))
    if args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, 'json'))


def main():
    parse()


if __name__ == '__main__':
    main()
