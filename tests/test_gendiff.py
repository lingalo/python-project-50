#!/usr/bin/env python3
from gendiff import generate_diff as gen_dif, to_json_value as to_json


FILE_PATH1 = '/home/furia/python-project-50/tests/fixtures/file1.json'
FILE_PATH2 = '/home/furia/python-project-50/tests/fixtures/file2.json'
RIGHT = '/home/furia/python-project-50/tests/fixtures/diff_file1_file2'


def test_gen_dif():
    assert gen_dif(FILE_PATH1, FILE_PATH2) == open(RIGHT).read()


def test_to_json():
    assert to_json(None) == 'null'
