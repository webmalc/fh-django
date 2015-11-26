from django.forms.models import modelform_factory


class FormInitialDataMixin:
    """
    Get initial data mixin
    """

    def get_initial_data(self, exclude=[]):
        return {key: field.initial for (key, field) in self.fields.items() if key not in exclude}


class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)
