# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataprofile',
            name='expertise',
            field=models.CharField(max_length=250),
        ),
    ]
