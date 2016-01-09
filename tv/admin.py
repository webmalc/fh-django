# -*- coding: utf-8 -*-
from django.contrib import admin
from fh.admin import FhAdmin
from tv import models


class ChannelAdmin(FhAdmin):
    """ Task admin class """

    list_display = ('title', 'category', 'is_enabled', 'created_at')
    list_display_links = ('title',)
    list_filter = ('category', 'is_enabled', 'created_at')
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('title', 'category', 'code'),
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-add'),
            'fields': ['is_enabled', 'created_by'],
        }),
    )
    suit_form_tabs = (('general', 'General'), ('add', 'Settings'))
    ordering = ('title',)
    search_fields = ('id', 'title', 'category')

    @staticmethod
    def suit_row_attributes(obj):
        if not obj.is_enabled:
            return {'class': 'error'}

    @staticmethod
    def suit_cell_attributes(obj, column):
        if column == 'is_enabled':
            return {'class': 'text-center'}


admin.site.register(models.Channel, ChannelAdmin)
