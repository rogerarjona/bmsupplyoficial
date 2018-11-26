# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class PartnerAdmin(admin.ModelAdmin):
	model = Partner
	list_display = ('name', 'email', 'created', 'last_updated')
	search_fields = ('name', 'id')
admin.site.register(Partner, PartnerAdmin)

class WarehouseAdmin(admin.ModelAdmin):
	model = Warehouse
	list_display = ('name', 'created', 'partner')
	search_fields = ('name', 'id', 'partner')
	raw_id_fields = ['partner']
admin.site.register(Warehouse, WarehouseAdmin)

class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ('name', 'price', 'quantity', 'created', 'last_updated')
	search_fields = ('name', 'price', 'partner')
	raw_id_fields = ['partner', 'warehouse', 'category', 'status', 'promotion']
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	model = Category
	list_display = ('name', 'created')
	search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)

class StatusAdmin(admin.ModelAdmin):
	model = Status
	list_display = ('name', 'created')
	search_fields = ('name',)
admin.site.register(Status, StatusAdmin)

class PromotionAdmin(admin.ModelAdmin):
	model = Promotion
	list_display = ('name', 'porcent', 'created')
	search_fields = ('name', 'porcent')
admin.site.register(Promotion, PromotionAdmin)
