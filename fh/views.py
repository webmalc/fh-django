from django.http import JsonResponse
from taggit.models import Tag


def tags(request, query=None):
    """
    JSON tags list
    :param request:
    :param query:
    :return: JsonResponse
    """
    items = Tag.objects
    if query:
        items = items.filter(name__contains=query.strip())
    data = [tag.name for tag in items.order_by('name').all()]
    return JsonResponse(data, safe=False)
