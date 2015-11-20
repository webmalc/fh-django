

class FormInitialDataMixin:
    """
    Get initial data mixin
    """

    def get_initial_data(self, exclude=[]):
        return {key: field.initial for (key, field) in self.fields.items() if key not in exclude}
