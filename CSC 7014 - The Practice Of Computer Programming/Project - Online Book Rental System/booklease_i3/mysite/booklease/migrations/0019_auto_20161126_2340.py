# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklease', '0018_auto_20161121_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='review_id',
        ),
        migrations.AddField(
            model_name='reviews',
            name='borrowed_book_transaction_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_book_transaction_id', to='booklease.BorrowedBook'),
            preserve_default=False,
        ),
    ]
