from django import forms
from suit.widgets import SuitSplitDateTimeWidget


class PaymentAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'date': SuitSplitDateTimeWidget,
        }
