from pathlib import Path
from gendiff import file_to_dict, stylish


flat_diff_path = Path(
    "tests", "fixtures", "json", "flat", "collected_diff_1_2.json"
    )
tree_diff_path = Path(
    "tests", "fixtures", "json", "tree", "collected_diff_3_4.json"
    )

stylish_flat_path = Path(
    "tests", "fixtures", "json", "flat", "stylish_diff_file1_file2"
    )
stylish_tree_path = Path(
    "tests", "fixtures", "json", "tree", "stylish_diff_file3_file4"
    )


def test_stylish():
    flat_diff = file_to_dict(flat_diff_path)
    tree_diff = file_to_dict(tree_diff_path)
    with open(stylish_flat_path) as stylish_flat:
        assert stylish(flat_diff) == stylish_flat.read()

    with open(stylish_tree_path) as stylish_tree:
        assert stylish(tree_diff) == stylish_tree.read()
