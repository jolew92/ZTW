# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150511_1452'),
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
            name='Timetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_time', models.TimeField()),
                ('cinema', models.ForeignKey(verbose_name=b'Kino', to='cinema.Cinema')),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
            options={
                'ordering': ['cinema'],
                'verbose_name': 'Repertuar',
                'verbose_name_plural': 'Repertuary',
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
            model_name='cinema',
            name='town',
            field=models.ForeignKey(verbose_name=b'Miasto', to='cinema.Town'),
            preserve_default=True,
        ),
    ]
