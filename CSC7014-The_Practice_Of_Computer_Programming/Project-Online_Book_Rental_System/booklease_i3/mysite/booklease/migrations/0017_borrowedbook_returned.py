# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklease', '0016_auto_20161121_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
