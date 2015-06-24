from django.db import models
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    """ CommonInfo abstract model """

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, editable=False,
                                   related_name="created_by", related_query_name="created_by")
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, editable=False,
                                    related_name="modified_by", related_query_name="modified_by")

    class Meta:
        abstract = True
