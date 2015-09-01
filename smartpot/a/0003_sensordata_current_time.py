# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smartpot', '0002_auto_20150617_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='current_time',
            field=models.TimeField(default=datetime.datetime(2015, 6, 17, 20, 2, 32, 203758, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
