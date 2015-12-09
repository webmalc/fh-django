# -*- coding: utf-8 -*-
from django.contrib import admin
from fh.admin import FhAdmin
from fh.filters import TaggitListFilter
from tasks import models
from tasks import forms


class TaskAdmin(FhAdmin):
    """ Task admin class """

    list_display = (
        'get_tags_as_string', 'title'
    )
    list_display_links = ('get_tags_as_string', 'title',)
    list_filter = [TaggitListFilter, 'created_by', 'date', 'created_at', ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('title', 'comment', 'tags', 'priority', 'remind'),
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-add'),
            'fields': ['date', 'assigned_to', 'created_by'],
        }),
    ]
    suit_form_tabs = (('general', 'General'), ('add', 'Date & user'))
    ordering = ['-date']
    search_fields = ('id', 'title')

    class Media:
        css = {
            'all': ('admin/css/task.css',),
        }
        js = ('admin/js/task.js',)


admin.site.register(models.Task, TaskAdmin)
