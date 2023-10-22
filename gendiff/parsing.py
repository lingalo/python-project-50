def collect_diff(data1, data2):  # noqa: C901
    diff = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data1:
            diff[key] = {'diff': 'added', 'value': value2}

        elif key not in data2:
            diff[key] = {'diff': 'deleted', 'value': value1}

        elif value1 == value2:
            diff[key] = {'diff': 'unchanged', 'value': value1}

        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {'diff': 'node', 'value': collect_diff(value1, value2)}

        elif value1 != value2:
            diff[key] = {'diff': 'changed', 'value1': value1, 'value2': value2}

    return diff


# Вот какая странность: если я убираю elif и оставляю else,
# то сложность равна 6 и линтер пропускает
# Подумать над тем, чтобы строчку diff[key] = {'diff': 'added', 'value': value2}
#  вынести в конец цикла и оставить только
# elif isinstance(value1, dict) and isinstance(value2, dict):
#   diff[key] = {'diff': 'node', 'value': collect_diff(value1, value2)}
# это условие
# и возможно это
# elif value1 != value2:
# # else:
#     diff[key] = {'diff': 'changed', 'value1': value1, 'value2': value2}

# value присваивать первое или второе значение
# а для дифф сделать отдельный словарь
# короче я хз, подумаю позже
