# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import order_table.models


class Migration(migrations.Migration):

    dependencies = [
        ('order_table', '0003_auto_20171219_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default=order_table.models.User.name_default, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=order_table.models.User.name_default, upload_to=''),
        ),
    ]
