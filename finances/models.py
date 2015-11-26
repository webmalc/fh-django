from django.db import models
from django.core.validators import MinValueValidator
from fh.models import CommonInfo
from django.utils import timezone
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.db.models import Sum
from decimal import Decimal
from django.db import connection


class PaymentManager(models.Manager):
    """ Payment model manager """

    def tags_by_amount(self, filtered_tags=None, **kwargs):
        """
        Payments tags sorted by payments amount
        :param kwargs: dict
        :param filtered_tags: dict
        :return: list [('tag_name', 'amount'), (tag_name', 'amount'), ...]
        """
        filtered_tags = filtered_tags if filtered_tags else self.filtered_tags(**kwargs)
        data = []
        for key, tag in filtered_tags.items():
            amount = self.filtered(begin=kwargs['begin'], end=kwargs['end'], user=kwargs['user'],
                                   is_incoming=kwargs['is_incoming']).filter(tags__in=(tag,)) \
                .aggregate(total=Sum('amount'))
            data.append((tag.name, amount['total']))

        return data

    def tags_by_count(self, limit=15, filtered_tags=None, **kwargs):
        """
        Payments tags sorted by count
        :param kwargs: dict
        :param limit: int
        :param filtered_tags: dict
        :return: list [('tag_name', 'count'), (tag_name', 'count'), ...]
        """
        filtered_tags = filtered_tags if filtered_tags else self.filtered_tags(**kwargs)

        return [(tag.name, tag.num_times) for tag in Payment.tags.most_common()[:limit] if
                tag.id in list(filtered_tags.keys())]

    def filtered_tags(self, **kwargs):
        """
        Get filtered tags
        :param kwargs: dict
        :return: dict {'id': Tag, 'id': Tag}
        """
        filtered_tags = {}
        for payment in self.filtered(**kwargs).order_by().distinct('tags'):
            for tag in payment.tags.all():
                if (kwargs['include_tags'] and tag in kwargs['include_tags']) or not kwargs['include_tags']:
                    filtered_tags[tag.id] = tag

        return filtered_tags

    def payments_by_days(self, begin=None, end=None, include_tags=None, exclude_tags=None, user=None,
                         is_debt=None, is_incoming=None):
        """
        Payments amount by days
        :param begin: datetime.date
        :param end: datetime.date
        :param include_tags: list
        :param exclude_tags: list
        :param is_debt: boolean
        :param user: django.contrib.auth.models.User
        :param is_incoming: boolean
        :return: list [('day', 'amount'), ('day', 'amount'), ...]
        """
        q = self.filtered(begin=begin, end=end, include_tags=include_tags, exclude_tags=exclude_tags, user=user,
                          is_debt=is_debt, is_incoming=is_incoming)
        data = q.extra(select={'day': 'date(date)'}).values('day').annotate(total=Sum('amount')).order_by('day')

        return [(entry['day'], entry['total']) for entry in data]

    def payments_by_months(self, begin=None, end=None, include_tags=None, exclude_tags=None, user=None,
                           is_debt=None, is_incoming=None):
        """
        Payments amount by months
        :param begin: datetime.date
        :param end: datetime.date
        :param include_tags: list
        :param exclude_tags: list
        :param is_debt: boolean
        :param user: django.contrib.auth.models.User
        :param is_incoming: boolean
        :return: list [('day', 'amount'), ('day', 'amount'), ...]
        """
        q = self.filtered(begin=begin, end=end, include_tags=include_tags, exclude_tags=exclude_tags, user=user,
                          is_debt=is_debt, is_incoming=is_incoming)
        truncate_date = connection.ops.date_trunc_sql('month', 'date')
        data = q.extra(select={'month': truncate_date}).values('month').annotate(total=Sum('amount')).order_by('month')

        return [(entry['month'], entry['total']) for entry in data]

    def summary(self, begin=None, end=None, include_tags=None, exclude_tags=None, user=None,
                is_debt=None, is_incoming=None):
        """
        Payments total in/out
        :param begin: datetime.date
        :param end: datetime.date
        :param include_tags: list
        :param exclude_tags: list
        :param user: django.contrib.auth.models.User
        :param is_incoming: boolean
        :param is_debt: boolean
        :return: dict {'in': 1200.34, 'out': 500.45}
        """
        q = self.filtered(begin=begin, end=end, include_tags=include_tags, is_debt=is_debt,
                          exclude_tags=exclude_tags, user=user)
        result = {'in': Decimal(0), 'out': Decimal(0), 'debt': Decimal(0)}

        debt_in = q.filter(is_debt=True, is_incoming=True).aggregate(total=Sum('amount'))['total']
        debt_out = q.filter(is_debt=True, is_incoming=False).aggregate(total=Sum('amount'))['total']

        if is_incoming is None:
            result['out'] = q.filter(is_incoming=False).aggregate(total=Sum('amount'))['total']
            result['in'] = q.filter(is_incoming=True).aggregate(total=Sum('amount'))['total']
        elif is_incoming:
            result['in'] = q.filter(is_incoming=True).aggregate(total=Sum('amount'))['total']
        else:
            result['out'] = q.filter(is_incoming=False).aggregate(total=Sum('amount'))['total']

        result['in'] = result['in'] if result['in'] else Decimal(0)
        result['out'] = result['out'] if result['out'] else Decimal(0)
        result['debt_in'] = debt_in if debt_in else Decimal(0)
        result['debt_out'] = debt_out if debt_out else Decimal(0)
        result['total'] = result['in'] - result['out']
        result['debt'] = result['debt_in'] - result['debt_out']

        return result

    def filtered(self, begin=None, end=None, include_tags=None, exclude_tags=None, user=None, is_incoming=None,
                 is_debt=None, sort='date', order='asc'):
        """
        Filtered payment query
        :param begin: datetime.date
        :param end: datetime.date
        :param include_tags: list
        :param exclude_tags: list
        :param user: django.contrib.auth.models.User
        :param is_incoming: boolean
        :param is_debt: boolean
        :param sort: string
        :param order: string
        :return: QuerySet
        """
        q = self.all()

        if begin is not None:
            q = q.filter(date__gte=begin)

        if end is not None:
            q = q.filter(date__lte=end)

        if include_tags is not None:
            q = q.filter(tags__in=include_tags)

        if exclude_tags is not None:
            q = q.exclude(tags__in=exclude_tags)

        if is_incoming is not None:
            q = q.filter(is_incoming=is_incoming)

        if is_debt is not None:
            q = q.filter(is_debt=is_debt)

        if user is not None:
            q = q.filter(created_by=user)

        if sort in ('amount', 'created_by', 'is_incoming', 'date', 'is_debt'):
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
    is_debt = models.BooleanField(default=False, verbose_name='Is debt?')
    comment = models.CharField(max_length=255, null=True, blank=True)
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

    def __str__(self):
        return '#%s' % self.id

    class Meta:
        ordering = ['-date']
