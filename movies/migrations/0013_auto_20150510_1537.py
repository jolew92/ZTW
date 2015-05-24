# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20150510_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierole',
            name='people',
            field=models.ManyToManyField(to='people.Person', null=True, verbose_name=b'Osoba', blank=True),
            preserve_default=True,
        ),
    ]
