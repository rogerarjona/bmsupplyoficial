# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-25 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20181125_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]