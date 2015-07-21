# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pga', '0010_auto_20150718_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pick_four', models.ForeignKey(related_name='pick_four', to='pga.Player')),
                ('pick_one', models.ForeignKey(related_name='pick_one', to='pga.Player')),
                ('pick_three', models.ForeignKey(related_name='pick_three', to='pga.Player')),
                ('pick_two', models.ForeignKey(related_name='pick_two', to='pga.Player')),
                ('tournament', models.ForeignKey(to='pga.Tournament')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
