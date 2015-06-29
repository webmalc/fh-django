from django.db import models
from django.core.validators import MinValueValidator
from fh.models import CommonInfo
from django.utils import timezone
from taggit.managers import TaggableManager


class Payment(CommonInfo):
    """ Payment model """

    tags = TaggableManager()
    amount = models.DecimalField(max_digits=20, decimal_places=2,
                                 validators=[MinValueValidator(0.01)])
    is_incoming = models.BooleanField(default=False, verbose_name='Is incoming?')
    date = models.DateTimeField(default=timezone.now)

    def get_tags_as_string(self):
        """
        Return tags as formatted string
        :return: formatted string
        """
        return ', '.join([tag.name for tag in self.tags.all()])

    get_tags_as_string.short_description = 'Tags'

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date']
