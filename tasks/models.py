from django.db import models
from django.core.validators import MaxValueValidator
from taggit.managers import TaggableManager
from fh.models import CommonInfo
from users.models import User
from fh.models import TagsMixin


class Task(CommonInfo, TagsMixin):
    """ Task model """

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

    title = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    tags = TaggableManager(blank=True)
    # Minutes before date field
    remind = models.PositiveIntegerField(choices=REMIND_BEFORE, null=True, blank=True, verbose_name='Remind before?')
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES, validators=[MaxValueValidator(5)])
    assigned_to = models.ManyToManyField(User, blank=True)
    is_completed = models.BooleanField(default=False, verbose_name='Is completed?')

    def get_assigned_to_as_string(self):
        """
        Return users as formatted string
        :return: formatted string
        """
        if not self.assigned_to.count():
            return 'All'

        return ', '.join([str(user) for user in self.assigned_to.all()])

    get_assigned_to_as_string.short_description = 'Assigned to'

    class Meta:
        ordering = ('is_completed', '-date', '-created_at')
