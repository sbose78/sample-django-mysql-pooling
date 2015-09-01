# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smartpot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scientific_name', models.CharField(max_length=200)),
                ('plant_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PotData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pot', models.ForeignKey(to='smartpot.Pot')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sunlight', models.FloatField()),
                ('moisture', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='potdata',
            name='sensor_data',
            field=models.ForeignKey(to='smartpot.SensorData'),
        ),
        migrations.AddField(
            model_name='pot',
            name='plant',
            field=models.ForeignKey(default=datetime.datetime(2015, 6, 17, 20, 0, 44, 435735, tzinfo=utc), to='smartpot.Plant'),
            preserve_default=False,
        ),
    ]
