# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_avgrole_rolerate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movierole',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_role',
            field=models.ManyToManyField(to='movies.MovieRole', null=True, verbose_name=b'Role w filmie', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movierole',
            name='people',
            field=models.ForeignKey(verbose_name=b'Osoba', blank=True, to='people.Person', null=True),
            preserve_default=True,
        ),
    ]
