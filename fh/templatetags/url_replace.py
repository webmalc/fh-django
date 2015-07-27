from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, **kwargs):

    dict_ = request.GET.copy()
    for key in kwargs:
        dict_[key] = kwargs[key]

    return dict_.urlencode()
