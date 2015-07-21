# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0009_odd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odd',
            name='odds_to_win',
            field=models.CharField(max_length=10),
        ),
    ]
