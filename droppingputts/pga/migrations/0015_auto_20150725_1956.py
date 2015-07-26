# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0014_auto_20150721_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published'),
        ),
    ]
