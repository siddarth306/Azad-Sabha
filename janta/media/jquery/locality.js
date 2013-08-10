
$(document).ready(function()
{


});
function show_post()
{
  //alert("working");
   $('#issuelist').toggle(1000);//load('issuetitle.html', '#post_public');
   $('#showissue').show(1000);
   $('#post_comment').show(1000);
   //$('#issuelist').slideup(1000);
}

$('#post_title').click( function() {
  $(this).prop('href', 'http://www.google.com/');
});
