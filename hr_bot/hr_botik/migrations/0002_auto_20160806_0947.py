# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_botik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrquery',
            name='dreamage',
            field=models.FloatField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hrquery',
            name='dreamlocation',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='hrquery',
            name='dreamskills',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='hrquery',
            name='dreamtitle',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
    ]
