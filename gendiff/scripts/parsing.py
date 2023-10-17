import json
import yaml
from yaml.loader import SafeLoader
from pathlib import Path


SAME = '    '
FILE1 = '  - '
FILE2 = '  + '


INSTRUCTIONS = {
    '.yaml': lambda file_: yaml.load(file_, Loader=SafeLoader),
    '.yml': lambda file_: yaml.load(file_, Loader=SafeLoader),
    '.json': lambda file_: json.load(file_)
    }


def file_to_dict(file_path1, file_path2):
    file_form1 = Path(file_path1).suffix
    file_form2 = Path(file_path2).suffix
    with open(file_path1) as file_1, open(file_path2) as file_2:
        return (
                INSTRUCTIONS[file_form1](file_1),
                INSTRUCTIONS[file_form2](file_2),
                )


def to_json_value(value):
    if value is False:
        return 'false'
    if value is True:
        return 'true'
    if value is None:
        return 'null'
    return value


def generate_diff(file_path1, file_path2):
    data1, data2 = file_to_dict(file_path1, file_path2)
    s_data = sorted(set(data1) | set(data2))

    result = ['{']
    for key in s_data:
        value1 = to_json_value(data1.get(key, 'not_value'))
        value2 = to_json_value(data2.get(key, 'not_value'))

        if value1 == value2:
            result.append(f'{SAME}{key}: {value1}')
        else:
            if value1 != 'not_value':
                result.append(f'{FILE1}{key}: {value1}')
            if value2 != 'not_value':
                result.append(f'{FILE2}{key}: {value2}')
    result.append('}')
    return '\n'.join(result)
