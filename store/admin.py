# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class PartnerAdmin(admin.ModelAdmin):
	model = Partner
	list_display = ('name', 'email', 'created')
	search_fields = ('name', 'id')
admin.site.register(Partner, PartnerAdmin)
