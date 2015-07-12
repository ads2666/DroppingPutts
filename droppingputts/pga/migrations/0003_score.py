# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0002_auto_20150712_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round_one', models.CharField(max_length=10)),
                ('round_two', models.CharField(max_length=10)),
                ('round_three', models.CharField(max_length=10)),
                ('round_four', models.CharField(max_length=10)),
                ('overall', models.CharField(max_length=10)),
                ('player', models.ForeignKey(to='pga.Player')),
                ('tournament', models.ForeignKey(to='pga.Tournament')),
            ],
        ),
    ]
