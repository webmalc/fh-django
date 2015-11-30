from django.db import models
from django.core.validators import MaxValueValidator
from taggit.managers import TaggableManager
from fh.models import CommonInfo
from users.models import User


class Task(CommonInfo):
    """ Task model """

    title = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    tags = TaggableManager()
    remind = models.PositiveIntegerField(null=True, blank=True)  # Minutes before date field
    priority = models.PositiveSmallIntegerField(validators=(MaxValueValidator(5),))
    assigned_to = models.ManyToManyField(User, blank=True)
