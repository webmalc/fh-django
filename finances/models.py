from django.db import models
from django.core.validators import MinValueValidator
from fh.models import CommonInfo
from django.utils import timezone
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.db.models import Sum
from decimal import Decimal


class PaymentManager(models.Manager):
    """ Payment model manager """

    def tags_by_count(self, begin=None, end=None, tags=None, user=None, is_incoming=None, limit=15):
        """
        Payments tags sorted by count
        :param begin: datetime.date
        :param end: datetime.date
        :param tags: list
        :param user: django.contrib.auth.models.User
        :param is_incoming: boolean
        :param limit: int
        :return: list [('tag_name', 'count'), (tag_name', 'count'), ...]
        """

        filtered_tags = []
        for payment in self.filtered(begin, end, tags, user, is_incoming).order_by().distinct('tags'):
            for tag in payment.tags.all():
                if (tags and tag in tags) or not tags:
                    filtered_tags.append(tag.id)

        return [(tag.name, tag.num_times) for tag in Payment.tags.most_common()[:limit] if tag.id in filtered_tags]

    def summary(self, begin=None, end=None, tags=None, user=None, is_incoming=None):
        """
        Payments total in/out
        :param begin: datetime.date
        :param end: datetime.date
        :param tags: list
        :param user: django.contrib.auth.models.User
        :param is_incoming: boolean
        :return: dict {'in': 1200.34, 'out': 500.45}
        """
        q = self.filtered(begin, end, tags, user)
        result = {'in': Decimal(0), 'out': Decimal(0)}

        if is_incoming is None:
            result['out'] = q.filter(is_incoming=False).aggregate(total=Sum('amount'))['total']
            result['in'] = q.filter(is_incoming=True).aggregate(total=Sum('amount'))['total']
        elif is_incoming:
            result['in'] = q.filter(is_incoming=True).aggregate(total=Sum('amount'))['total']
        else:
            result['out'] = q.filter(is_incoming=False).aggregate(total=Sum('amount'))['total']

        result['in'] = result['in'] if result['in'] else Decimal(0)
        result['out'] = result['out'] if result['out'] else Decimal(0)
        result['total'] = result['in'] - result['out']

        return result

    def filtered(self, begin=None, end=None, tags=None, user=None, is_incoming=None, sort='date', order='asc'):
        """
        Filtered payment query
        :param begin: datetime.date
        :param end: datetime.date
        :param tags: list
        :param user: django.contrib.auth.models.User
        :param is_incoming: boolean
        :param sort: string
        :param order: string
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
