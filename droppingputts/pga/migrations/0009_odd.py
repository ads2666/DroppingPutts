# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0008_auto_20150712_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('odds_to_win', models.DecimalField(max_digits=7, decimal_places=6)),
                ('player', models.ForeignKey(to='pga.Player')),
                ('tournament', models.ForeignKey(to='pga.Tournament')),
            ],
        ),
    ]
