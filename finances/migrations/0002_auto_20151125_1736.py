# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='comment',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='payment',
            name='is_debt',
            field=models.BooleanField(default=False, verbose_name='Is debt?'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(related_query_name='created_by', null=True, blank=True, to='users.User', on_delete=django.db.models.deletion.SET_NULL, related_name='created_by'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='is_incoming',
            field=models.BooleanField(default=False, verbose_name='Is incoming?'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='modified_by',
            field=models.ForeignKey(related_query_name='modified_by', null=True, blank=True, to='users.User', on_delete=django.db.models.deletion.SET_NULL, editable=False, related_name='modified_by'),
        ),
    ]
