from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget
import autocomplete_light
from django import forms
from datetime import date
from django.utils import timezone
from taggit.models import Tag
from django.forms import Form
from fh.forms import FormInitialDataMixin
from users.models import User


class PaymentForm(autocomplete_light.ModelForm):
    """
    Payment add/edit form
    """
    tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))


class PaymentsFilterForm(Form, FormInitialDataMixin):
    """
    Payments list filter form
    """

    def __init__(self, *args, **kwargs):

        super(PaymentsFilterForm, self).__init__(*args, **kwargs)

        self.dates = {
            'tomorrow': date.fromordinal(timezone.now().toordinal() + 1),
            'today': date.today(),
            'yesterday': date.fromordinal(timezone.now().toordinal() - 1),
            'week': date.fromordinal(timezone.now().toordinal() - 7),
            'month': date.fromordinal(timezone.now().toordinal() - 31),
            'year': date.fromordinal(timezone.now().toordinal() - 365),
        }
        self.tags = Tag.objects.all().order_by('name')

        self.fields['begin'] = forms.DateField(
            label='From',
            required=True,
            input_formats=('%Y-%m-%d',),
            widget=forms.TextInput(attrs={'placeholder': self.dates['week'], 'class': 'datepicker'}),
            initial=self.dates['year']
        )
        self.fields['end'] = forms.DateField(
            label='To',
            required=True,
            input_formats=('%Y-%m-%d',),
            widget=forms.TextInput(attrs={'placeholder': self.dates['tomorrow'], 'class': 'datepicker'}),
            initial=self.dates['tomorrow']
        )
        self.fields['period'] = forms.ChoiceField(
            label='Period',
            required=False,
            choices=(
                ('', '---------'),
                ('%s_%s' % (self.dates['today'], self.dates['tomorrow']), 'Today'),
                ('%s_%s' % (self.dates['yesterday'], self.dates['today']), 'Yesterday'),
                ('%s_%s' % (self.dates['week'], self.dates['tomorrow']), 'Last week'),
                ('%s_%s' % (self.dates['month'], self.dates['tomorrow']), 'Last month'),
                ('%s_%s' % (self.dates['year'], self.dates['tomorrow']), 'Last year'),
            ),
            initial='%s_%s' % (self.dates['year'], self.dates['tomorrow'])
        )
        self.fields['include_tags'] = forms.ModelMultipleChoiceField(
            label='Tags <small><i class="fa fa-plus-circle"></i></small>',
            required=False,
            queryset=self.tags,
            widget=forms.SelectMultiple(attrs={"data-live-search": "true", "data-size": 10})
        )
        self.fields['exclude_tags'] = forms.ModelMultipleChoiceField(
            label='Tags  <small><i class="fa fa-minus-circle"></i></small>',
            required=False,
            queryset=self.tags,
            widget=forms.SelectMultiple(attrs={"data-live-search": "true", "data-size": 10})
        )
        self.fields['user'] = forms.ModelChoiceField(
            required=False,
            empty_label="---------",
            queryset=User.objects.all()
        )
        self.fields['is_debt'] = forms.ChoiceField(
            label='Is debt',
            required=False,
            choices=(
                ('', '---------'), (1, 'Yes'), (0, 'No')
            )
        )
        self.fields['is_incoming'] = forms.ChoiceField(
            label='Is incoming',
            required=False,
            choices=(
                ('', '---------'), (1, 'Yes'), (0, 'No')
            )
        )

    def clean(self):
        data = super(PaymentsFilterForm, self).clean()
        begin = data.get("begin")
        end = data.get("end")
        is_incoming = self.cleaned_data['is_incoming']
        is_debt = self.cleaned_data['is_debt']
        self.cleaned_data['is_incoming'] = bool(int(data.get("is_incoming"))) if is_incoming else None
        self.cleaned_data['is_debt'] = bool(int(data.get("is_debt"))) if is_debt else None
        self.cleaned_data['include_tags'] = data.get("include_tags") if data.get("include_tags") else None
        self.cleaned_data.pop("period", None)

        if begin and end:
            if begin > end or abs((end - begin).days) > 366 * 2:
                msg = "Period self.dates incorrect."
                self.add_error('begin', msg)
                self.add_error('end', msg)
