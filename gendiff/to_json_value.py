def to_json_value(value, flag=0):
    if value is False:
        return 'false'
    if value is True:
        return 'true'
    if value is None:
        return 'null'
    if flag == 0:
        return str(value)
    return repr(value)
