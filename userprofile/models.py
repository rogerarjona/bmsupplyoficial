# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	
	personal_user = 0
	entrepreneur = 1
	microempresa = 2
	pequena_empresa = 3
	mediana_empresa = 4
	grande_empresa = 5


	industria = 0
	comercio = 1
	servicios = 2
	educacion = 3 
	gobierno = 4


	TIPO_USUARIO = (
		(personal_user, 'Usuario Personal'),
		(entrepreneur, 'Emprendedor'),
		(microempresa, 'Microempresa'),
		(pequena_empresa, 'Pequeña'),
		(mediana_empresa, 'Mediana'),
		(grande_empresa, 'Grande')
	)

	GIRO = (
		(industria, 'Industria'),
		(comercio, 'Comercio'),
		(servicios, 'Servicios'),
		(educacion, 'Educacion'),
		(gobierno, 'Gobierno'),
	)

	phone = models.CharField(max_length=20, blank=True)
	enterprise_size = models.PositiveSmallIntegerField(choices=TIPO_USUARIO, default=personal_user)
	enterprise_type = models.PositiveSmallIntegerField(choices=GIRO, default=comercio)
	news = models.BooleanField(default=True)
	sure = models.BooleanField(default=True)
	#Foreign Key
	user = models.OneToOneField(User, )

