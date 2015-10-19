from django import template

register = template.Library()


@register.simple_tag
def url_replace(request=None, params=None, **kwargs):

    if not params and request:
        params = request.GET.copy()

    for key in kwargs:
        params[key] = kwargs[key]

    return params.urlencode()
