# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectworklogsall',
            name='pwa_markdown',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectworklogsall',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projectworklogsall',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projectworklogsall',
            name='pwa_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]