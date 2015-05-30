# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, verbose_name=b'Tyty\xc5\x82', blank=True)),
                ('image', models.FileField(upload_to=b'images/', verbose_name=b'Zdj\xc4\x99cia')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Data')),
                ('width', models.IntegerField(null=True, verbose_name=b'Wysoko\xc5\x9b\xc4\x87', blank=True)),
                ('height', models.IntegerField(null=True, verbose_name=b'Szeroko\xc5\x9b\xc4\x87', blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Zdjecie',
                'verbose_name_plural': 'Zdj\u0119cia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie', models.OneToOneField(verbose_name=b'Film', to='movies.Movie')),
            ],
            options={
                'ordering': ['movie'],
                'verbose_name': 'Album Filmu',
                'verbose_name_plural': 'Albumy Film\xf3w',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.OneToOneField(verbose_name=b'Osoba', to='people.Person')),
            ],
            options={
                'ordering': ['person'],
                'verbose_name': 'Album Osoby',
                'verbose_name_plural': 'Albumy Os\xf3b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='movies',
            field=models.ManyToManyField(to='photogallery.MovieAlbum', verbose_name=b'Filmy', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='people',
            field=models.ManyToManyField(to='photogallery.PersonAlbum', verbose_name=b'Osoby', blank=True),
            preserve_default=True,
        ),
    ]
