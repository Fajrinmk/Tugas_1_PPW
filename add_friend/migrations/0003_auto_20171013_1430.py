# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 07:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('add_friend', '0002_new_friend_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_friend',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 13, 14, 30, 34, 933375, tzinfo=utc)),
        ),
    ]
