#!
# -*- coding: utf-8 -*-
from django import forms
from .forms import *
from .models import EnvioFacturacion

class nuevoProductoCarrito(forms.Form):
	id_producto = forms.CharField()
	cantidad = forms.CharField()

class CarritoForm(forms.Form):

	precio_total_sin_iva = forms.CharField()
	total_iva = forms.CharField()
	precio_total = forms.CharField()
	total_sin_iva = forms.CharField()
	envio_sin_iva = forms.CharField()
	cantidad_producto = forms.CharField()

class EnvioFacturacionForm(forms.ModelForm):
	class Meta:
		model = EnvioFacturacion
		exclude = ('profile', 'created', 'pais') 