from django.contrib import admin
from finances import models

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'is_incoming', 'created_at', 'created_by', 'modified_at', 'modified_by')
    list_display_links = ('id', 'amount')
    fields = ['amount', 'is_incoming', 'created_by']

admin.site.register(models.Payment, PaymentAdmin)
