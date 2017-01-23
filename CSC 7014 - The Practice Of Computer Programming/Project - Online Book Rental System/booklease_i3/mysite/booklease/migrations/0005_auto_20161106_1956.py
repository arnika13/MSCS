# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklease', '0004_auto_20161106_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='book_status',
            field=models.CharField(choices=[('RE', 'Rented'), ('RT', 'Returned')], default='RE', max_length=2),
        ),
    ]
