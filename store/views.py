# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.urlresolvers import reverse_lazy,reverse
from .models import *

def index(request):
	lista_empresas = Partner.objects.all()
	user = request.user
	return render(request, 'lista_empresas.html', {'lista_empresas': lista_empresas, 'user':user})

# def sucursal(request):
# 	empresa = request.user.perfilusuario.empresa
# 	lista_sucursal = Sucursal.objects.filter(empresa = empresa)
# 	return render(request, 'lista_sucursal.html', {'lista_sucursal': lista_sucursal} )
