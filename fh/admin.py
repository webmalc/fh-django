from django.contrib import admin
from django.db import models as models
from suit.widgets import SuitSplitDateTimeWidget
from sitetree.admin import TreeItemAdmin, override_item_admin
from django.utils.translation import ugettext_lazy as _


class FhAdmin(admin.ModelAdmin):
    """
    Base Admin class
    """
    formfield_overrides = {
        models.DateTimeField: {'widget': SuitSplitDateTimeWidget},
    }


class CustomTreeItemAdmin(TreeItemAdmin):
    fieldsets = (
        (_('Basic settings'), {
            'fields': ('parent', 'title', 'url',)
        }),
        (_('Access settings'), {
            'classes': ('collapse',),
            'fields': ('access_loggedin', 'access_guest', 'access_restricted', 'access_permissions', 'access_perm_type')
        }),
        (_('Display settings'), {
            'classes': ('collapse',),
            'fields': ('hidden', 'inmenu', 'inbreadcrumbs', 'insitetree')
        }),
        (_('Additional settings'), {
            'classes': ('collapse',),
            'fields': ('hint', 'description', 'alias', 'icon', 'urlaspattern')
        }),
    )


override_item_admin(CustomTreeItemAdmin)
