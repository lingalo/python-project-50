from gendiff import generate_diff as gen_dif, file_to_dict
from gendiff import stylish, plain, json_diff
from pathlib import Path


path_json1 = Path("tests", "fixtures", "json", "flat", "file1.json")
path_json2 = Path("tests", "fixtures", "json", "flat", "file2.json")

# +json:
flat_collected_diff = Path(
    "tests", "fixtures", "json", "flat", "collected_diff_1_2.json"
)
stylish_flat_path = Path(
    "tests", "fixtures", "json", "flat", "stylish_diff_file1_file2"
)
plain_flat_path = Path(
    "tests", "fixtures", "json", "flat", "plain_diff_file1_file2"
)

path_json3 = Path("tests", "fixtures", "json", "tree", "file3.json")
path_json4 = Path("tests", "fixtures", "json", "tree", "file4.json")

# +json:
tree_collected_diff = Path(
    "tests", "fixtures", "json", "tree", "collected_diff_3_4.json"
)
stylish_tree_path = Path(
    "tests", "fixtures", "json", "tree", "stylish_diff_file3_file4"
)
plain_tree_path = Path(
    "tests", "fixtures", "json", "tree", "plain_diff_file3_file4"
)


def test_generate_diff():
    flat_diff = file_to_dict(flat_collected_diff)
    tree_diff = file_to_dict(tree_collected_diff)

    # plain:
    assert gen_dif(path_json1, path_json2, 'plain') == plain(flat_diff)
    assert gen_dif(path_json3, path_json4, 'plain') == plain(tree_diff)

    # json:
    assert gen_dif(path_json1, path_json2, 'json') == json_diff(flat_diff)
    assert gen_dif(path_json3, path_json4, 'json') == json_diff(tree_diff)

    # stylish:
    assert gen_dif(path_json1, path_json2) == stylish(flat_diff)
    assert gen_dif(path_json3, path_json4, 'stylish') == stylish(tree_diff)
