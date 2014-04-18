#-*-coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from artigo.views import *
from agenda.views import lista

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^galery/$',)
	url(r'^item/(?P<nr_item>\d+)/$', item, name='listar_por_item'),
	url(r'^add_artigo/$', adiciona, name='artigo_add'),
	url(r'^$', HomePageView.as_view(), name="home"),
	url(r'^about/$', TemplateView.as_view(template_name='about.tpl'), name='about'),
	url(r'^artigo_arquive/$', ArtigoListView.as_view(template_name='artigo/artigo_arquive.tpl'), name='artigo_arquive'),
	#url(r'^galery/$', GalleryImageView.as_view(template_name='galery.tpl'), name='galeria'),
	
	url(r'^admin/', include(admin.site.urls)),
	
	
	#url(r'^lista/$', ArtigoListView.as_view(), name='lista_artigo'),
	#url(r'^(?P<slug>[-_\w]+)/$', ArtigoDetailView.as_view(), name='artigo_detail'),
	#url(r'^contador/(?P<pk>\d+)/$', ArtigoContaRedirectView.as_view(), name='contador_redireciona'),
	#url(r'^(?P<ano>\d(4))/$', ArtigoAnoView.as_view(), name='artigo_por_ano'),
	#url(r'^archive/$', ArchiveIndexView.as_view(model=Artigo, date_field='publicacao'), name='artigo_arquive'),

	#========================================
	# pattern evento
	#===========================================
	#url(r'lista_evento/$', lista, name='lista_evento'),
	
)

#===========================================
#syntax for named regular-expression groups
# (?<name>pattern) 
# name is name of the group
#pattern same pattern to mach(coincidir)
#=============================================

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += staticfiles_urlpatterns()

''''
#https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/#module-django.contrib.staticfiles
if settings.DEBUG:
	urlpatterns += patterns('django.staticfiles.views',
	url(r'^static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_URL }),)#Note, the beginning of the pattern (r'^static/') should be your STATIC_URL setting.
'''