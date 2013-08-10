
function get()
{
 
 var input = $('#comment').val();
 if ( $('#comment').val() == '' ){
 alert('Empty!!!');}
 else{
 $('#post_public1').append('<span style="color:gray;font-family:times new roman;cursor:hand;">Username:</span> &nbsp;'+input + '<br/><br/> <hr>');}
 };
function get_issue()
{
 var input = $('#post_issue').val();

 if ( $('#post_issue').val() == '' ){
 alert('Empty!!!');}
 else{

  alert('succesed');
 $('#post_issue').append('<span style="color:gray;font-family:times new roman;cursor:hand;">Username:</span> &nbsp;'+input + '<br/><br/> <hr>');}
 
 
 };
 function show_issue()
 {

 	for (i=0;i<index;i++)
{
	 document.write('<form name="frm">POSTS {{a}}<br>');

//$('#post_issue').append('<img src="janta.jpg" width="40px" height="40px"style="display:inline;float:left;">&nbsp;'+'<span style="color:gray;font-family:times new roman;">Username:</span> &nbsp;'+issues[] + '<br/><br/> <hr>');}
 
}
 };


/* 	commentHeight = $(#postcomment).css("height") - 370;
 	if(commentHeight > 800){
 		$(#wrap).css('height:', '1500px')*/
 
