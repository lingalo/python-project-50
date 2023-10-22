#!/usr/bin/env python3
from gendiff import stylish, plain, collect_diff, json_diff, file_to_dict
import argparse


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = file_to_dict(file_path1), file_to_dict(file_path2)

    diff = collect_diff(data1, data2)
    if format_name == 'plain':
        return plain(diff)
    if format_name == 'json':
        return json_diff(diff)
    return stylish(diff)


def parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output'
    )

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
