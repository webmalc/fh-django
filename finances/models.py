from django.db import models
from django.core.validators import MinValueValidator
from fh.models import CommonInfo
from django.utils import timezone
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse


class PaymentManager(models.Manager):
    """ Payment model manager """

    def filtered(self, sort='date', order='asc'):
        q = self.all()
        if sort in ('amount', 'created_by', 'is_incoming', 'date'):
            q = q.order_by(sort)
        if order == 'desc':
            q = q.reverse()

        return q


class Payment(CommonInfo):
    """ Payment model """

    tags = TaggableManager()
    amount = models.DecimalField(max_digits=20, decimal_places=2,
                                 validators=[MinValueValidator(0.01)])
    is_incoming = models.BooleanField(default=False, verbose_name='Is incoming?')
    date = models.DateTimeField(default=timezone.now)
    objects = PaymentManager()

    def get_tags_as_string(self):
        """
        Return tags as formatted string
        :return: formatted string
        """
        return ', '.join([tag.name for tag in self.tags.all()])

    get_tags_as_string.short_description = 'Tags'

    def get_absolute_url(self):
        return reverse('finances:payment_update', kwargs={'pk': self.pk})

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date']
