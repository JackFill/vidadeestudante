<div id="wrapper">
	<div id="menu">
		{% block menu %} 
			<ul>
				<li><a href="/">Home</a></li>
				<li><a href="">Galeria</a></li>
				<li><a href="{% url "artigo_arquive" %}">Artigos</a></li>
				<li><a href="{% url "about" %}">Sobre</a></li>
				<li><a href="">Contato</a></li>
				<li><a href="">OMG</a></li>
				<li><a href="">Chat</a></li>
				<li><a href="">parceiros</a></li>
				<li><a href="{% url "artigo_add" %}">Novo</a></li>
			</ul>
		{% endblock %}
		
	</div>
</div>


