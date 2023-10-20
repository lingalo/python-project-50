#!/usr/bin/env python3
from gendiff import to_json_value as to_json
from gendiff import generate_diff as gen_dif
from pathlib import Path


from gendiff.parsing import file_to_dict
from tests.fixtures.collected_differences import diff1, diff2
from gendiff.collect_diff import collect_diff


from gendiff.stylish import stylish


from gendiff.plain import plain


file_path_json1 = Path("tests", "fixtures", "json", "flat", "file1.json")
file_pat_json2 = Path("tests", "fixtures", "json", "flat", "file2.json")
file_pat_yaml1 = Path("tests", "fixtures", "yaml", "flat", "file1.yml")
file_pat_yaml2 = Path("tests", "fixtures", "yaml", "flat", "file2.yaml")


file_path_tree_json1 = Path("tests", "fixtures", "json", "tree", "file1.json")
file_path_tree_json2 = Path("tests", "fixtures", "json", "tree", "file2.json")
file_path_tree_json3 = Path("tests", "fixtures", "json", "tree", "file3.json")
file_path_tree_json4 = Path("tests", "fixtures", "json", "tree", "file4.json")


file_path_tree_yaml1 = Path("tests", "fixtures", "yaml", "tree", "file1.yaml")
file_path_tree_yaml2 = Path("tests", "fixtures", "yaml", "tree", "file2.yaml")
file_path_tree_yaml3 = Path("tests", "fixtures", "yaml", "tree", "file3.yaml")
file_path_tree_yaml4 = Path("tests", "fixtures", "yaml", "tree", "file4.yaml")


def test_gen_dif():
    RIGHT = Path("tests", "fixtures", "diff_file1_file2")
    with open(RIGHT) as right_file:
        right = right_file.read()
        assert gen_dif(file_path_json1, file_pat_json2) == right
        assert gen_dif(file_pat_yaml1, file_pat_yaml2) == right
        assert gen_dif(file_pat_yaml1, file_pat_json2) == right


# Интересует, собираюсь переписывать
def test_to_json():
    assert to_json(None) == 'null'


# Нужно написать тесты ещё на плоские структуры
def test_collect_diff():
    json_tree_data1 = file_to_dict(file_path_tree_json1)
    json_tree_data2 = file_to_dict(file_path_tree_json2)
    json_tree_data3 = file_to_dict(file_path_tree_json3)
    json_tree_data4 = file_to_dict(file_path_tree_json4)

    yaml_tree_data1 = file_to_dict(file_path_tree_yaml1)
    yaml_tree_data2 = file_to_dict(file_path_tree_yaml2)
    yaml_tree_data3 = file_to_dict(file_path_tree_yaml3)
    yaml_tree_data4 = file_to_dict(file_path_tree_yaml4)

    # Три теста всего, по аналогии с первым, пять путей
    assert collect_diff(json_tree_data1, json_tree_data2) == diff1
    assert collect_diff(yaml_tree_data1, yaml_tree_data2) == diff1

    assert collect_diff(json_tree_data3, json_tree_data4) == diff2
    assert collect_diff(yaml_tree_data3, yaml_tree_data4) == diff2

    assert collect_diff(json_tree_data1, yaml_tree_data2) == diff1
    assert collect_diff(yaml_tree_data3, json_tree_data4) == diff2


def test_stylish():
    RIGHT = Path("tests", "fixtures", "diff_file3_file4")
    with open(RIGHT) as right_file:
        right = right_file.read()
        assert stylish(diff2) == right


def test_plain():
    RIGHT = Path("tests", "fixtures", "diff_file3_file4_plain")
    with open(RIGHT) as right_file:
        right = right_file.read()
        assert plain(diff2) == right
