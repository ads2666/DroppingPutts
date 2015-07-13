# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0007_auto_20150712_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='round_one',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='round_two',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
