# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib import messages
from .models import *

def index(request):
	lista_empresas = Partner.objects.all()
	user = request.user
	return render(request, 'lista_empresas.html', {'lista_empresas': lista_empresas, 'user':user})

def desktop_list(request):

	desktop = Product.objects.filter(category__name="Desktop")
	return render(request, 'lista_desktop.html', {'product_list':desktop})

def portatiles_list(request):

	portatil = Product.objects.filter(category__name="Portatiles")
	return render(request, 'lista_desktop.html', {'product_list':portatil})

def redes_list(request):

	redes = Product.objects.filter(category__name="Redes")
	return render(request, 'lista_desktop.html', {'product_list':redes})

def accesorios_list(request):

	accesorios = Product.objects.filter(category__name="Accesorios")
	return render(request, 'lista_desktop.html', {'product_list':accesorios})

def impresoras_list(request):

	impresoras = Product.objects.filter(category__name="Accesorios")
	return render(request, 'lista_desktop.html', {'product_list':impresoras})

def muebles_list(request):

	muebles = Product.objects.filter(category__name="Accesorios")
	return render(request, 'lista_desktop.html', {'product_list':muebles})

def mostrar_producto(request, id):
	try:
		producto = Product.objects.get(id=id)
	except Product.DoesNotExist:
		producto = None
	
	if producto == None:
		return HttpResponseRedirect(reverse('index'))

	return render(request, 'mostrar_producto.html', {'producto':producto})
# def sucursal(request):
# 	empresa = request.user.perfilusuario.empresa
# 	lista_sucursal = Sucursal.objects.filter(empresa = empresa)
# 	return render(request, 'lista_sucursal.html', {'lista_sucursal': lista_sucursal} )
