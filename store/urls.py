from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from store import views

urlpatterns = [
	# url(r'^accounts/', include('allauth.urls')),
	url(r'^$', views.index, name="index" ),
	url(r'^desktop/$', views.desktop_list, name = "desktop_list"),
	url(r'^portatiles/$', views.portatiles_list, name = "portatiles_list"),
	url(r'^impresoras-tintas/$', views.impresoras_list, name = "impresoras_list"),
	url(r'^accesorios/$', views.accesorios_list, name = "accesorios_list"),
	url(r'^redes/$', views.redes_list, name = "redes_list"),
	url(r'^muebles-oficina/$', views.muebles_list, name = "muebles_list"),
	url(r'^mostrar-producto/([\w.@+-]+)/$', views.mostrar_producto, name = "mostrar_producto"),
	url(r'^shopping-cart/$', views.shopping_cart, name = "shopping_cart"),

]