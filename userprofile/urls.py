from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
]