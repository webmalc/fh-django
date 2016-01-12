from django.db import models
from fh.models import CommonInfo
from django.core.urlresolvers import reverse


class Channel(CommonInfo):
    """ Channel model """

    CATEGORIES = {
        'Kids': 'fa fa-child',
        'Educational': 'fa fa-flask',
        'Public': 'fa fa-group',
        'Music': 'fa fa-music',
        'Sport': 'fa fa-futbol-o',
        'Regional': 'fa fa-globe',
        'Entertainment': 'fa fa-star',
        'Man': 'fa fa-male',
        'Woman': 'fa fa-female',
        'Films': 'fa fa-film',
        'News': 'fa fa-newspaper-o',
        'Religion': 'fa fa-bolt',
        'Other': 'fa fa-tv'
    }

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=[(i, i) for i in sorted(CATEGORIES.keys())])
    is_enabled = models.BooleanField(default=True, verbose_name='Is enabled?')
    code = models.TextField()
    alternative_code = models.TextField(null=True, blank=True)
    is_favorite = models.BooleanField(default=False, verbose_name='Is favorite?')

    def get_absolute_url(self):
        return reverse('tv:channel_show', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['category', 'title']
