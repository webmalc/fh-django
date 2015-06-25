from django.contrib.auth.admin import admin, UserAdmin
from django.contrib.auth.models import User
from .forms import UserAdminChangeForm
from django.utils.translation import ugettext_lazy as _


class MyUserAdmin(UserAdmin):
    form = UserAdminChangeForm

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('username', 'password')
        }),
        (_('Personal info'), {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': ('first_name', 'last_name', 'email')
        }),
        (_('Permissions'), {
            'classes': ('suit-tab', 'suit-tab-permissions'),
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions')
        }),
        (_('Important dates'), {
            'classes': ('suit-tab', 'suit-tab-dates'),
            'fields': ('last_login', 'date_joined')
        }),
    )

    suit_form_tabs = (
        ('general', _('General')),
        ('info', _('Personal info')),
        ('permissions', _('Permissions')),
        ('dates', _('Important dates'))
    )

    def suit_cell_attributes(self, obj, column):
        if column == 'is_staff':
            return {'class': 'text-center'}

    class Media:
        css = {
            'all': ('admin/css/users.css',)
        }


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
