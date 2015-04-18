# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Kraj')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Kraj',
                'verbose_name_plural': 'Kraje',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name=b'Opis filmu')),
                ('language', models.CharField(default=b'PL', max_length=2, verbose_name=b'J\xc4\x99zyk', choices=[(b'PL', b'Polski'), (b'EN', b'English')])),
            ],
            options={
                'verbose_name': 'Opis filmu',
                'verbose_name_plural': 'Opisy film\xf3w',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=30, verbose_name=b'Gatunek')),
            ],
            options={
                'ordering': ['genre'],
                'verbose_name': 'Gatunek',
                'verbose_name_plural': 'Gatunki',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'J\xc4\x99zyk')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'J\u0119zyk',
                'verbose_name_plural': 'J\u0119zyki',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'Tytu\xc5\x82')),
                ('year', models.IntegerField(max_length=4, verbose_name=b'Rok')),
                ('country', models.ManyToManyField(to='movies.Country', null=True, verbose_name=b'Kraj', blank=True)),
                ('genre', models.ManyToManyField(to='movies.Genre', null=True, verbose_name=b'Gatunek', blank=True)),
                ('language', models.ForeignKey(verbose_name=b'J\xc4\x99zyk', blank=True, to='movies.Language', null=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmy',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie', models.ForeignKey(blank=True, to='movies.Movie', null=True)),
                ('people', models.ManyToManyField(to='people.Person', null=True, verbose_name=b'Osoba', blank=True)),
            ],
            options={
                'ordering': ['role'],
                'verbose_name': 'Rola',
                'verbose_name_plural': 'Role',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=30, verbose_name=b'Rola')),
            ],
            options={
                'ordering': ['role'],
                'verbose_name': 'Rola',
                'verbose_name_plural': 'Role',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movierole',
            name='role',
            field=models.ForeignKey(to='movies.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='movie',
            field=models.ForeignKey(to='movies.Movie'),
            preserve_default=True,
        ),
    ]
