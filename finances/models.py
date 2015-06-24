from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from fh.models import CommonInfo


class Payment(CommonInfo):
    """ Payment model """

    amount = models.DecimalField(max_digits=20, decimal_places=2,
                                 validators=[MinValueValidator(0)])
    is_incoming = models.BooleanField(default=False)
