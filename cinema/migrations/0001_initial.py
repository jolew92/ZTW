# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='Siec')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Siec',
                'verbose_name_plural': 'Sieci',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('additionalName', models.CharField(max_length=30, null=True, verbose_name=b'Dodatkowa nazwa', blank=True)),
                ('street', models.CharField(max_length=30, verbose_name=b'Ulica')),
                ('street_number', models.CharField(max_length=30, verbose_name=b'Nr')),
                ('brand', models.ForeignKey(verbose_name='Siec', to='cinema.Brand')),
            ],
            options={
                'ordering': ['brand'],
                'verbose_name': 'Kino',
                'verbose_name_plural': 'Kina',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seans_time', models.TimeField()),
            ],
            options={
                'ordering': ['movieInCinema'],
                'verbose_name': 'Repertuar',
                'verbose_name_plural': 'Repertuary',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sala', models.CharField(default=1, max_length=2, verbose_name=b'Sala', choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20')])),
                ('cinema', models.ForeignKey(verbose_name=b'Kino', to='cinema.Cinema')),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
            options={
                'ordering': ['cinema'],
                'verbose_name': 'Film w kinie',
                'verbose_name_plural': 'Filmy w kinach',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Miasto')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Miasto',
                'verbose_name_plural': 'Miasta',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seans',
            name='movieInCinema',
            field=models.ForeignKey(verbose_name=b'Film w kinie', to='cinema.Timetable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cinema',
            name='town',
            field=models.ForeignKey(verbose_name=b'Miasto', to='cinema.Town'),
            preserve_default=True,
        ),
    ]
