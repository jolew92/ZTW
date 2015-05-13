# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150510_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avgrole',
            name='role',
        ),
        migrations.DeleteModel(
            name='AvgRole',
        ),
        migrations.AddField(
            model_name='movierole',
            name='avgR',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movierole',
            name='numberOfVotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movierole',
            name='sumVotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
