# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 08:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('add_friend', '0006_auto_20171013_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_friend',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 13, 15, 30, 39, 263529, tzinfo=utc)),
        ),
    ]
