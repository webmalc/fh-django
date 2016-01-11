# -*- coding: utf-8 -*-
from django.contrib import admin
from fh.admin import FhAdmin
from tv import models


class ChannelAdmin(FhAdmin):
    """ Task admin class """

    list_display = ('title', 'category', 'is_enabled', 'is_favorite', 'created_at')
    list_display_links = ('title',)
    list_filter = ('category', 'is_enabled', 'created_at')
    fieldsets = (
        ('General', {
            'fields': ('title', 'category', 'code'),
        }),
        ('Settings', {
            'classes': ('collapse',),
            'fields': ['is_favorite', 'is_enabled', 'created_by'],
        }),
    )
    ordering = ('title',)
    search_fields = ('id', 'title', 'category')

    class Media:
        css = {
            'all': ('admin/css/tv.css',),
        }

admin.site.register(models.Channel, ChannelAdmin)
