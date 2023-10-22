# Здесь происходит преобразование данных
import json
import yaml
from yaml.loader import SafeLoader
from pathlib import Path


INSTRUCTIONS = {
    '.yaml': lambda file_: yaml.load(file_, Loader=SafeLoader),
    '.yml': lambda file_: yaml.load(file_, Loader=SafeLoader),
    '.json': lambda file_: json.load(file_)
    }


# Могу ли я обойтись без импорта Path?
# Рефакторинг строки 18
def file_to_dict(file_path):
    file_form = Path(file_path).suffix
    with open(file_path) as file:
        return INSTRUCTIONS[file_form](file)


def to_json_value(value, type='str'):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if type == 'repr':
        return repr(value)
    return str(value)
