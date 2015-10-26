from django import template

register = template.Library()


def pager(context, link):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    page_obj = context['page_obj']
    paginator = context['paginator']
    request = context['request']
    adjacent_pages = 1

    start_page = max(page_obj.number - adjacent_pages, 1)
    if start_page <= adjacent_pages:
        start_page = 1

    end_page = page_obj.number + adjacent_pages + 1
    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages + 1

    page_numbers = [n for n in range(start_page, end_page) if n <= paginator.num_pages]

    return {
        'page_obj': page_obj,
        'paginator': paginator,
        'link': link,
        'params': request.GET.copy(),
        'page_numbers': page_numbers,
        'show_first': 1 not in page_numbers,
        'show_last': paginator.num_pages not in page_numbers,
    }

register.inclusion_tag('pager/pager.html', takes_context=True)(pager)
