from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget
from django import forms


class FinancesForm(forms.ModelForm):
    tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))