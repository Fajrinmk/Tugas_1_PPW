# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 04:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 11, 2, 3, 493899, tzinfo=utc)),
        ),
    ]