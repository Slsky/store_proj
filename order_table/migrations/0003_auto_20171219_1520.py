# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_table', '0002_auto_20171219_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='comments',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='telephon',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='port',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='port',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order_table.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
