# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_avgrole_rolerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolerate',
            name='role',
            field=models.ManyToManyField(to='movies.MovieRole'),
            preserve_default=True,
        ),
    ]
