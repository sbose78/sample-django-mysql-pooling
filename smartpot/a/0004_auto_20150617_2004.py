# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartpot', '0003_sensordata_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='current_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
