<script type="text/javascript"> 
<!--

// (0=zero)fica direto, (1)rola uma vez. 
var repeat=0
var title=document.title
var leng=title.length
var start=1
function titlemove() {
titl=title.substring(start, leng) + title.substring(0, start)
document.title=titl
start++
if (start==leng+1) {
start=0
if (repeat==1)
return
}
//velocidade regule no 140
setTimeout("titlemove()",100)
}
if (document.title)
titlemove()

//-->
</script>
