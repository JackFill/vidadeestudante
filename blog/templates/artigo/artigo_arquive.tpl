{% extends "base.tpl" %}

{% block content %}
	{% load staticfiles %}
	<ul>
		{% for artigo in object_list %}
			<li> {{ artigo.publicacao}}: <a href="/artigo/{{ artigo.id }}"> {{ artigo.titulo }}</a> </li>
		{% endfor %}
  
	</ul>

{% endblock %}