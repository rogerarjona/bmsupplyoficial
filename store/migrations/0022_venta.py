# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 07:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0021_enviofacturacion_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta_userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
