# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20160307_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bioplex',
            fields=[
                ('bpid', models.CharField(db_column='BPID', max_length=40, primary_key=True, serialize=False)),
                ('entreza', models.IntegerField(blank=True, db_column='ENTREZA', null=True)),
                ('entrezb', models.IntegerField(blank=True, db_column='ENTREZB', null=True)),
                ('symbola', models.CharField(blank=True, db_column='SYMBOLA', max_length=40, null=True)),
                ('symbolb', models.CharField(blank=True, db_column='SYMBOLB', max_length=40, null=True)),
                ('pw', models.FloatField(blank=True, db_column='PW', null=True)),
                ('pni', models.FloatField(blank=True, db_column='PNI', null=True)),
                ('pint', models.FloatField(blank=True, db_column='PINT', null=True)),
            ],
            options={
                'db_table': 'bioplex',
                'managed': False,
            },
        ),
    ]
