#!/usr/bin/env python3
import argparse

def gendiff():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()


def main():
    print(gendiff())


if __name__ == '__main__':
    main()
