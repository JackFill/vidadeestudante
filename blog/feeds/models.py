#-*-coding:utf-8 -*-

from django.db import models
from django.contrib.syndication.views import Feed

from artigo.models import Artigo


class UltimosArtigos(Feed):
	title = " Ultimos Artigos Postados"
	link = "/artigos/" #endereco web desse artigo
	description = "Artigos mais recentes"
	
	
	def items(self):
		#return Artigo.objects.order_by('-publicacao')
		return Artigo.objects.all()
		
	
	def item_title(self, item):
		return item.title
		
		
	def item_description(self, item):
		return item.description
		
	
	
	'''
		só é necessário se não houver um método get_absolute_url no Artigo 
	'''
	#def item_link(self, item):
		#return reverse('novos artigos', args=[item.pk])