# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-05 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_ncbiprot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syns_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=6)),
                ('geneid', models.CharField(blank=True, max_length=20, null=True)),
                ('synonym', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'syns_view',
                'managed': False,
            },
        ),
    ]
