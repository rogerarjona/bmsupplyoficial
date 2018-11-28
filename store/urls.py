from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from store import views

urlpatterns = [
	# url(r'^accounts/', include('allauth.urls')),
	url(r'^$', views.desktop_list, name="index" ),
	url(r'^desktop/$', views.desktop_list, name = "desktop_list"),
	url(r'^portatiles/$', views.portatiles_list, name = "portatiles_list"),
	url(r'^impresoras-tintas/$', views.impresoras_list, name = "impresoras_list"),
	url(r'^accesorios/$', views.accesorios_list, name = "accesorios_list"),
	url(r'^redes/$', views.redes_list, name = "redes_list"),
	url(r'^muebles-oficina/$', views.muebles_list, name = "muebles_list"),
	url(r'^mostrar-producto/([\w.@+-]+)/$', views.mostrar_producto, name = "mostrar_producto"),
	url(r'^shopping-cart/$', login_required(views.shopping_cart), name = "shopping_cart"),
	url(r'^shopping-cart-add/([\w.@+-]+)/$', login_required(views.shopping_cart_add), name = "shopping_cart_add"),
	url(r'^direccion-facturacion/$', login_required(views.envio_facturacion), name = 'envio_facturacion' ),
	url(r'^envio-pago/([\w.@+-]+)/$', login_required(views.envio_pago), name = 'envio_pago' ),
	url(r'^factura/([\w.@+-]+)/$', login_required(views.factura_venta), name = 'factura_venta'),

]