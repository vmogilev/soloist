# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectWorklogsAll',
            fields=[
                ('pwa_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.CharField(max_length=30)),
                ('modified_at', models.DateTimeField()),
                ('modified_by', models.CharField(max_length=30)),
                ('pwa_note', models.TextField()),
                ('cpa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categories.CategoryProjectsAll')),
            ],
            options={
                'db_table': 'project_worklogs_all',
                'managed': True,
            },
        ),
    ]
