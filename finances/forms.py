from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget
import autocomplete_light


class FinancesForm(autocomplete_light.ModelForm):
    tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))
