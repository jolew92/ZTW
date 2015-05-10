# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150510_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name'], 'verbose_name': 'J\u0119zyk', 'verbose_name_plural': 'J\u0119zyki'},
        ),
    ]
