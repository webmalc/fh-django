from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from fh.models import CommonInfo


class Payment(CommonInfo):
    """ Payment model """

    amount = models.DecimalField(max_digits=20, decimal_places=2,
                                 validators=[MinValueValidator(0.01)])
    is_incoming = models.BooleanField(default=False, verbose_name='Is incoming?')
    date = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date']

