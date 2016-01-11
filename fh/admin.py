from django.contrib import admin
from sitetree.admin import TreeItemAdmin, override_item_admin
from django.utils.translation import ugettext_lazy as _


class FhAdmin(admin.ModelAdmin):
    """
    Base Admin class
    """
    actions_on_top = False
    actions_on_bottom = True


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
