# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_role_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='desc',
        ),
    ]
