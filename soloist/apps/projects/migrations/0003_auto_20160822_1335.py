# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160822_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectworklogsall',
            name='pwa_markdown',
            field=models.BooleanField(default=True),
        ),
    ]
