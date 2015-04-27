# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150425_1711'),
        ('list', '0002_auto_20150425_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieListItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movielist', models.ForeignKey(blank=True, to='list.MovieList', null=True)),
                ('movies', models.ManyToManyField(to='movies.Movie', null=True, verbose_name=b'Movies', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='movieitem',
            name='movieitem',
        ),
        migrations.RemoveField(
            model_name='movieitem',
            name='movielist',
        ),
        migrations.DeleteModel(
            name='MovieItem',
        ),
        migrations.AlterModelOptions(
            name='movielist',
            options={},
        ),
    ]
