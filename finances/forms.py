from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget
import autocomplete_light
from django import forms
from datetime import date
from django.contrib.auth.models import User
from taggit.models import Tag


class PaymentForm(autocomplete_light.ModelForm):
    """
    Payment add/edit form
    """
    tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))


class PaymentsFilterForm(forms.Form):
    """
    Payments list filter form
    """

    DATES = {
        'tomorrow': date.fromordinal(date.today().toordinal() + 1),
        'today': date.today(),
        'yesterday': date.fromordinal(date.today().toordinal() - 1),
        'week': date.fromordinal(date.today().toordinal() - 7),
        'month': date.fromordinal(date.today().toordinal() - 31),
        'year': date.fromordinal(date.today().toordinal() - 365),
    }
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    begin = forms.DateField(
        label='From',
        required=False,
        input_formats=('%d.%m.%Y',),
        widget=forms.TextInput(attrs={'placeholder': DATES['week'], 'class': 'datepicker'})
    )
    end = forms.DateField(
        label='To',
        required=False,
        input_formats=('%d.%m.%Y',),
        widget=forms.TextInput(attrs={'placeholder': DATES['tomorrow'], 'class': 'datepicker'})
    )
    period = forms.ChoiceField(
        label='Period',
        required=False,
        choices=(
            ('', '---------'),
            ('%s_%s' % (DATES['today'], DATES['tomorrow']), 'Today'),
            ('%s_%s' % (DATES['yesterday'], DATES['today']), 'Yesterday'),
            ('%s_%s' % (DATES['week'], DATES['tomorrow']), 'Last week'),
            ('%s_%s' % (DATES['month'], DATES['tomorrow']), 'Last month'),
            ('%s_%s' % (DATES['year'], DATES['tomorrow']), 'Last year'),
        )
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all()
    )
    user = forms.ModelChoiceField(
        required=False,
        empty_label="---------",
        queryset=User.objects.all()
    )
    is_incoming = forms.BooleanField(label="Is incoming?")

