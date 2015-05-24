# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_auto_20150504_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sumVotes', models.IntegerField()),
                ('numberOfVotes', models.IntegerField()),
                ('role', models.ForeignKey(to='movies.MovieRole')),
            ],
            options={
                'verbose_name': 'AVG ROLEs',
                'verbose_name_plural': 'AVG ROLE',
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
                'verbose_name_plural': 'Oceny r\xf3l',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='movierole',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_role',
            field=models.ManyToManyField(to='movies.MovieRole', null=True, verbose_name=b'Role w filmie', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movierole',
            name='people',
            field=models.ForeignKey(verbose_name=b'Osoba', blank=True, to='people.Person', null=True),
            preserve_default=True,
        ),
    ]
