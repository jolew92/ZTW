# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(null=True, verbose_name=b'U\xc5\xbcytkownik', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'Lista u\u017cytkownika',
                'verbose_name_plural': 'Listy u\u017cytkownika',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieListItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Nazwa')),
                ('movielist', models.ForeignKey(verbose_name=b'U\xc5\xbcytkownik', to='list.MovieList')),
                ('movies', models.ManyToManyField(to='movies.Movie', null=True, verbose_name=b'Filmy', blank=True)),
            ],
            options={
                'verbose_name': 'Lista',
                'verbose_name_plural': 'Listy',
            },
            bases=(models.Model,),
        ),
    ]
