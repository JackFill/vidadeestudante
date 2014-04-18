#-*-coding:utf-8 -*-

from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class Evento(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	publicacao = models.DateTimeField(default=datetime.now, blank=True)
	slug = models.SlugField(max_length=100, blank=True, unique=True)
	
	class Meta:
		ordering = ('-publicacao',)
		
	
	def __unicode__(self):
		return self.titulo
		
		
	
	def was_published():
		recente = timezone.now() - timedelta(days=1)
		return self.publicacao >= recente
		publicacao_Recente.admin_order_field = 'publicacao'
		publicacao_Recente.boolean = True
		publicacao_Recente.short_description = 'Publicado Recentemente'
		
		
	
	
	
	def get_absolute_url(self):
		return reverse('event_archive', kwargs={'pk':pk})


