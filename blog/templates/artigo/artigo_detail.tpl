<h1>
	{{ object.headline }}
	
</h1>
<p> {{ object.content }}</p>
<p> Reporter: {{ object.reporter }} </p>
<p> Publicado: {{ object.publicacao|date }}</p>
<p>Date: {{ now|date }}</p>