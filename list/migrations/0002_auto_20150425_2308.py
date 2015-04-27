# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='movielist',
            name='movielist',
        ),
        migrations.AddField(
            model_name='movieitem',
            name='movielist',
            field=models.ManyToManyField(to='list.MovieList', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movielist',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name=b'Nazwa'),
            preserve_default=False,
        ),
    ]
