# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib import messages
from django.db.models import Count, Sum, F, Func
from .models import *
from .forms import *

def index(request):
	lista_empresas = Partner.objects.all()
	user = request.user
	return render(request, 'lista_empresas.html', {'lista_empresas': lista_empresas, 'user':user})

def desktop_list(request):

	desktop = Product.objects.filter(category__name="Desktop")
	#discount = QuantityDiscount.objects.filter(quantity__lte=10).order_by('-quantity').first()
	total = list(ProductWarehouse.objects.filter(product__category__name="Desktop").values('product__id').annotate(total=Sum('quantity')))

	desktop_map = {}
	for d in desktop:
		id_desktop = str(d.id)
		desktop_map[id_desktop] = {'producto': d, 'cantidad': 0}

	for t in total:
		id_desktop = str(t['product__id'])
		if id_desktop in desktop_map:
			desktop_map[id_desktop]['cantidad'] = t['total']
	
	category = "Desktop"
	
	return render(request, 'lista_desktop.html', {'product_list':desktop_map, 'category':category})

def portatiles_list(request):

	portatil = Product.objects.filter(category__name="Portatiles")
	total = list(ProductWarehouse.objects.filter(product__category__name="Portatiles").values('product__id').annotate(total=Sum('quantity')))

	portatiles_map = {}
	for d in portatil:
		id_portatil = str(d.id)
		portatiles_map[id_portatil] = {'producto': d, 'cantidad': 0}

	for t in total:
		id_portatil = str(t['product__id'])
		if id_portatil in portatiles_map:
			portatiles_map[id_portatil]['cantidad'] = t['total']

	return render(request, 'lista_desktop.html', {'product_list':portatiles_map, 'category':'Portatiles'})

def redes_list(request):

	redes = Product.objects.filter(category__name="Redes")
	total = list(ProductWarehouse.objects.filter(product__category__name="Redes").values('product__id').annotate(total=Sum('quantity')))

	redes_map = {}
	for d in redes:
		id_redes = str(d.id)
		redes_map[id_redes] = {'producto': d, 'cantidad': 0}

	for t in total:
		id_redes = str(t['product__id'])
		if id_redes in redes_map:
			redes_map[id_redes]['cantidad'] = t['total']

	return render(request, 'lista_desktop.html', {'product_list':redes_map, 'category':'Redes'})

def accesorios_list(request):

	accesorios = Product.objects.filter(category__name="Accesorios")
	total = list(ProductWarehouse.objects.filter(product__category__name="Accesorios").values('product__id').annotate(total=Sum('quantity')))

	accesorios_map = {}
	for d in accesorios:
		id_accesorio = str(d.id)
		accesorios_map[id_accesorio] = {'producto': d, 'cantidad': 0}

	for t in total:
		id_accesorio = str(t['product__id'])
		if id_accesorio in accesorios_map:
			accesorios_map[id_accesorio]['cantidad'] = t['total']

	return render(request, 'lista_desktop.html', {'product_list':accesorios_map, 'category':'Accesorios'})

def impresoras_list(request):

	impresoras = Product.objects.filter(category__name="Impresoras y Tintas")
	total = list(ProductWarehouse.objects.filter(product__category__name="Impresoras y Tintas").values('product__id').annotate(total=Sum('quantity')))

	impresoras_map = {}
	for d in impresoras:
		id_impresora = str(d.id)
		impresoras_map[id_impresora] = {'producto': d, 'cantidad': 0}

	for t in total:
		id_impresora = str(t['product__id'])
		if id_impresora in impresoras_map:
			impresoras_map[id_impresora]['cantidad'] = t['total']

	return render(request, 'lista_desktop.html', {'product_list':impresoras_map, 'category':'Impresoras y Tintas'})

def muebles_list(request):

	muebles = Product.objects.filter(category__name="Muebles de Oficina")
	total = list(ProductWarehouse.objects.filter(product__category__name="Muebles de Oficina").values('product__id').annotate(total=Sum('quantity')))

	muebles_map = {}
	for d in muebles:
		id_mueble = str(d.id)
		muebles_map[id_mueble] = {'producto': d, 'cantidad': 0}

	for t in total:
		id_mueble = str(t['product__id'])
		if id_mueble in muebles_map:
			muebles_map[id_mueble]['cantidad'] = t['total']

	return render(request, 'lista_desktop.html', {'product_list':muebles_map, 'category':'Muebles de Oficina'})

def mostrar_producto(request, id):
	
	try:
		producto = Product.objects.get(id=id)
		productwarehouse = ProductWarehouse.objects.select_related('product', 'warehouse').filter(product=producto)
	except (Product.DoesNotExist, ProductWarehouse.DoesNotExist):
		producto = None
		productwarehouse = None
		
	if producto == None:
		return HttpResponseRedirect(reverse('index'))
	
	discount = QuantityDiscount.objects.all().order_by('quantity')
	prueba = 4500.2
	product_map = {}
	discount_map = {}
	for p in productwarehouse:
		id_producto = str(p.id)
		for d in discount:
			id_discount = str(d.id)
			discount_map[id_discount] = {'name': d.name, 'total': "{0:.2f}".format(p.price * d.mult)}
			
		product_map[id_producto] = {'producto': p, 'dis': discount_map}

	form = nuevoProductoCarrito()

	return render(request, 'mostrar_producto.html', {'producto':producto, 'productwarehouse':productwarehouse, 'product_map':product_map
		, 'prueba':prueba, 'form':form})

import decimal
def shopping_cart(request):

	user = request.user
	product_user = VentaTemporal.objects.filter(profile=user)

	total_sin_iva = 0
	envio_sin_iva = 0

	product_map = {}
	for product in product_user:
		id_producto = str(product.id)
		product_map[id_producto] = {'producto': product, 'total_producto': product.cantidad_producto * product.producto.price}

	for product in product_user:
		total_sin_iva += (product.cantidad_producto * product.producto.price)
		envio_sin_iva += (product.producto.product.send.cost)

	precio_total_sin_iva = total_sin_iva + envio_sin_iva
	total_iva = precio_total_sin_iva * decimal.Decimal(1.16)
	total_iva = "{0:.2f}".format(total_iva)
	precio_total = precio_total_sin_iva + decimal.Decimal(total_iva)
	precio_total = "{0:.2f}".format(precio_total)

	shopping_cart_form = CarritoForm()
	shopping_cart_form.initial['']

	return render(request, 'shopping_cart.html', {'product_user':product_user, 'product_map':product_map, 'total_sin_iva':total_sin_iva,
		'envio_sin_iva':envio_sin_iva, 'precio_total_sin_iva':precio_total_sin_iva, 'total_iva':total_iva, 'precio_total':precio_total})

# def envio_facturacion(request):
# 	user = request.user
	
# 	shopping_cart_form = CarritoForm(request.POST)

# 	if request.method == 'POST':
# 	 	envio_facturacion = EnvioFacturacionForm(request.POST)
# 	 	if envio_facturacion.is_valid():
# 	 		envio_facturacion_form = envio_facturacion.save(commit=false)
# 	 		envio_facturacion_form.profile

# 	else:
# 		envio_facturacion = EnvioFacturacionForm()

# 	return render(request, '')
