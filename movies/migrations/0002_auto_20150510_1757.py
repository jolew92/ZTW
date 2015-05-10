# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rolerate',
            options={'verbose_name': 'Ocena roli', 'verbose_name_plural': 'Oceny r\xf3l'},
        ),
        migrations.AlterField(
            model_name='description',
            name='language',
            field=models.CharField(default=b'PL', max_length=2, verbose_name=b'J\xc4\x99zyk', choices=[(b'PL', b'Polski'), (b'EN', b'English')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.ForeignKey(verbose_name=b'J\xc4\x99zyk', blank=True, to='movies.Language', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=30, verbose_name=b'Tytu\xc5\x82\xe2\x80\x9a'),
            preserve_default=True,
        ),
    ]
