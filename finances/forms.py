from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget
import autocomplete_light
from django import forms
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.models import Tag
from fh.forms import Form

DATES = {
    'tomorrow': date.fromordinal(timezone.now().toordinal() + 1),
    'today': date.today(),
    'yesterday': date.fromordinal(timezone.now().toordinal() - 1),
    'week': date.fromordinal(timezone.now().toordinal() - 7),
    'month': date.fromordinal(timezone.now().toordinal() - 31),
    'year': date.fromordinal(timezone.now().toordinal() - 365),
}
TAGS = Tag.objects.all().order_by('name')


class PaymentForm(autocomplete_light.ModelForm):
    """
    Payment add/edit form
    """
    tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))


class PaymentsFilterForm(Form):
    """
    Payments list filter form
    """

    begin = forms.DateField(
        label='From',
        required=True,
        input_formats=('%Y-%m-%d',),
        widget=forms.TextInput(attrs={'placeholder': DATES['week'], 'class': 'datepicker'}),
        initial=DATES['year']
    )
    end = forms.DateField(
        label='To',
        required=True,
        input_formats=('%Y-%m-%d',),
        widget=forms.TextInput(attrs={'placeholder': DATES['tomorrow'], 'class': 'datepicker'}),
        initial=DATES['tomorrow']
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
        ),
        initial='%s_%s' % (DATES['year'], DATES['tomorrow'])
    )
    include_tags = forms.ModelMultipleChoiceField(
        label='Tags <small><i class="fa fa-plus-circle"></i></small>',
        required=False,
        queryset=TAGS,
        widget=forms.SelectMultiple(attrs={"data-live-search": "true", "data-size": 10})
    )
    exclude_tags = forms.ModelMultipleChoiceField(
        label='Tags  <small><i class="fa fa-minus-circle"></i></small>',
        required=False,
        queryset=TAGS,
        widget=forms.SelectMultiple(attrs={"data-live-search": "true", "data-size": 10})
    )
    user = forms.ModelChoiceField(
        required=False,
        empty_label="---------",
        queryset=User.objects.all()
    )
    is_incoming = forms.ChoiceField(
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
        self.cleaned_data['is_incoming'] = bool(int(data.get("is_incoming"))) if is_incoming else None
        self.cleaned_data['include_tags'] = data.get("include_tags") if data.get("include_tags") else None
        self.cleaned_data.pop("period", None)

        if begin and end:
            if begin > end or abs((end - begin).days) > 366 * 2:
                msg = "Period dates incorrect."
                self.add_error('begin', msg)
                self.add_error('end', msg)
