# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0002_auto_20150517_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['title'], 'verbose_name': 'Zdjecie', 'verbose_name_plural': 'Zdj\u0119cia'},
        ),
        migrations.AlterModelOptions(
            name='moviealbum',
            options={'ordering': ['movie'], 'verbose_name': 'Album Filmu', 'verbose_name_plural': 'Albumy Film\xf3w'},
        ),
        migrations.AlterModelOptions(
            name='personalbum',
            options={'ordering': ['person'], 'verbose_name': 'Album Osoby', 'verbose_name_plural': 'Albumy Os\xf3b'},
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Data'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.IntegerField(null=True, verbose_name=b'Szeroko\xc5\x9b\xc4\x87', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to=b'images/', verbose_name=b'Zdj\xc4\x99cia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='movies',
            field=models.ManyToManyField(to='photogallery.MovieAlbum', verbose_name=b'Filmy', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='people',
            field=models.ManyToManyField(to='photogallery.PersonAlbum', verbose_name=b'Osoby', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Tyty\xc5\x82', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.IntegerField(null=True, verbose_name=b'Wysoko\xc5\x9b\xc4\x87', blank=True),
            preserve_default=True,
        ),
    ]
