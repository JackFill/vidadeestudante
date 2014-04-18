#-*-coding:utf-8 -*-

from django.shortcuts import render_to_response
from models import Evento


def lista(request):
	lista_evento = Evento.objects.all()
	return render_to_response('evento/lista_evento.tpl', {'lista_evento': lista_evento})
	