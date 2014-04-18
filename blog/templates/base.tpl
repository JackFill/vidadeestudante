<!DOCTAPE 	HTML>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br" lang="pt-br">

<html lang="en">
	<head>
		<title>
			{% block title %}Bem vindo ao meu blog :: Tudo em um só lugar {% endblock %}
		</title>
		
		{% block meta %}
			<meta http-equiv="Content-type" content="text/html"; charset="utf-8" />
			<meta http-equiv="Content-Language" content="pt-br" />
			<meta name="Keywords" content="blog, Estudante, Vida de Estudante", blog vida de estudante />
			<meta name="description" content="Este blog foi criado afim de descrver, de modo engraçado, a vida diária de estudantes na escola" />
		{% endblock meta %}
		
		{% block style %}
			{% load staticfiles %}
			<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}" />
		{% endblock style %}
		
		{% block scripts %}
		{% endblock scripts %}
		
	</head>
	
	<body>
		<div id="all">
		
			<div id="bannertop">
			
				{% block bannertop %}
					<div class="photo">
						<!--add propaganda-->
					</div>
				{% endblock bannertop %}
				
			</div>
			
			
		
			<h1> {% block h1 %}{% endblock %}</h1>
		
			<div id="content" >
				{% include "menu.tpl" %}
				{% block content %} {% endblock %}
			</div>
		
			{% include "footer.tpl" %}
		</div>
	</body>
</html>