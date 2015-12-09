from django.db import models
from django.core.validators import MaxValueValidator
from taggit.managers import TaggableManager
from fh.models import CommonInfo
from users.models import User
from fh.models import TagsMixin


class Task(CommonInfo, TagsMixin):
    PRIORITIES = (
        (1, 'trivial'),
        (2, 'minor'),
        (3, 'normal'),
        (4, 'major'),
        (5, 'critical')
    )
    REMIND_BEFORE = (
        (15, '15 minutes'),
        (30, '30 minutes'),
        (60, '1 hour'),
        (60 * 2, '2 hours'),
        (60 * 3, '3 hours'),
        (60 * 6, '6 hours'),
        (60 * 24, '1 day'),
        (60 * 24 * 2, '2 days'),
        (60 * 24 * 3, '3 days'),
        (60 * 24 * 7, '1 week'),
        (60 * 24 * 14, '2 weeks'),
        (60 * 24 * 21, '3 weeks'),
    )

    """ Task model """

    title = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    tags = TaggableManager()
    # Minutes before date field
    remind = models.PositiveIntegerField(choices=REMIND_BEFORE, null=True, blank=True, verbose_name='Remind before?')
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES, validators=[MaxValueValidator(5)])
    assigned_to = models.ManyToManyField(User, blank=True)
