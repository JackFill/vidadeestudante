<h1>Artigos</h1>
<ul>
	{% for artigo in object_list %}
		<li> {{ artigo.publicacao|date }} - {{ artigo.headline }}</li>
	{% empty %}
		<li> N�o h� artigos ainda</li>
	{% endfor %}
</ul>