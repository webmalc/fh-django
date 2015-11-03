# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.utils.timezone
import django.core.validators
import django.db.models.deletion
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('is_incoming', models.BooleanField(default=False, verbose_name=b'Is incoming?')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(related_query_name=b'created_by', related_name='created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_query_name=b'modified_by', related_name='modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
