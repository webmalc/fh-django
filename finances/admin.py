from django.contrib import admin
from finances import models

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'date', 'is_incoming', 'created_at', 'created_by', 'modified_at', 'modified_by')
    list_display_links = ('id', 'amount')
    list_filter = ['is_incoming', 'created_by', 'date', 'created_at']
    fieldsets = [
        (None, {'fields': ['amount', 'is_incoming']}),
        ('Date & user', {'fields': ['date', 'created_by'], 'classes': ['collapse']}),
    ]
    ordering = ['-date']

admin.site.register(models.Payment, PaymentAdmin)
