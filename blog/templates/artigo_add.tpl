{% extends "base.tpl" %}
	
	{%block content %}
		
		<form action"" method="post">
			{% csrf_token %}
			{{ form.as_p}}
			<button type="submit" >Adicionar</button>
		</form>
		
	{% endblock %}