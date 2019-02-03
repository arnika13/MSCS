# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklease', '0011_auto_20161114_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_id', to='booklease.Book')),
                ('bookowner_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookowner_username', to='booklease.BookLeaseUser')),
                ('borrower_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower_username', to='booklease.BookLeaseUser')),
            ],
        ),
    ]