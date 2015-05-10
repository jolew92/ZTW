# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name=b'Biografia')),
                ('language', models.CharField(default=b'PL', max_length=2, verbose_name=b'J\xc4\x99zyk', choices=[(b'PL', b'Polski'), (b'EN', b'English')])),
            ],
            options={
                'verbose_name': 'Biografia',
                'verbose_name_plural': 'Biografie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name=b'Imi\xc4\x99')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Nazwisko')),
                ('birthday', models.DateField(null=True, verbose_name=b'Data urodzenia', blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name': 'Osoba',
                'verbose_name_plural': 'Osoby',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='biography',
            name='person',
            field=models.ForeignKey(to='people.Person'),
            preserve_default=True,
        ),
    ]
