from django.contrib.auth.forms import UserChangeForm
from suit.widgets import SuitSplitDateTimeWidget


class UserAdminChangeForm(UserChangeForm):
    class Meta:
        widgets = {
            'date_joined': SuitSplitDateTimeWidget,
            'last_login': SuitSplitDateTimeWidget,
        }
