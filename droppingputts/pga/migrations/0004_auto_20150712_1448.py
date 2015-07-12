# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pga', '0003_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='year',
        ),
        migrations.AddField(
            model_name='tournament',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 7, 12, 19, 48, 32, 581840, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
