import json
import yaml
from yaml.loader import SafeLoader
from pathlib import Path
from gendiff.stylish import stylish
from gendiff.plain import plain
from gendiff.collect_diff import collect_diff
from gendiff.json import json_diff


SAME = '    '
FILE1 = '  - '
FILE2 = '  + '


INSTRUCTIONS = {
    '.yaml': lambda file_: yaml.load(file_, Loader=SafeLoader),
    '.yml': lambda file_: yaml.load(file_, Loader=SafeLoader),
    '.json': lambda file_: json.load(file_)
    }


def file_to_dict(file_path):
    file_form = Path(file_path).suffix
    with open(file_path) as file:
        return INSTRUCTIONS[file_form](file)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = file_to_dict(file_path1), file_to_dict(file_path2)

    diff = collect_diff(data1, data2)
    if format_name == 'plain':
        return plain(diff)
    if format_name == 'json':
        return json_diff(diff)
    return stylish(diff)
