# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movieitem', models.ForeignKey(to='movies.Movie', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Ulubiony',
                'verbose_name_plural': 'Ulubione',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movielist', models.ManyToManyField(to='list.MovieItem', null=True)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'Lista ulubionych',
                'verbose_name_plural': 'Listy ulubionych',
            },
            bases=(models.Model,),
        ),
    ]
