from django.db import models
from django.core.validators import MinValueValidator
from fh.models import CommonInfo
from django.utils import timezone
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse


class PaymentManager(models.Manager):
    """ Payment model manager """

    def filtered(self, begin=None, end=None, tags=None, user=None, is_incoming=None, sort='date', order='asc'):
        """
        Filtered payment query
        :param begin:
        :param end:
        :param tags:
        :param user:
        :param is_incoming:
        :param sort:
        :param order:
        :return: QuerySet
        """
        q = self.all()

        if begin is not None:
            q = q.filter(date__gte=begin)

        if end is not None:
            q = q.filter(date__lte=end)

        if tags is not None:
            q = q.filter(tags__in=tags)

        if is_incoming is not None:
            q = q.filter(is_incoming=is_incoming)

        if user is not None:
            q = q.filter(created_by=user)

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
