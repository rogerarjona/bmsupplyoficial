# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_venta_terminada'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
