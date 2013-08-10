
$(document).ready(function(){
 
// Adding a Drop Down Login Form to Bootstrap’s Navbar
// http://mifsud.me/adding-dropdown-login-form-bootstraps-navbar/


$("#twitter").mouseenter(function(){
 $('#twitter').attr("src", "/media/icons/tweet2.png");
});

$("#twitter").mouseleave(function(){
 $('#twitter').attr("src", "/media/icons/tweet2bw.png");
});

 
  $(" #home ").mouseenter(function(){
    $("#home div").css("background-image","url('/media/icons/home2.png')");});
  $(" #home ").mouseleave(function(){
    $("#home div").css("background-image","url('/media/icons/home1.png')");});


   $(" #locality ").mouseenter(function(){
    $("#locality div").css("background-image","url('/media/icons/locality2.png')");});

  $(" #locality ").mouseleave(function(){
    $("#locality div").css("background-image","url('/media/icons/locality1.png')");});

  $(" #posts ").mouseenter(function(){
    $("#posts div").css("background-image","url('/media/icons/posts2.png')");});
  $(" #posts ").mouseleave(function(){
    $("#posts div").css("background-image","url('/media/icons/posts1.png')");});


$(" #suggestions ").mouseenter(function(){
    $("#suggestions div").css("background-image","url('/media/icons/suggestions2.png')");});
  $(" #suggestions ").mouseleave(function(){
    $("#suggestions div").css("background-image","url('/media/icons/suggestions1.png')");});

$(" #feedback ").mouseenter(function(){
    $("#feedback div").css("background-image","url('/media/icons/feedback22.png')");});
  $(" #feedback ").mouseleave(function(){
    $("#feedback div").css("background-image","url('/media/icons/feedback11.png')");});


  $(" #aboutus ").mouseenter(function(){
    $("#aboutus div").css("background-image","url('/media/icons/aboutus2.png')");});
  $(" #aboutus ").mouseleave(function(){
    $("#aboutus div").css("background-image","url('/media/icons/aboutus1.png')");});

  
   /* $(window).resize(function(){
        var h = $(window).height();
        var w = $(window).width();
        if(w < 1367) {
        $('body').width('1360px');
        }
        if(w > 1366) {
            $('body').width('100%');
            }
    });*/


$(function() {
    var button = $('#loginButton');
    var box = $('#loginBox');
    var form = $('#loginForm');
   
    button.removeAttr('a');
   
      button.click(function(login) {
        box.toggle();
        button.toggleClass('active');
    });
    
       box.mouseleave(function()
      {
              box.toggle();
        button.toggleClass('active');
      });
   
    
});


});
