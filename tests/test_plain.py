from pathlib import Path
from gendiff import file_to_dict, plain


flat_diff_path = Path(
    "tests", "fixtures", "json", "flat", "collected_diff_1_2.json"
)
tree_diff_path = Path(
    "tests", "fixtures", "json", "tree", "collected_diff_3_4.json"
)

plain_flat_path = Path(
    "tests", "fixtures", "json", "flat", "plain_diff_file1_file2"
)
plain_tree_path = Path(
    "tests", "fixtures", "json", "tree", "plain_diff_file3_file4"
)


def test_stylish():
    flat_diff = file_to_dict(flat_diff_path)
    tree_diff = file_to_dict(tree_diff_path)
    with open(plain_flat_path) as plain_flat:
        assert plain(flat_diff) == plain_flat.read()

    with open(plain_tree_path) as plain_tree:
        assert plain(tree_diff) == plain_tree.read()
