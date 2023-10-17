#!/usr/bin/env python3
from gendiff import generate_diff as gen_dif, to_json_value as to_json
import pathlib


FILE_PATH1 = pathlib.Path("tests", "fixtures", "json_format", "file1.json")
FILE_PATH2 = pathlib.Path("tests", "fixtures", "json_format", "file2.json")


FILE_PATH1_YAML = pathlib.Path("tests", "fixtures", "yaml_format", "file1.yml")
FILE_PATH2_YAML = pathlib.Path("tests", "fixtures", "yaml_format", "file2.yaml")


RIGHT = pathlib.Path("tests", "fixtures", "diff_file1_file2")


def test_gen_dif():
    with open(RIGHT) as right_file:
        right = right_file.read()
        assert gen_dif(FILE_PATH1, FILE_PATH2) == right
        assert gen_dif(FILE_PATH1_YAML, FILE_PATH2_YAML) == right
        assert gen_dif(FILE_PATH1_YAML, FILE_PATH2) == right


def test_to_json():
    assert to_json(None) == 'null'
