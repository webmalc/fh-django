# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20151130_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(verbose_name='Is completed?', default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'trivial'), (2, 'minor'), (3, 'normal'), (4, 'major'), (5, 'critical')], validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='task',
            name='remind',
            field=models.PositiveIntegerField(blank=True, choices=[(15, '15 minutes'), (30, '30 minutes'), (60, '1 hour'), (120, '2 hours'), (180, '3 hours'), (360, '6 hours'), (1440, '1 day'), (2880, '2 days'), (4320, '3 days'), (10080, '1 week'), (20160, '2 weeks'), (30240, '3 weeks')], null=True, verbose_name='Remind before?'),
        ),
    ]
