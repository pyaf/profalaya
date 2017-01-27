# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor_info', '0009_auto_20170127_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='research_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='professor_info.ResearchWork'),
        ),
    ]
