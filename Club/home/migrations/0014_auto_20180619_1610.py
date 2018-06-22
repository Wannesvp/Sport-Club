# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-19 14:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180618_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='level',
        ),
        migrations.AddField(
            model_name='training',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='End Time'),
        ),
        migrations.AddField(
            model_name='training',
            name='is_standard',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date'),
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]