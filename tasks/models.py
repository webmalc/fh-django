from django.db import models
from taggit.managers import TaggableManager
from fh.models import CommonInfo
from users.models import User


class Task(CommonInfo):
    """ Task model """

    title = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    tags = TaggableManager()
    remind = models.PositiveIntegerField()  # Minutes before date field
    priority = models.PositiveSmallIntegerField(max_length=5)
    assigned_to = models.ManyToManyField(User, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name="assigned_to", related_query_name="assigned_to")
