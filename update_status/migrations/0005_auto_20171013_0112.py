# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 18:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0004_auto_20171013_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 13, 1, 12, 39, 568078, tzinfo=utc)),
        ),
    ]
