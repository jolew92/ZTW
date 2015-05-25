# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='description',
            options={'verbose_name': 'Opis filmu', 'verbose_name_plural': 'Opisy film\xf3w'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name'], 'verbose_name': 'J\u0119zyk', 'verbose_name_plural': 'J\u0119zyki'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Ocena filmu', 'verbose_name_plural': 'Oceny film\xf3w'},
        ),
        migrations.AlterModelOptions(
            name='rolerate',
            options={'verbose_name': 'Ocena rolo', 'verbose_name_plural': 'Oceny r\xf3l'},
        ),
        migrations.AddField(
            model_name='avgrole',
            name='avgR',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='description',
            name='language',
            field=models.CharField(default=b'PL', max_length=2, verbose_name=b'J\xc4\x99zyk', choices=[(b'PL', b'Polski'), (b'EN', b'English')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'J\xc4\x99zyk'),
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
            field=models.CharField(max_length=30, verbose_name=b'Tytu\xc5\x82'),
            preserve_default=True,
        ),
    ]
