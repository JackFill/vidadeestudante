{% extends "base.tpl" %}
<!--http://stackoverflow.com/questions/4226446/how-to-layout-a-image-gallery?rq=1-->
{% block content %}
	<div id="gallery">
		<div class="image">
			<img src= "{% url %}"/>
			<div class="placeholder">
				<p> description</p>
			</div>
		</div>
		<div class="image">
			<img src=""/>
			<div class="placeholder">
				<p>description<p/>
			</div>
		</div>
	
	</div>

{% endblock %}