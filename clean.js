
<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){
    var t_h = $("div.article").html();
    var wi = $("div.article").width();
    $("body").find("*").removeAttr("width");
    $("body").empty().html("<div>"+t_h+"</div>");
    $("body").empty().width(wi).html("<div>"+t_h+"</div>");
});
</script>

