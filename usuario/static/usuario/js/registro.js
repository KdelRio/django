$.validator.setDefaults( {
    submitHandler: function () {
		alert( "Cuenta creada!, seras redirigido al login" );
		('#registrarse').attr('href','./Login.html');
	  }
    }
 );
 
 $(document).ready(function(){
	 $('#register-form').validate({
		rules: {
		   nombre: {
			  required: true,
			  minlength: 2
		   },
		   apellido: {
			  required: true,
			  minlength: 4,
		   },
		   correo: {
			  required: true,
			  email: true
		   },
		   telefono: {
			  required: true,
			  number: true,
			  minlength: 8
		   },
		   contraseña: {
			  required: true,
			  minlength: 6
		   },
		   tyc: {
			  required: true
		   },
		   agree: "required"
		},
		messages: {           
		   nombre: {
			  required: "Por favor ingresa tu nombre",
			  minlength: "Tu Nombre debe ser de no menos de 2 caracteres de longitud"
		   },
		   apellido: {
			  required: "Por favor ingresa tu apellido",
			  minlength: "Tu apellido debe ser de no menos de 4 caracteres de longitud"
		   },
		   correo: {
			  required: "Por favor ingresa un correo valido",
			  email: "Debe contener @; ejemplo@gmail.com"
		   },
		   telefono: {
			  required: "Por favor ingresa tu numero de telefono",
			  minlength: "Debe contener almenos 8 numeros"
		   },
		   contraseña: {
			  required: "Por favor ingresa tu contraseña",
			  minlength: "Tu contraseña debe ser de no menos de 6 caracteres de longitud"
		   },
		   tyc: {
			  required: "Esta Casilla es obligatoria."
		 }
		},
	 });
  });
 
 


 
 