 $(document).ready(function(){
 	var display= false
 	$('#settings').click(function(){

 		if(display == true)
 		{
 			
 			$('#change_password').hide('slow');
 			return display= false;

 		}

 		else
 		{
 			
 			$('#change_password').show('slow');
 			return display= true;
 		}




 	});
 });
