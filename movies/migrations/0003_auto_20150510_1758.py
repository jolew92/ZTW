# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150510_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='description',
            options={'verbose_name': 'Opis filmu', 'verbose_name_plural': 'Opisy film\xf3w'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Ocena filmu', 'verbose_name_plural': 'Oceny film\xf3w'},
        ),
    ]
