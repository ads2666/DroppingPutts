# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0012_score_total_strokes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-total_strokes']},
        ),
        migrations.AddField(
            model_name='score',
            name='position',
            field=models.CharField(default=7, max_length=10),
            preserve_default=False,
        ),
    ]
