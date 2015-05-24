# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('movies', '0009_auto_20150510_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolerate',
            name='person',
            field=models.ForeignKey(default='', to='people.Person'),
            preserve_default=False,
        ),
    ]
