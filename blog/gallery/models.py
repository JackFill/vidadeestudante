#-*-coding:utf-8 -*-

from django.db import models
from datetime import datetime
from django.db.models import signals
from django.template.defaultfilters import slugfy



"""Um album eh um pacote de imagens, ele tem um titulo e um slug para
sua identificacao."""
#http://www.aprendendodjango.com/uma-galeria-de-imagens-simples-e-util/
class Gallery(models.Model):
	titulo = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, blank=True, unique=True)
	
	
	class Meta:
		ordering=('titulo',)
		
	
	def __unicode__(self):
		return self.titulo

	#erro reverse sintax invalid
	def get_absolute_url(self):
		return reverse('gallery', *kwargs{'gallery': self.slug})
		



"""Cada instancia desta classe contem uma imagem da galeria, com seu
respectivo thumbnail (miniatura) e imagem em tamanho natural.
Varias imagens podem conter dentro de uma galeria"""		
		
class Image(models.Model):
	gallery = models.ForeignKey(Gallery)
	titulo = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True, help_text='Gerado automaticamente.')
	descricao = models.TextField(blank=True, help_text='Descreva esta imagem.(opcional)')
	original = models.ImageField( null=True, blank=True, upload_to='images/gallery/origin')
	thumbnail = models.ImageField(null=True, blank=True, upload_to='images/gallery/thumbs')
	publicacao = models.DateTimeField(default=datetime.now, blank=True)
	
	class Meta:
		ordering = ('gallery', 'titulo',)
		
		
	
	def __unicode__(self):
		return self.titulo

	
	def get_absolute_url(self):
		return reverse('image', **kwargs={'slug': self.slug })
		
	def save(self):
		
	

#http://schbank.wordpress.com/2010/09/28/django-application-a-simple-gallery/

signals.pre_save.connect(slug_pre_save, sender=Gallery)
signals.pre_save.connect(slug_pre_save, sender=Image)