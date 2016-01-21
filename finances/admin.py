# -*- coding: utf-8 -*-
from django.contrib import admin
from fh.admin import FhAdmin
from fh.filters import TaggitListFilter
from finances import models
from finances import forms


class PaymentAdmin(FhAdmin):
    """ Payment admin class """

    form = forms.PaymentForm
    list_display = (
        'get_tags_as_string', 'amount', 'date', 'is_debt', 'is_incoming',
        'created_at', 'created_by'
    )
    list_display_links = ('get_tags_as_string', 'amount',)
    list_filter = [TaggitListFilter, 'is_incoming', 'created_by', 'date', 'created_at', ]
    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ['tags', 'amount', 'is_incoming'],
        }),
        ('Date & user', {
            'classes': ('collapse',),
            'fields': ['date', 'created_by'],
        }),
    ]

    ordering = ['-date']
    search_fields = ['id']

    class Media:
        css = {
            'all': ('admin/css/finances.css',),
        }
        js = ('admin/js/finances.js',)


admin.site.register(models.Payment, PaymentAdmin)
