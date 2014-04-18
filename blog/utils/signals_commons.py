#-*-coding:utf-8 -*-
from django.template.defaultfilters import Slugify

"""Este signal gera um slug automaticamente. Ele verifica se ja existe um
    objeto com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade"""


def slug_pre_save(signal, instance, sender, **kwargs):
	if not instance.slug:
		slug = slugfy(instance.titulo)
		new_slug = slug
		counter = 0
		
		
		while sender.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
			counter +=1
			new_slug = '%s - %d' %(slug, counter)
		
		instance.slug = new_slug