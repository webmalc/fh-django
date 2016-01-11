# -*- coding: utf-8 -*-
from django.contrib import admin
from fh.admin import FhAdmin
from fh.filters import TaggitListFilter
from tasks import models


class TaskAdmin(FhAdmin):
    """ Task admin class """

    list_display = (
        'title', 'get_tags_as_string', 'date', 'remind',
        'priority', 'get_assigned_to_as_string', 'is_completed'
    )
    list_display_links = ('title',)
    list_filter = (
        TaggitListFilter, 'assigned_to', 'priority', 'created_by', 'date'

    )
    fieldsets = (
        ('General', {
            'fields': ('title', 'comment', 'tags', 'priority', 'remind'),
        }),
        ('Date & user', {
            'classes': ('collapse',),
            'fields': ['date', 'assigned_to', 'created_by', 'is_completed'],
        }),
    )

    ordering = ('is_completed', '-priority', '-date')
    search_fields = ('id', 'title', 'comment')

    def make_completed(self, request, queryset):
        """
        Mark tasks as as completed
        :param request:
        :param queryset:
        :return: None
        """
        queryset.update(is_completed=True)
        self.message_user(request, "Tasks successfully marked as completed.")
    make_completed.short_description = "Complete selected tasks"

    def make_uncompleted(self, request, queryset):
        """
        Mark tasks as as open
        :param request:
        :param queryset:
        :return: None
        """
        queryset.update(is_completed=False)
        self.message_user(request, "Tasks successfully marked as open.")
    make_uncompleted.short_description = "Open selected tasks"

    actions = (make_completed, make_uncompleted)

    class Media:
        css = {
            'all': ('admin/css/tasks.css',),
        }
        js = ('admin/js/tasks.js',)


admin.site.register(models.Task, TaskAdmin)
