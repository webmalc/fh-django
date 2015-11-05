# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetreeitem',
            name='description',
            field=models.TextField(help_text='Additional comments on this item.', blank=True, default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sitetreeitem',
            name='hint',
            field=models.CharField(help_text='Some additional information about this item that is used as a hint.', blank=True, default='', verbose_name='Hint', max_length=200),
        ),
        migrations.AlterField(
            model_name='sitetreeitem',
            name='icon',
            field=models.CharField(null=True, help_text='FontAwesome icon. Example: fa-user.', max_length=50),
        ),
    ]
