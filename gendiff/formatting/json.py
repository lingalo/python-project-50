from json import dumps


def json_diff(diff):
    return dumps(diff, indent=2)
