from pathlib import Path
from json import dumps
from gendiff import file_to_dict, json_diff


flat_diff_path = Path(
    "tests", "fixtures", "json", "flat", "collected_diff_1_2.json"
    )
tree_diff_path = Path(
    "tests", "fixtures", "json", "tree", "collected_diff_3_4.json"
    )


def test_json_diff():
    flat_diff = file_to_dict(flat_diff_path)
    tree_diff = file_to_dict(tree_diff_path)

    assert json_diff(flat_diff) == dumps(flat_diff, indent=2)
    assert json_diff(tree_diff) == dumps(tree_diff, indent=2)
