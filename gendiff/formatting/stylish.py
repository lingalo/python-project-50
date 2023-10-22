from gendiff import to_json_value
# Принимает на вход словарь с собранным диффом, преобразует в строку


def stylish(diff, replacer='    ', spaces_count=1):  # noqa: C901

    def walk(node, depth=spaces_count):
        start = '{'
        border = replacer * depth
        border_ = replacer[-2:] + replacer * (depth - 1)
        end = (depth - spaces_count) * replacer + '}'

        if not isinstance(node, dict):
            return to_json_value(node)

        lines = [start]
        for key, value in node.items():
            slov = {'added': '+ ', 'deleted': '- ', 'unchanged': '  ', 'node': '  '}  # noqa: E501
            if not isinstance(value, dict) or 'diff' not in value:
                result = f'{border}{key}: {walk(value, depth + spaces_count)}'

            elif value['diff'] in slov:
                znak = slov[value['diff']]
                value = value["value"]
                result = f'{border_}{znak}{key}: {walk(value, depth + spaces_count)}'  # noqa: E501

            elif value.get('diff') == 'changed':
                value1 = value["value1"]
                value2 = value["value2"]
                result1 = f'{border_}- {key}: {walk(value1, depth + spaces_count)}'  # noqa: E501
                lines.append(result1)
                result = f'{border_}+ {key}: {walk(value2, depth + spaces_count)}'  # noqa: E501

            lines.append(result)

        lines.append(end)
        return '\n'.join(lines)
    return walk(diff)
