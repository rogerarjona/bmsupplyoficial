# -*- coding: utf-8 -*-	
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from userprofile.models import *
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
    pdf = models.FileField(upload_to='pdf', blank=True, null=True)
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

class VentaTemporal(models.Model):
    
    cantidad_producto = models.SmallIntegerField(default=1)
    created = models.DateTimeField(auto_now=True, editable=False)

    profile = models.ForeignKey(User, related_name='venta_temporal_userprofile')
    producto = models.ForeignKey(ProductWarehouse, related_name='temporal_productwarehouse')
    
    class Meta:
        ordering = ('-created',)
        verbose_name = "Ventas Temporales"
        verbose_name_plural = "Ventas Temporales"

    def __unicode__(self):
        return u'{0}'.format(self.producto)
    

class EnvioFacturacion(models.Model):

    mujer = 0
    hombre = 1

    SEXO = (
        (mujer, 'Mujer'),
        (hombre, 'Hombre')
    )

    Aguascalientes = 1
    Baja_California = 2
    Baja_California_Sur = 3
    Campeche = 4
    Chiapas = 5
    Chihuahua = 6   
    Ciudad_de_Mexico = 7   
    Coahuila = 8
    Colima = 9
    Durango = 10  
    Estado_de_Mexico = 11
    Guanajuato = 12
    Guerrero = 13
    Hidalgo = 14   
    Jalisco = 15   
    Michoacan_de_Ocampo = 16
    Morelos = 17
    Nayarit = 18
    Nuevo_Leon = 19   
    Oaxaca = 20
    Puebla = 21   
    Queretaro = 22
    Quintana_Roo = 23
    San_Luis_Potosi = 24   
    Sinaloa = 25
    Sonora = 26  
    Tabasco = 27
    Tamaulipas = 28
    Tlaxcala = 29
    Veracruz = 30   
    Yucatan = 31
    Zacatecas = 32
    
    ESTADO = (
        (Aguascalientes,'Aguascalientes'),
        (Baja_California,'Baja California'),
        (Baja_California_Sur,'Baja California Sur'),
        (Campeche,'Campeche'),
        (Chiapas,'Chiapas'),
        (Chihuahua,'Chihuahua'),
        (Ciudad_de_Mexico,'Ciudad de Mexico'),
        (Coahuila,'Coahuila'),
        (Colima,'Colima'),
        (Durango,'Durango'),
        (Estado_de_Mexico,'Estado de Mexico'),
        (Guanajuato,'Guanajuato'),
        (Guerrero,'Guerrero'),
        (Hidalgo,'Hidalgo'),
        (Jalisco,'Jalisco'),
        (Michoacan_de_Ocampo,'Michoacan'),
        (Morelos,'Morelos'),
        (Nayarit,'Nayarit'),
        (Nuevo_Leon,'Nuevo Leon'),
        (Oaxaca,'Oaxaca'),
        (Puebla,'Puebla'),
        (Queretaro,'Queretaro'),
        (Quintana_Roo,'Quintana_Roo'),
        (San_Luis_Potosi,'San Luis Potosi'),
        (Sinaloa,'Sinaloa'),
        (Sonora,'Sonora'),
        (Tabasco,'Tabasco'),
        (Tamaulipas,'Tamaulipas'),
        (Tlaxcala,'Tlaxcala'),
        (Veracruz,'Veracruz'),
        (Yucatan,'Yucatan'),
        (Zacatecas,'Zacatecas'),

    )
    nombre_destinatario = models.CharField(max_length=50,)
    apellido_destinatario = models.CharField(max_length=50)
    empresa_destino = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.PositiveSmallIntegerField(choices=SEXO, default=mujer)
    telefono_destinatario = models.CharField(max_length=10, )
    calle = models.CharField(max_length=50,)
    numero_calle = models.CharField(max_length=15,)
    referencia =  models.CharField(max_length=100, blank=True, null=True)
    colonia =  models.CharField(max_length=50, )
    codigo_postal =  models.CharField(max_length=8,)
    ciudad =  models.CharField(max_length=50,)
    estado =  models.PositiveSmallIntegerField(choices=ESTADO, default=Quintana_Roo)
    pais =  models.CharField(max_length=50, blank=True, null=True)

    razon_social = models.CharField(max_length=100, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    email_facturacion = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, editable=False)

    #foreing key
    profile = models.ForeignKey(User, related_name='enviofacturacion_userprofile')