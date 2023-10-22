from pathlib import Path
from gendiff import to_json_value, file_to_dict


def test_to_json_value():
    assert to_json_value(None) == 'null'
    assert to_json_value(True) == 'true'
    assert to_json_value(120) == str(120)
    assert to_json_value('value', type='repr') == repr('value')
    assert to_json_value('', type='repr') == repr('')


def test_file_to_dict():
    # Прокинуть через фикстуру? И добавить инициализацию через функ.
    case_json = Path("tests", "fixtures", "json", "tree", "file1.json")
    case_yaml = Path("tests", "fixtures", "yaml", "tree", "file1.yaml")
    case_yml = Path("tests", "fixtures", "yaml", "flat", "file1.yml")

    right_yaml_json = {
        "hello": "world",
        "is": False,
        "nested": {"cg": 6, "count": 5}
    }
    right_yml = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }

    assert file_to_dict(case_json) == right_yaml_json
    assert file_to_dict(case_yaml) == right_yaml_json
    assert file_to_dict(case_yml) == right_yml
