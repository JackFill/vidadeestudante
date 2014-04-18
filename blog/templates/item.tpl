{% extends "base.tpl" %}

	{% block content %}
	
		<h1>{{ item.titulo }}</h1>
		<p>{{ item.publicacao|date:'d/m/y' }}</p>
		<pre>
			{{ item.conteudo }}
		</pre>
		
	{% endblock %}