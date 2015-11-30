# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('modified_at', models.DateTimeField(null=True, auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('comment', models.TextField(null=True, blank=True)),
                ('date', models.DateTimeField()),
                ('remind', models.PositiveIntegerField()),
                ('priority', models.PositiveSmallIntegerField(validators=(django.core.validators.MaxValueValidator(5),))),
                ('assigned_to', models.ManyToManyField(to='users.User', blank=True)),
                ('created_by', models.ForeignKey(null=True, to='users.User', blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_task_created_by')),
                ('modified_by', models.ForeignKey(null=True, to='users.User', blank=True, on_delete=django.db.models.deletion.SET_NULL, editable=False, related_name='tasks_task_modified_by')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
