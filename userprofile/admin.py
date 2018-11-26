# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False

class UserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    search_fields = ('username','email','first_name', 'last_name') 
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined',)
    ordering = ('-date_joined',)

    def get_queryset(self, request):
        queryset = super(UserAdmin, self).get_queryset(request)
        queryset = queryset.select_related('profile',)
        return queryset

admin.site.unregister(User)
admin.site.register(User, UserAdmin)