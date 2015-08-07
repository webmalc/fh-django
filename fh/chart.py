import json


def get(data, x='x', y='y'):
    data.insert(0, [x, y])
    return json.dumps(data)
