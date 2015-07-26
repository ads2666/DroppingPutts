# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0015_auto_20150725_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='total_strokes',
            field=models.IntegerField(null=True),
        ),
    ]
