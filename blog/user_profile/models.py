#-*-coding:utf-8 -*-

from django.db import models
from django.forms import ModelForm



PF_CHOICES =(
	('ES', ),
	('WB', 'WEBDEVELOPMENT'),
	('PG', 'PROGRAMER'),
	('OT', 'OUTRO')
)

#https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/
class Autor(models.Model):
	image = models.ImageField()
	profissao = models.CharField(max_length=2, choices=UF_CHOICES)
	
	
	def __unicode__(self):
		return self.profisao
		
	
	
	def get_absolute_url(self):
		return('autor', kwargs={'pk':pk})
	


	
#https://docs.djangoproject.com/en/dev/topics/forms/modelforms/

class AutorForm(modelForm):
	class Meta:
		model = Autor
		fields = '__all__'
		
