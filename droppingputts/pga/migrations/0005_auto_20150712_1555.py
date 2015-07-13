# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0004_auto_20150712_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='overall',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
