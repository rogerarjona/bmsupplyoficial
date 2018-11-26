from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from userprofile import views

urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
	url(r'^crear-cuenta/$', views.update_profile, name="update_profile")
]