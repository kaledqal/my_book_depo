# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-03 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_books', '0004_auto_20180403_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authoredbook',
            old_name='isbn',
            new_name='book',
        ),
    ]
