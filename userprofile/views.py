# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy,reverse
# Create your views here.

# @transaction.atomic
def update_profile(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            first = user_form.cleaned_data['first_name']
            second = user_form.cleaned_data['last_name']
            tmp = "{0}@{1}".format(first,second)
            user.username = tmp
            user.save()

            perfil = profile_form.save(commit=False)
            perfil.user = user
            perfil.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'new_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })