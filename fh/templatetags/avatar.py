from django import template
from avatar.conf import settings
from avatar.util import cache_result
from avatar.templatetags.avatar_tags import avatar_url


register = template.Library()


@register.simple_tag
def cached_avatar_url(user, size=settings.AVATAR_DEFAULT_SIZE):
    return cache_result(size)(avatar_url)(user, size)
