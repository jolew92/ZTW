# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0004_auto_20150412_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieitem',
            old_name='movielist',
            new_name='movieitem',
        ),
        migrations.AddField(
            model_name='movielist',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
