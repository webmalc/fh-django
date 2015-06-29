import autocomplete_light
from taggit.models import Tag


class TagAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = Tag
    attrs = {
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Comma separated tags',
    }

autocomplete_light.register(TagAutocomplete)
