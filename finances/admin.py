# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from fh.admin import FhAdmin
from fh.filters import TaggitListFilter
from finances import models
from finances import forms


class PaymentChangeList(ChangeList):
    """ Payment change list """

    def __init__(self, request, model, list_display, list_display_links,
                 list_filter, date_hierarchy, search_fields, list_select_related,
                 list_per_page, list_max_show_all, list_editable, model_admin):
        self.total_in = 0
        self.total_out = 0
        self.total_balance = 0

        super(PaymentChangeList, self).__init__(request, model, list_display, list_display_links,
                                                list_filter, date_hierarchy, search_fields, list_select_related,
                                                list_per_page, list_max_show_all, list_editable, model_admin)

    def get_results(self, *args, **kwargs):
        super(PaymentChangeList, self).get_results(*args, **kwargs)

        for payment in self.result_list:
            if payment.is_incoming:
                self.total_in += payment.amount
            else:
                self.total_out += payment.amount

        self.total_balance = self.total_in - self.total_out


class PaymentAdmin(FhAdmin):
    """ Payment admin class """

    form = forms.PaymentForm
    list_display = (
        'get_tags_as_string', 'amount', 'date', 'is_debt', 'is_incoming',
        'created_at', 'created_by', 'modified_at', 'modified_by'
    )
    list_display_links = ('get_tags_as_string', 'amount',)
    list_filter = [TaggitListFilter, 'is_incoming', 'created_by', 'date', 'created_at', ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ['tags', 'amount', 'is_incoming'],
        }),
        ('Date & user', {
            'classes': ('suit-tab', 'suit-tab-add'),
            'fields': ['date', 'created_by'],
        }),
    ]
    suit_form_tabs = (('general', 'General'), ('add', 'Date & user'))
    ordering = ['-date']
    search_fields = ['id']

    def get_changelist(self, request):
        return PaymentChangeList

    @staticmethod
    def suit_row_attributes(obj, request):
        if obj.is_debt:
            return {'class': 'error'}
        if obj.is_incoming:
            return {'class': 'success'}

    @staticmethod
    def suit_cell_attributes(obj, column):
        if column == 'is_incoming':
            return {'class': 'text-center'}
        if column == 'is_debt':
            return {'class': 'text-center'}
        elif column == 'amount':
            return {'class': 'text-right'}

    class Media:
        css = {
            'all': ('admin/css/finances.css',),
        }
        js = ('admin/js/finances.js',)


admin.site.register(models.Payment, PaymentAdmin)
