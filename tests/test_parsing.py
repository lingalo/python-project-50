from gendiff import collect_diff, file_to_dict
from pathlib import Path


flat_path1 = Path("tests", "fixtures", "json", "flat", "file1.json")
flat_path2 = Path("tests", "fixtures", "json", "flat", "file2.json")
tree_path3 = Path("tests", "fixtures", "json", "tree", "file3.json")
tree_path4 = Path("tests", "fixtures", "json", "tree", "file4.json")

flat_diff_path = Path(
    "tests", "fixtures", "json", "flat", "collected_diff_1_2.json"
    )
tree_diff_path = Path(
    "tests", "fixtures", "json", "tree", "collected_diff_3_4.json"
    )


def test_collect_diff():
    flat_data1, flat_data2 = file_to_dict(flat_path1), file_to_dict(flat_path2)
    tree_data3, tree_data4 = file_to_dict(tree_path3), file_to_dict(tree_path4)

    flat_diff = file_to_dict(flat_diff_path)
    tree_diff = file_to_dict(tree_diff_path)

    assert collect_diff(flat_data1, flat_data2) == flat_diff
    assert collect_diff(tree_data3, tree_data4) == tree_diff
