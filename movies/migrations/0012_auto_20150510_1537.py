# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_remove_rolerate_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierole',
            name='people',
            field=models.ForeignKey(verbose_name=b'Osoba', blank=True, to='people.Person', null=True),
            preserve_default=True,
        ),
    ]
