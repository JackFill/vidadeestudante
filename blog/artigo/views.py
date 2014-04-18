#-*-coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

#=============teste def ==================
from django.template import RequestContext
from django.http import Http404



from models import Artigo
from forms import FormAddArtigo


#https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#django.views.generic.base.View
#templateView renderiza um template determinado na definicao template_name
class HomePageView(TemplateView):
	template_name = "home.tpl"
	
	#retorna um dicionario representando o contexto do template
	#os argumentos fornecidos se tornarao o contexto retornados
	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['artigo_index'] = Artigo.objects.all() [:2] #retorna apenas os 2 primeiros objetos
		#Uses a default context_object_name of latest.artigo_index deve ser usado no template.ex:{% for some in artigo_index %}
		return context

'''
https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/#listview
'''
#listando arquivos	ok	
class ArtigoListView(ListView):
	model = Artigo
	
	
	def get_context_data(self, **kwargs):
		context = super(ArtigoListView, self).get_context_data(**kwargs)
		context['latest'] = timezone.now()
		return context


#add artigos
class ArtigoCreateView(CreateView):
	model = Artigo
	fields = ['titulo', 'conteudo','publicacao']
	form_class = FormAddArtigo
	sucess_url = 'artigo_arquive'
	template_name='artigo_add.tpl'

	
#endblock		

#class ContatoView()
#resolver logica tratamento de imagem exibição


#https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/
#https://docs.djangoproject.com/en/dev/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data
	
#https://docs.djangoproject.com/en/dev/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names	


#https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/



#endblock
		
		

		

#listando artigos por ano
#https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/



#add artigo
def adiciona(request):
	
	if request.method=='POST':
		form = FormAddArtigo(request.POST, request.FILES)
		if form.is_valid():
			dados = form.cleaned_data
			item = Artigo(**dados)
			item.save()
			#html exibindo quando for salvo
			return render_to_response("save.tpl", {})
	else:
		form=FormAddArtigo()
		
	return render_to_response("artigo_add.tpl", {'form':form}, context_instance=RequestContext(request))



def item(request, nr_item):
		try:
			item = Artigo.objects.get(pk=nr_item)
		except Artigo.DoesNotExist:
			raise Http404()
		return render_to_response('item.tpl', {'item':item})
		