{% extends "base.tpl" %}

	{% block content %}
		<p> salvo com sucesso</p>
		<a href="{% url "home" %}" >voltar a homepage</a><br />
		<a href="{% url "artigo_add" %}">Adicionar novo</a>
		
	{% endblock %}