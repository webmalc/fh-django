from django.contrib import admin
from fh.admin import FhAdmin
from fh.filters import TaggitListFilter
from finances import models

class PaymentAdmin(FhAdmin):
    """ Payment admin class """

    list_display = ('get_tags_as_string', 'amount', 'date', 'is_incoming', 'created_at', 'created_by', 'modified_at', 'modified_by')
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

    @staticmethod
    def suit_cell_attributes(obj, column):
        if column == 'is_incoming':
            return {'class': 'text-center'}
        elif column == 'amount':
            return {'class': 'text-right'}

    class Media:
        css = {
            'all': ('bootstrap-tagsinput/dist/bootstrap-tagsinput.css', 'admin/css/finances.css'),
        }
        js = ('bootstrap-tagsinput/dist/bootstrap-tagsinput.min.js', 'admin/js/finances.js')


admin.site.register(models.Payment, PaymentAdmin)
