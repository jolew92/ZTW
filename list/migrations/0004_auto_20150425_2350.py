# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20150425_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='name',
        ),
        migrations.AddField(
            model_name='movielistitem',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name=b'Nazwa'),
            preserve_default=False,
        ),
    ]
