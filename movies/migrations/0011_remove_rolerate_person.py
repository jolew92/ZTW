# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_rolerate_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rolerate',
            name='person',
        ),
    ]
