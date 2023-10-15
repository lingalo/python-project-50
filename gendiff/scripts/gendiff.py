#!/usr/bin/env python3
import argparse
import json


SAME = '    '
FILE1 = '  - '
FILE2 = '  + '


def to_jsonf(value):
    if value is False:
        return 'false'
    if value is True:
        return 'true'
    if value is None:
        return 'null'
    return value


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    s_data = sorted(set(data1) | set(data2))

    result = ['{']
    for key in s_data:
        value1 = to_jsonf(data1.get(key, 'not_value'))
        value2 = to_jsonf(data2.get(key, 'not_value'))

        if value1 == value2:
            result.append(f'{SAME}{key}: {value1}')
        else:
            if value1 != 'not_value':
                result.append(f'{FILE1}{key}: {value1}')
            if value2 != 'not_value':
                result.append(f'{FILE2}{key}: {value2}')
    result.append('}')
    result = '\n'.join(result)
    print(result)
    return result


def gen():
    # print('hello')
    parser = argparse.ArgumentParser(
        prog='gendiff', 
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)

def main():
    gen()
    # generate_diff()


if __name__ == '__main__':
    main()