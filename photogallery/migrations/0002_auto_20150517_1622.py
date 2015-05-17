# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviealbum',
            name='movie',
            field=models.OneToOneField(verbose_name=b'Film', to='movies.Movie'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personalbum',
            name='person',
            field=models.OneToOneField(verbose_name=b'Osoba', to='people.Person'),
            preserve_default=True,
        ),
    ]
