# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20181126_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantitydiscount',
            name='mult',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
