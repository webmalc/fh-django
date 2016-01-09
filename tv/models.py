from django.db import models
from fh.models import CommonInfo
from django.core.urlresolvers import reverse


class Channel(CommonInfo):
    """ Channel model """

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_enabled = models.BooleanField(default=True, verbose_name='Is enabled?')
    code = models.TextField()

    def get_absolute_url(self):
        return reverse('tv:channel_show', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-category', 'title']
