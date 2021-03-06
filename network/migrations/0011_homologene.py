# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-13 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_cdd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homologene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hid', models.IntegerField(db_column='HID')),
                ('taxid', models.IntegerField(db_column='TAXID')),
                ('eid', models.IntegerField(db_column='EID')),
                ('symbol', models.CharField(blank=True, db_column='SYMBOL', max_length=30, null=True)),
                ('protgi', models.IntegerField(blank=True, db_column='PROTGI', null=True)),
                ('protacc', models.CharField(blank=True, db_column='PROTACC', max_length=30, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'homologene',
            },
        ),
    ]
