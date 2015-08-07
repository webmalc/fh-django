import json
import decimal


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError


def get(data, x='x', y='y'):
    data.insert(0, [x, y])
    return json.dumps(data, default=decimal_default)
