# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('movies', '0014_auto_20150510_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movierole',
            name='person',
        ),
        migrations.AddField(
            model_name='movierole',
            name='people',
            field=models.ManyToManyField(to='people.Person', null=True, verbose_name=b'Osoba', blank=True),
            preserve_default=True,
        ),
    ]
