# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-25 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20181125_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='class_css',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]