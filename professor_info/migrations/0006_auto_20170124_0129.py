# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_info', '0005_auto_20170121_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
    ]
