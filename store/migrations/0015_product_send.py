# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_quantitydiscount_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='send',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_send', to='store.Send'),
        ),
    ]