# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(default='', max_length=30, verbose_name=b'Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='genre_en',
            field=models.CharField(default='', max_length=30, verbose_name=b'Genre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='name_en',
            field=models.CharField(default='', max_length=30, verbose_name=b'Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='title_en',
            field=models.CharField(default='', max_length=30, verbose_name=b'Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='role_en',
            field=models.CharField(default='', max_length=30, verbose_name=b'Role'),
            preserve_default=False,
        ),
    ]
