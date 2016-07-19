# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_auto_20160719_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProjectsAll',
            fields=[
                ('cpa_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.CharField(max_length=30)),
                ('modified_at', models.DateTimeField()),
                ('modified_by', models.CharField(max_length=30)),
                ('cpa_code', models.CharField(max_length=30)),
                ('cpa_title', models.CharField(max_length=160)),
                ('cpa_title_deleted', models.CharField(blank=True, max_length=160, null=True)),
                ('cpa_summary', models.CharField(blank=True, max_length=512, null=True)),
                ('cpa_url', models.CharField(max_length=160, unique=True)),
                ('cpa_url_deleted', models.CharField(blank=True, max_length=160, null=True)),
                ('cpa_deleted', models.BooleanField()),
                ('cpa_deleted_date', models.DateTimeField(blank=True, null=True)),
                ('cpa_deleted_by', models.CharField(blank=True, max_length=30, null=True)),
                ('cca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.ClientCategoriesAll')),
                ('cpoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.ClientPurchaseOrdersAll')),
                ('tua', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.TeamUsersAll')),
            ],
            options={
                'managed': True,
                'db_table': 'category_projects_all',
            },
        ),
        migrations.AlterUniqueTogether(
            name='categoryprojectsall',
            unique_together=set([('cpa_title', 'cca'), ('cpa_code', 'cca')]),
        ),
    ]
