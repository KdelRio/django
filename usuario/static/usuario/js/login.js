$.validator.setDefaults( {
    submitHandler: function () {
		alert( "Datos Correctos, Ingresando!" );
		('#ingresar').attr('href','./cuenta.html');
	  }
    }
 );

 $(document).ready(function(){
	 $('#loginform').validate({
		rules: {
		   correo: {
			  required: true,
			  email: true
		   },
		   contraseña: {
			  required: true,
			  minlength: 6
		   },
		   agree: "required"
		},
		messages: {           
		 correo: {
			  required: "Por favor ingresa un correo valido",
			  email: "Debe contener @; ejemplo@gmail.com"
		   },
		   contraseña: {
			  required: "Por favor ingresa una contraseña",
			  minlength: "Tu contraseña debe ser de no menos de 6 caracteres de longitud"
		   },
		},
	 });
  });
 
 


 
 