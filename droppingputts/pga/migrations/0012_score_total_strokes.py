# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0011_pick'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='total_strokes',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]
