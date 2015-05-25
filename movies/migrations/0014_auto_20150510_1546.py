# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('movies', '0013_auto_20150510_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movierole',
            name='people',
        ),
        migrations.AddField(
            model_name='movierole',
            name='person',
            field=models.ForeignKey(verbose_name=b'Osoba', blank=True, to='people.Person', null=True),
            preserve_default=True,
        ),
    ]
