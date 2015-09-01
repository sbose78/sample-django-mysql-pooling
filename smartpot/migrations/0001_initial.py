# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Pot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secret_token', models.CharField(max_length=200)),
                ('hardware_id', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('is_connected', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(to='smartpot.Plant')),
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
            name='PotUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pot', models.ForeignKey(to='smartpot.Pot')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sunlight', models.FloatField()),
                ('moisture', models.FloatField()),
                ('current_time', models.TimeField(auto_now_add=True)),
                ('pot', models.ForeignKey(to='smartpot.Pot')),
            ],
        ),
        migrations.AddField(
            model_name='potdata',
            name='sensor_data',
            field=models.ForeignKey(to='smartpot.SensorData'),
        ),
    ]
