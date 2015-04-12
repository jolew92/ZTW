# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_remove_role_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieitem',
            name='movielist',
            field=models.ForeignKey(to='movies.Movie', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movieitem',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
