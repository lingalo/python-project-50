from gendiff import to_json_value
# На вход попадает дифф уже готовый


def plain(node):  # noqa: C901
    result = []
    result_konez = []

    def rec(node, path=''):
        if not isinstance(node, dict):
            if path not in result:
                result.append(path)
                return (path, to_json_value(node, type='repr'))
            return to_json_value(node, type='repr')

        for key, value_n in node.items():
            slov = {'added': '+ ', 'deleted': '- ', 'node': '  '}

            if not isinstance(value_n, dict):
                return (path, '[complex value]')

            elif 'diff' not in value_n:
                return (path, '[complex value]')

            elif value_n['diff'] in slov:
                value = value_n.get('value')
                cor = rec(value, '.'.join((path, key)))

                if isinstance(cor, tuple):
                    p, v = cor
                    p = p[1:]
                    if value_n['diff'] == 'added':
                        result_konez.append(f"Property {repr(p)} was added with value: {v}")  # noqa: E501
                    if value_n['diff'] == 'deleted':
                        result_konez.append(f"Property '{p}' was removed")

            elif value_n.get('diff') == 'changed':
                value1 = value_n.get('value1')
                value2 = value_n.get('value2')

                cor1 = rec(value1, '.'.join((path, key)))
                cor2 = rec(value2, '.'.join((path, key)))

                if isinstance(cor1, tuple) and isinstance(cor2, tuple):
                    p, v1 = cor1
                    v2 = cor2[1]
                    p = p[1:]
                    result_konez.append(f"Property '{p}' was updated. From {v1} to {v2}")  # noqa: E501

                elif isinstance(cor1, tuple):
                    p, v1 = cor1
                    v2 = cor2
                    p = p[1:]
                    result_konez.append(f"Property '{p}' was updated. From {v1} to {v2}")  # noqa: E501

                elif isinstance(cor2, tuple):
                    v1 = cor1
                    p, v2 = cor2
                    p = p[1:]
                    result_konez.append(f"Property '{p}' was updated. From {v1} to {v2}")  # noqa: E501
    rec(node)
    return '\n'.join(result_konez)
