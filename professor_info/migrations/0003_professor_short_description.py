# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-21 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_info', '0002_professor_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]