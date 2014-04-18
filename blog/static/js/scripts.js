<script type="text/javascript">
	$(document).ready(function){
		$('#gallery .image p').hide();
		$('#gallery .image').hover(
		function() { $(this) .find('p').show() },
		function() { $(this) .find('p') .hide() }
		);
	});
</script>