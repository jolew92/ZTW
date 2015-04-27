# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20150425_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movielist',
            options={'verbose_name': 'Lista u\u017cytkownika', 'verbose_name_plural': 'Listy u\u017cytkownika'},
        ),
        migrations.AlterModelOptions(
            name='movielistitem',
            options={'verbose_name': 'Lista', 'verbose_name_plural': 'Listy'},
        ),
        migrations.AlterField(
            model_name='movielist',
            name='user',
            field=models.ForeignKey(null=True, verbose_name=b'U\xc5\xbcytkownik', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movielistitem',
            name='movielist',
            field=models.ForeignKey(default='', verbose_name=b'U\xc5\xbcytkownik', to='list.MovieList'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movielistitem',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie', null=True, verbose_name=b'Filmy', blank=True),
            preserve_default=True,
        ),
    ]
