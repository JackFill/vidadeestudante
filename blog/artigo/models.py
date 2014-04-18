#-*-coding:utf-8 -*-

from django.db import models, signals
from django.db.models.signals import pre_save
from datetime import datetime
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify



#https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/
class Artigo(models.Model):
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField(default=datetime.now, blank=True)
#https://docs.djangoproject.com/en/1.6/ref/contrib/admin/admindocs/	
	'''
		sinais permitem certos remetentes notificar um conjunto de receptores que alguma ação tenha ocorrido
	'''
	
	slug = models.SlugField(max_length=100, unique=True, blank=True)
#https://djangosnippets.org/snippets/728/
#https://pythonhosted.org/django-autoslug/fields.html
	
	
	
	class Meta:
		ordering = ('-publicacao',)
	
	def __unicode__(self):
		return self.titulo
	
	#gerando url unica para cada artigo
	def get_absolute_url(self):
		return reverse('artigo_arquive', kwargs={'slug': self.slug})
						#Uses a default template_name_suffix of _archive.

		

'''
	Django inclui um "despachante sinal" que ajuda a permitir que 
	aplicações dissociadas ser notificado quando as 
	ações ocorrem em outras partes do quadro. Em 
	poucas palavras, sinais permitem certos remetentes 
	notificar um conjunto de receptores que alguma ação 
	teve lugar. Eles são especialmente úteis quando muitas 
	peças de código podem estar interessados nos 
	mesmos eventos
'''		
	