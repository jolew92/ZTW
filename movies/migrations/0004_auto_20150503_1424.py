# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Ocena filmu', 'verbose_name_plural': 'Oceny film\xf3w'},
        ),
    ]
