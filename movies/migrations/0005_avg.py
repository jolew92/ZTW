# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150503_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sumVotes', models.IntegerField()),
                ('numberOfVotes', models.IntegerField()),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
