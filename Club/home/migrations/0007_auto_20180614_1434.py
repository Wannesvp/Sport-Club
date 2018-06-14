# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-14 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180614_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cool_down',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(blank=True, max_length=200)),
                ('content_repeat', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('content_1', models.CharField(blank=True, max_length=1000)),
                ('content_1_repeat', models.IntegerField(default=1)),
                ('content_2', models.CharField(blank=True, max_length=1000)),
                ('content_2_repeat', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Warm_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(blank=True, max_length=200)),
                ('content_repeat', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='training_program',
            name='cool_down',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Cool_down'),
        ),
        migrations.AlterField(
            model_name='training_program',
            name='core',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Core'),
        ),
        migrations.AlterField(
            model_name='training_program',
            name='warm_up',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Warm_up'),
        ),
    ]