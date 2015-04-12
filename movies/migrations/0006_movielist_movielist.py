# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20150412_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='movielist',
            field=models.ManyToManyField(to='movies.MovieItem', null=True),
            preserve_default=True,
        ),
    ]
