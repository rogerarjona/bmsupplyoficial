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
	list_display = ('shortname', 'category', 'created', 'last_updated', )
	search_fields = ('name', 'partner')
	raw_id_fields = ['partner', 'category','promotion']
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

class SendAdmin(admin.ModelAdmin):
	model = Send
	list_display = ('name', 'created')
	search_fields = ('name',)
admin.site.register(Send, SendAdmin)

class ProductWarehouseAdmin(admin.ModelAdmin):
	model = ProductWarehouse
	list_display = ('product', 'warehouse', 'price', 'quantity', 'status')
	search_fields = ('product__name', 'warehouse__name',)
admin.site.register(ProductWarehouse, ProductWarehouseAdmin)

class QuantityDiscountAdmin(admin.ModelAdmin):
	model = QuantityDiscount
	list_display = ('name', 'mult', 'created')
	search_fields = ('name',)
admin.site.register(QuantityDiscount, QuantityDiscountAdmin)

class VentaTemporalAdmin(admin.ModelAdmin):
	model = VentaTemporal
	list_display = ('id', 'producto', 'cantidad_producto', 'profile', 'terminada')
	search_fields = ('producto', 'profile')
	raw_id_fields = ['producto', 'profile',]
admin.site.register(VentaTemporal, VentaTemporalAdmin)

class EnvioFacturacionAdmin(admin.ModelAdmin):
	model = EnvioFacturacion
	list_display = ('profile', 'rfc', 'email_facturacion')
	search_fields = ('profile',)
	raw_id_fields = ['profile',]
admin.site.register(EnvioFacturacion, EnvioFacturacionAdmin)

class VentaAdmin(admin.ModelAdmin):
	model = Venta
	list_display = ('profile', 'total', 'terminada', 'created')
	search_fields = ('profile',)
	raw_id_fields = ['profile',]
admin.site.register(Venta, VentaAdmin)