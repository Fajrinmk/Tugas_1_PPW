# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 08:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('add_friend', '0004_auto_20171013_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_friend',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 13, 15, 15, 16, 91655, tzinfo=utc)),
        ),
    ]
