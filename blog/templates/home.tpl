{% extends "base.tpl" %}

{% block content %}
	{% load staticfiles %}
		<img src="{% static "images/perfil/user.png" %}" alt="User" />
	
	
	{% for object in artigo_index %}
		
		<div id="artigo">
			<h1 id="titulo"><a href="/object/{{ object.id }}">{{ object.titulo }}</a></h1> {{ object.conteudo }}
		</div>
		{% empty %}
			<li> Não Há Artigos</li>
	{% endfor %}
	<!-- https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/#std:templatetag-staticfiles-static-->
	
	
{% endblock %}