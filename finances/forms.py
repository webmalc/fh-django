from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget
import autocomplete_light
from django import forms
from datetime import date


class PaymentForm(autocomplete_light.ModelForm):
    """
    Payment add/edit form
    """
    tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))


class PaymentsFilterForm(forms.Form):
    """
    Payments list filter form
    """
    begin = forms.CharField(
        label='From',
        max_length=11,
        widget=forms.TextInput(attrs={'placeholder': date.fromordinal(date.today().toordinal()-7).strftime('%d.%m.%Y')})
    )
    end = forms.CharField(
        label='To',
        max_length=11,
        widget=forms.TextInput(attrs={'placeholder': date.today().strftime('%d.%m.%Y')})
    )

