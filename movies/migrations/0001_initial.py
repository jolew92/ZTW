# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sumVotes', models.IntegerField()),
                ('numberOfVotes', models.IntegerField()),
            ],
            options={
                'verbose_name': 'avg',
                'verbose_name_plural': 'avg',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AvgRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sumVotes', models.IntegerField()),
                ('numberOfVotes', models.IntegerField()),
            ],
            options={
                'verbose_name': 'AVG ROLEs',
                'verbose_name_plural': 'AVG ROLE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Kraj')),
                ('name_en', models.CharField(max_length=30, verbose_name=b'Country')),
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
                ('language', models.CharField(default=b'PL', max_length=2, verbose_name=b'J\xc3\x84\xe2\x84\xa2zyk', choices=[(b'PL', b'Polski'), (b'EN', b'English')])),
            ],
            options={
                'verbose_name': 'Opis filmu',
                'verbose_name_plural': 'Opisy film\u0102\u0142w',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=30, verbose_name=b'Gatunek')),
                ('genre_en', models.CharField(max_length=30, verbose_name=b'Genre')),
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
                ('name', models.CharField(max_length=30, verbose_name=b'J\xc3\x84\xe2\x84\xa2zyk')),
                ('name_en', models.CharField(max_length=30, verbose_name=b'Language')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'J\xc4\u2122zyk',
                'verbose_name_plural': 'J\xc4\u2122zyki',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'Tytu\xc4\xb9\xe2\x80\x9a')),
                ('title_en', models.CharField(max_length=30, verbose_name=b'Title')),
                ('year', models.IntegerField(max_length=4, verbose_name=b'Rok')),
                ('country', models.ManyToManyField(to='movies.Country', null=True, verbose_name=b'Kraj', blank=True)),
                ('genre', models.ManyToManyField(to='movies.Genre', null=True, verbose_name=b'Gatunek', blank=True)),
                ('language', models.ForeignKey(verbose_name=b'J\xc3\x84\xe2\x84\xa2zyk', blank=True, to='movies.Language', null=True)),
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
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(max_length=2, verbose_name=b'Oceny', choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('movie', models.ForeignKey(to='movies.Movie')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Ocena filmu',
                'verbose_name_plural': 'Oceny film\u0102\u0142w',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=30, verbose_name=b'Rola')),
                ('role_en', models.CharField(max_length=30, verbose_name=b'Role')),
            ],
            options={
                'ordering': ['role'],
                'verbose_name': 'Rola',
                'verbose_name_plural': 'Role',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoleRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(max_length=2, verbose_name=b'Oceny2', choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('role', models.ForeignKey(to='movies.MovieRole')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Ocena rolo',
                'verbose_name_plural': 'Oceny r\u0102\u0142l',
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
        migrations.AddField(
            model_name='avgrole',
            name='role',
            field=models.ForeignKey(to='movies.MovieRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avg',
            name='movie',
            field=models.ForeignKey(to='movies.Movie'),
            preserve_default=True,
        ),
    ]
