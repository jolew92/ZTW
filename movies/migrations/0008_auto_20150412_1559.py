# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20150412_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieitem',
            options={'verbose_name': 'Ulubiony', 'verbose_name_plural': 'Ulubione'},
        ),
        migrations.AlterModelOptions(
            name='movielist',
            options={'verbose_name': 'Lista ulubionych', 'verbose_name_plural': 'Listy ulubionych'},
        ),
    ]
