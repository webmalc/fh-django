from django import forms


class Form(forms.Form):
    """
    Base form
    """

    def get_initial_data(self, exclude=[]):
        return {key: field.initial for (key, field) in self.fields.items() if key not in exclude}
