from django.contrib import admin
from django.db import models as models
from suit.widgets import SuitSplitDateTimeWidget

class FhAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateTimeField: {'widget': SuitSplitDateTimeWidget},
    }
