# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 07:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0009_auto_20171013_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 13, 14, 14, 46, 494751, tzinfo=utc)),
        ),
    ]
