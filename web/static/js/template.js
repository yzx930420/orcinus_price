$(function(){
   $(".search_option").each(function(){
       $(this).click(function(){
          var option = $(this).html() + "<span class='caret'></span>";
          $("#action").val($(this).attr("action"));
          $("#search_type").html(option);
       });
   }) ;
});