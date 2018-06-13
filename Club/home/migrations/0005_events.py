# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-19 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180419_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('even_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]