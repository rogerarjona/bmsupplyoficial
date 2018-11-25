from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from store import views

urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
	url(r'^index/$', login_required(views.index), name="index" ),
]