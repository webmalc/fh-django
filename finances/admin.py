from django.contrib import admin
from finances import models, forms

class PaymentAdmin(admin.ModelAdmin):
    form = forms.PaymentAdminForm
    list_display = ('id', 'amount', 'date', 'is_incoming', 'created_at', 'created_by', 'modified_at', 'modified_by')
    list_display_links = ('id', 'amount')
    list_filter = ['is_incoming', 'created_by', 'date', 'created_at']
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ['amount', 'is_incoming'],
        }),
        ('Date & user', {
            'classes': ('suit-tab', 'suit-tab-add'),
            'fields': ['date', 'created_by'],
        }),
    ]
    suit_form_tabs = (('general', 'General'), ('add', 'Date & user'))
    ordering = ['-date']
    search_fields = ['id']

    def suit_cell_attributes(self, obj, column):
        if column == 'is_incoming':
            return {'class': 'text-center'}
        elif column == 'amount':
            return {'class': 'text-right'}

    class Media:
        css = {
            'all': ('admin/css/finances.css',)
        }


admin.site.register(models.Payment, PaymentAdmin)
