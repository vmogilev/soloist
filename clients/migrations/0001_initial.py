# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCategoriesAll',
            fields=[
                ('cca_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.CharField(max_length=30)),
                ('modified_at', models.DateTimeField()),
                ('modified_by', models.CharField(max_length=30)),
                ('cca_code', models.CharField(max_length=30)),
                ('cca_name', models.CharField(max_length=128)),
                ('pca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portals.PortalClientsAll')),
            ],
            options={
                'managed': True,
                'db_table': 'client_categories_all',
            },
        ),
        migrations.CreateModel(
            name='ClientPurchaseOrdersAll',
            fields=[
                ('cpoa_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.CharField(max_length=30)),
                ('modified_at', models.DateTimeField()),
                ('modified_by', models.CharField(max_length=30)),
                ('cpoa_number', models.CharField(max_length=30)),
                ('cpoa_date', models.DateTimeField()),
                ('cpoa_total', models.DecimalField(decimal_places=2, max_digits=17)),
                ('cpoa_soa', models.TextField(blank=True, null=True)),
                ('pca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portals.PortalClientsAll')),
            ],
            options={
                'managed': True,
                'db_table': 'client_purchase_orders_all',
            },
        ),
        migrations.AlterUniqueTogether(
            name='clientpurchaseordersall',
            unique_together=set([('pca', 'cpoa_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='clientcategoriesall',
            unique_together=set([('pca', 'cca_code')]),
        ),
    ]
