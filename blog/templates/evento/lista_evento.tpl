{% extends "base.tpl" %}

{%block content %}
	<a href="/adiciona/">Add novo evento</a>
	<ul>
		{% for evento in lista_evento %}
			<li>
				<a href="/evento/{{ evento.id }}">
					{{ evento.data|date: 'd/m/y' }} {{ evento.titulo }}
				</a>
			</li>
		
		{% empty %}
				<li>Nao ha Evento </li>
		
		{% endfor %}
		
	
	</ul>

{% endblock %}