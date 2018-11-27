#!
# -*- coding: utf-8 -*-
from django import forms

class nuevoProductoCarrito(forms.Form):
	id_producto = forms.CharField()
	cantidad = forms.CharField()
