# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor_info', '0007_auto_20170126_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='id',
            new_name='college_id',
        ),
    ]
