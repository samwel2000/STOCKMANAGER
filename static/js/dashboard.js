$(document).ready(function(){
  $(".sidebar_toogle").click(function(){
    $(".sidebar_layout_main").toggleClass("sidebar_layout");
    $(".layout_content_main").toggleClass("layout_content");
  });
});
