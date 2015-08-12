import decimal
import datetime


def get(data, x='x', y='y'):
    data.insert(0, (x, y))
    output = '['

    for entry in data:
        if isinstance(entry[0], datetime.date):
            output += '[new Date(%s), %s],' % (entry[0].strftime('%Y, %m, %d'), entry[1])
        elif isinstance(entry[1], (decimal.Decimal, int, float)):
            output += '["%s", %s],' % entry
        else:
            output += '["%s", "%s"],' % entry

    output += ']'
    return output
