# -*- coding: utf-8 -*-	
from __future__ import unicode_literals
from django.db import models

#Empresa / Colaborador
class Partner(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(max_length=100, blank=True)
    address = models.TextField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True,)
    webpage = models.URLField(max_length=150, blank=True, )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    contract = models.FileField(upload_to="partner/contracts", blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __unicode__(self):
        return u'{0}'.format(self.name)

#Almacen
class Warehouse(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=100, blank=True)
    address = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    #Foreign Keys
    partner = models.ForeignKey(Partner, related_name='partnet_warehouse')


    class Meta:
        ordering = ('-created',)
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Status(models.Model):

    name = models.CharField(max_length=100, unique=True)
    class_css = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Promotion(models.Model):

    name = models.CharField(max_length=100, unique=True)
    porcent = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Descuento", default=0)
    created = models.DateTimeField(auto_now=True, editable=False)
    start = models.DateField(auto_now=True, editable=True)
    end = models.DateField(auto_now=True, editable=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Send(models.Model):
    name = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Costo", default=0)
    created = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Product(models.Model):
    shortname = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1500, blank=True)
    description_image = models.ImageField(upload_to='description', blank=True, null=True)
    specifications = models.ImageField(upload_to='specifications', blank=True, null=True)
    image = models.ImageField(upload_to='product', blank=True, null=True)
    created = models.DateTimeField(auto_now=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    sku = models.CharField(max_length=30, blank=True, null=True)
    base = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Costo", default=0)

    #Foreign Keys
    category = models.ForeignKey(Category, related_name='product_category')
    promotion = models.ForeignKey(Promotion, related_name='product_promotion', blank=True, null=True)
    partner = models.ForeignKey(Partner, related_name='product_partner', on_delete=models.CASCADE)
    send = models.ForeignKey(Send, related_name='product_send', blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return u'{0}'.format(self.shortname)

class ProductWarehouse(models.Model):
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Costo", default=0)
    quantity = models.SmallIntegerField(default=1)

    #Foreign Keys
    product = models.ForeignKey(Product, related_name='product_productwarehouse')
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_productwarehouse')
    status = models.ForeignKey(Status, related_name='status_productwarehouse')

    class Meta:
        # ordering = ('-created',)
        verbose_name = "ProductWarehouse"
        verbose_name_plural = "ProductWarehouse"

    def __unicode__(self):
        return u'{0}'.format(self.product)

class QuantityDiscount(models.Model):
    quantity = models.SmallIntegerField(default=1)
    name = models.CharField(max_length=50)
    mult = models.DecimalField(max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "QuantityDiscount"
        verbose_name_plural = "QuantityDiscount"

    def __unicode__(self):
        return u'{0}'.format(self.name)