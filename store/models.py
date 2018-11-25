# -*- coding: utf-8 -*-	
from __future__ import unicode_literals
from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(max_length=100, blank=True)
    address = models.TextField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True,)
    webpage = models.URLField(max_length=150, blank=True, )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Warehouse(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=100, blank=True)
    address = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    #Foreign Keys
    partner = models.ForeignKey(Partner, related_name='partnet_warehouse')