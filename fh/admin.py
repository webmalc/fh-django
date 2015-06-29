from django.contrib import admin
from django.db import models as models
from suit.widgets import SuitSplitDateTimeWidget
from taggit.models import Tag

class FhAdmin(admin.ModelAdmin):
    """
    Base Admin class
    """
    formfield_overrides = {
        models.DateTimeField: {'widget': SuitSplitDateTimeWidget},
    }

admin.site.unregister(Tag)
