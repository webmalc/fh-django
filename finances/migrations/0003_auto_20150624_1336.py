# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_auto_20150624_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 24, 13, 36, 56, 569190)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(related_query_name=b'created_by', related_name='created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
