import json
import decimal
import datetime


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError('Invalid json format.')


def get(data, x='x', y='y'):
    data.insert(0, [x, y])
    return json.dumps(data, default=decimal_default)
