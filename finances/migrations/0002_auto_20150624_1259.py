# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='updated_at',
            new_name='modified_at',
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(max_digits=20, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='is_incoming',
            field=models.BooleanField(default=False, verbose_name=b'Is incoming?'),
        ),
    ]
