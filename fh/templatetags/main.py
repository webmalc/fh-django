from django import template

register = template.Library()


@register.filter()
def get_item(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    return None

