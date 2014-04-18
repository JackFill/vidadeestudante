#-*-coding:utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns =patterns('gallery.views',
	url(r'^$', GalleryView.as_view(template_name='gallery.tpl'))
	
)