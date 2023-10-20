diff1 = {'hell': {'diff': 'added', 'value': 'boy'},
 'hello': {'diff': 'unchanged', 'value': 'world'},
 'is': {'diff': 'changed', 'value1': False, 'value2': True},
 'nested': {'diff': 'node',
             'value': {'cg': {'diff': 'deleted', 'value': 6},
                       'count': {'diff': 'changed',
                                 'value1': 5,
                                 'value2': {'cg': 6}}}}}



diff2 = {
    'common': {'diff': 'node',
               'value': {'follow': {'diff': 'added', 'value': False},
                   'setting1': {'diff': 'unchanged', 'value': 'Value 1'},
                   'setting2': {'diff': 'deleted', 'value': 200},
                   'setting3': {'diff': 'changed', 'value1': True, 'value2': None},
                   'setting4': {'diff': 'added', 'value': 'blah blah'},
                   'setting5': {'diff': 'added', 'value': {'key5': 'value5'}},
                   'setting6': {'diff': 'node', 
                        'value': {'doge': {'diff': 'node', 
                            'value': {'wow': {'diff': 'changed', 'value1': '', 'value2': 'so much'}
                                }},
                            'key': {'diff': 'unchanged', 'value': 'value'},
                            'ops': {'diff': 'added', 'value': 'vops'}
                            }}
    }},
    'group1': {'diff': 'node',
               'value': {'baz': {'diff': 'changed', 'value1': 'bas', 'value2': 'bars'},
                   'foo': {'diff': 'unchanged', 'value': 'bar'},
                   'nest': {'diff': 'changed', 
                            'value1': {'key': "value"},
                            'value2': 'str'},
    }},
    'group2': {'diff': 'deleted', 
               'value': {'abc': 12345,
                   'deep': {'id': 45}
    }},
    'group3': {'diff': 'added', 
               'value': { 'deep': {
                   'id': {"number": 45}},
                   'fee': 100500
    }}
}

# ctrl + shift + L: писать сразу во всех строках с одинаковыми именами
# Нужно переименовать value1 в value, а value2 во что-нибудь другое... (тогда код в форматировании можно будет ещё немного сократить)
# Подумать о том, чтобы добавить children
