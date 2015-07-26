# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0013_auto_20150719_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['position']},
        ),
    ]
